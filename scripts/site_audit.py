#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
from xml.etree import ElementTree as ET

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
QUALITY_DIR = ROOT / "quality"
QUALITY_DIR.mkdir(exist_ok=True)
SITE_ORIGIN = "https://byteseismic.com"

SKIP_DIRS = {".git", ".cache", "node_modules", "assets", "quality", "research", "__pycache__"}
ORPHAN_ALLOWLIST = {
    "/",
    "/search/",
    "/guided-reading/",
    "/concept-glossary/",
    "/quality-review/",
    "/recent-posts-expanded-version/",
    "/byteseismic-podcasts/",
    "/menu-structure/",
}
ASSET_LIMITS = {
    ".css": 180_000,
    ".js": 280_000,
    ".jpg": 250_000,
    ".jpeg": 250_000,
    ".png": 250_000,
    ".webp": 250_000,
    ".svg": 120_000,
    ".ico": 120_000,
}
STYLE_SCARS = {
    "anchor-scaffold": re.compile(r"\bThe reader should be able to say what confusion appears when those distinctions are blurred together\b", re.I),
    "point-here": re.compile(r"\bThe point here is not to memorize a conclusion\b", re.I),
    "at-its-strongest": re.compile(r"\bAt its strongest\b", re.I),
    "first-anchor": re.compile(r"\bThe first anchor is\b", re.I),
    "anchors-here": re.compile(r"\bThe anchors here are\b", re.I),
    "decorate-it": re.compile(r"\bnarrow the field\s*<em>rather than</em>\s*merely decorate it\b", re.I),
    "prompt-leak": re.compile(r"\bThis inquiry seeks to identify the necessary and sufficient\b", re.I),
}
GRAMMAR_SCARS = {
    "double-the": re.compile(r"\bthe the\b", re.I),
    "double-of": re.compile(r"\bof of\b", re.I),
    "double-and": re.compile(r"\band and\b", re.I),
    "double-to": re.compile(r"\bto to\b", re.I),
    "double-is": re.compile(r"\bis is\b", re.I),
}
NOINDEX_PATHS = {
    "/byteseismic-podcasts/",
    "/quality-review/",
    "/recent-posts-expanded-version/",
}


def expected_noindex(page: str) -> bool:
    return page in NOINDEX_PATHS or page.startswith("/tags/")


def site_path(file_path: Path) -> str:
    rel = file_path.relative_to(ROOT)
    if rel == Path("index.html"):
        return "/"
    return f"/{rel.parent.as_posix()}/"


def target_file_for_path(path: str) -> Path:
    if path in {"", "/"}:
        return ROOT / "index.html"
    if path == "/index.html":
        return ROOT / "index.html"
    if path.endswith("/index.html"):
        return target_file_for_path(path[:-10] or "/")
    if path.endswith(".html"):
        return ROOT / path.lstrip("/")
    return ROOT / path.strip("/") / "index.html"


def normalize_site_target(path: str) -> str:
    if not path or path == "/index.html":
        return "/"
    if path.endswith("/index.html"):
        path = path[:-10] or "/"
    if path.endswith(".html"):
        return path
    if not path.endswith("/"):
        path = f"{path}/"
    return path


def canonical_for_page(page: str) -> str:
    return f"{SITE_ORIGIN}{page}"


def meta_content(soup: BeautifulSoup, *, name: str | None = None, prop: str | None = None) -> str:
    attrs = {"name": name} if name else {"property": prop}
    node = soup.find("meta", attrs=attrs)
    return (node.get("content") or "").strip() if node else ""


def canonical_href(soup: BeautifulSoup) -> str:
    node = soup.find("link", rel=lambda value: value and "canonical" in value)
    return (node.get("href") or "").strip() if node else ""


def json_ld_payloads(soup: BeautifulSoup, page: str, issues: list[dict]) -> list[dict]:
    payloads: list[dict] = []
    for index, node in enumerate(soup.find_all("script", attrs={"type": "application/ld+json"}), start=1):
        raw = node.string or node.get_text("", strip=True)
        if not raw.strip():
            issues.append({"page": page, "issue": f"empty JSON-LD script #{index}"})
            continue
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            issues.append({"page": page, "issue": f"invalid JSON-LD script #{index}: {exc.msg}"})
            continue
        if isinstance(parsed, list):
            payloads.extend(item for item in parsed if isinstance(item, dict))
        elif isinstance(parsed, dict):
            payloads.append(parsed)
    return payloads


def payload_types(payload: dict) -> set[str]:
    values: set[str] = set()
    raw_type = payload.get("@type")
    if isinstance(raw_type, str):
        values.add(raw_type)
    elif isinstance(raw_type, list):
        values.update(item for item in raw_type if isinstance(item, str))
    graph = payload.get("@graph")
    if isinstance(graph, list):
        for node in graph:
            if isinstance(node, dict):
                values.update(payload_types(node))
    return values


def has_json_ld_type(payloads: list[dict], target: str) -> bool:
    return any(target in payload_types(payload) for payload in payloads)


def sitemap_paths() -> set[str]:
    target = ROOT / "sitemap.xml"
    if not target.exists():
        return set()
    try:
        tree = ET.parse(target)
    except ET.ParseError:
        return set()
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    paths: set[str] = set()
    for loc in tree.findall(".//sm:loc", namespace):
        url = (loc.text or "").strip()
        if not url.startswith(SITE_ORIGIN):
            continue
        paths.add(normalize_site_target(urlparse(url).path or "/"))
    return paths


def robots_disallows() -> list[str]:
    target = ROOT / "robots.txt"
    if not target.exists():
        return []
    disallows = []
    for raw_line in target.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line.lower().startswith("disallow:"):
            continue
        value = line.split(":", 1)[1].strip()
        if value:
            disallows.append(value)
    return disallows


def internal_target(current: str, href: str) -> tuple[str, str] | None:
    if not href:
        return None
    parsed = urlparse(href)
    if parsed.scheme or href.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    absolute = urlparse(urljoin(f"https://byteseismic.com{current}", href))
    return normalize_site_target(absolute.path or current), unquote(absolute.fragment or "")


def html_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("index.html")
        if not any(part in SKIP_DIRS for part in path.parts)
    )


def extract_ids(soup: BeautifulSoup) -> set[str]:
    return {node.get("id") for node in soup.select("[id]") if node.get("id")}


def heading_duplicates(soup: BeautifulSoup) -> list[str]:
    counts: Counter[str] = Counter()
    for heading in soup.select("h1, h2, h3"):
        text = " ".join(heading.get_text(" ", strip=True).split())
        if text:
            counts[text] += 1
    return [text for text, count in counts.items() if count > 1]


def prompt_numbers(soup: BeautifulSoup) -> list[int]:
    values: list[int] = []
    for badge in soup.select(".article-section--prompt .article-section__number"):
        text = badge.get_text(" ", strip=True)
        if text.isdigit():
            values.append(int(text))
    return values


def numbers_are_sequential(values: list[int]) -> bool:
    return not values or values == list(range(1, len(values) + 1))


def audit() -> dict:
    pages = html_files()
    page_by_path = {site_path(path): path for path in pages}
    ids_by_path: dict[str, set[str]] = {}
    soups: dict[str, BeautifulSoup] = {}
    robots_by_path: dict[str, str] = {}
    title_counts: Counter[str] = Counter()
    description_counts: Counter[str] = Counter()
    duplicate_ids: list[dict] = []
    repeated_headings: list[dict] = []
    prompt_number_issues: list[dict] = []
    seo_issues: list[dict] = []
    json_ld_issues: list[dict] = []

    for path in pages:
        soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
        page = site_path(path)
        soups[page] = soup
        ids_by_path[page] = extract_ids(soup)

        title = " ".join((soup.title.get_text(" ", strip=True) if soup.title else "").split())
        description = meta_content(soup, name="description")
        robots = meta_content(soup, name="robots").lower()
        canonical = canonical_href(soup)
        og_title = meta_content(soup, prop="og:title")
        og_description = meta_content(soup, prop="og:description")
        og_image = meta_content(soup, prop="og:image")
        og_url = meta_content(soup, prop="og:url")
        twitter_card = meta_content(soup, name="twitter:card")
        h1_count = len(soup.select("h1"))
        is_noindex = "noindex" in robots
        robots_by_path[page] = robots

        if title:
            title_counts[title] += 1
        else:
            seo_issues.append({"page": page, "issue": "missing title"})
        if description:
            description_counts[description] += 1
            if not is_noindex and len(description) > 170:
                seo_issues.append({"page": page, "issue": f"meta description too long ({len(description)} chars)"})
        else:
            seo_issues.append({"page": page, "issue": "missing meta description"})
        if not robots:
            seo_issues.append({"page": page, "issue": "missing robots meta"})
        elif expected_noindex(page) and "noindex" not in robots:
            seo_issues.append({"page": page, "issue": "expected noindex robots meta"})
        elif not expected_noindex(page) and "noindex" in robots:
            seo_issues.append({"page": page, "issue": "unexpected noindex robots meta"})
        expected_canonical = canonical_for_page(page)
        if not canonical:
            seo_issues.append({"page": page, "issue": "missing canonical URL"})
        elif canonical != expected_canonical:
            seo_issues.append({"page": page, "issue": f"canonical mismatch ({canonical})"})
        if h1_count != 1:
            seo_issues.append({"page": page, "issue": f"expected exactly one h1, found {h1_count}"})
        if not og_title:
            seo_issues.append({"page": page, "issue": "missing og:title"})
        if not og_description:
            seo_issues.append({"page": page, "issue": "missing og:description"})
        if not og_url:
            seo_issues.append({"page": page, "issue": "missing og:url"})
        if not og_image:
            seo_issues.append({"page": page, "issue": "missing og:image"})
        if not twitter_card:
            seo_issues.append({"page": page, "issue": "missing twitter:card"})

        payloads = json_ld_payloads(soup, page, json_ld_issues)
        body = soup.find("body")
        page_type = body.get("data-page-type", "") if body else ""
        is_article = page_type == "article" or meta_content(soup, prop="og:type") == "article"
        is_archive = page_type == "archive"
        if not is_noindex:
            if not has_json_ld_type(payloads, "WebSite"):
                seo_issues.append({"page": page, "issue": "missing WebSite JSON-LD"})
            if page != "/" and not has_json_ld_type(payloads, "BreadcrumbList"):
                seo_issues.append({"page": page, "issue": "missing BreadcrumbList JSON-LD"})
            if is_article:
                article_payloads = [payload for payload in payloads if "Article" in payload_types(payload)]
                if not article_payloads:
                    seo_issues.append({"page": page, "issue": "missing Article JSON-LD"})
                else:
                    article = article_payloads[0]
                    if not article.get("datePublished"):
                        seo_issues.append({"page": page, "issue": "Article JSON-LD missing datePublished"})
                    if not article.get("dateModified"):
                        seo_issues.append({"page": page, "issue": "Article JSON-LD missing dateModified"})
            if is_archive and not has_json_ld_type(payloads, "CollectionPage"):
                seo_issues.append({"page": page, "issue": "archive page missing CollectionPage JSON-LD"})

        counts = Counter(node.get("id") for node in soup.select("[id]") if node.get("id"))
        duplicate_ids.extend(
            {"page": page, "id": dup_id, "count": count}
            for dup_id, count in counts.items()
            if count > 1
        )
        repeated_headings.extend(
            {"page": page, "heading": heading}
            for heading in heading_duplicates(soup)
        )
        values = prompt_numbers(soup)
        if values and not numbers_are_sequential(values):
            prompt_number_issues.append({"page": page, "numbers": values})

    duplicate_titles = [
        {"title": title, "count": count}
        for title, count in sorted(title_counts.items())
        if count > 1
    ]
    duplicate_descriptions = [
        {"description": description, "count": count}
        for description, count in sorted(description_counts.items())
        if count > 1
    ]

    broken_links: list[dict] = []
    inbound_counts: Counter[str] = Counter()
    for current, soup in soups.items():
        for node in soup.select("a[href]"):
            href = node.get("href", "").strip()
            target = internal_target(current, href)
            if not target:
                continue
            target_path, fragment = target
            if target_path.startswith("/assets/"):
                continue
            target_file = target_file_for_path(target_path)
            if not target_file.exists():
                broken_links.append({"page": current, "href": href, "reason": "missing target"})
                continue
            target_site_path = site_path(target_file)
            if target_site_path != current:
                inbound_counts[target_site_path] += 1
            if fragment and fragment not in ids_by_path.get(target_site_path, set()):
                broken_links.append({"page": current, "href": href, "reason": f"missing anchor #{fragment}"})

    orphan_pages = [
        page for page in sorted(page_by_path)
        if page not in ORPHAN_ALLOWLIST and inbound_counts.get(page, 0) == 0
    ]

    sitemap_index = sitemap_paths()
    sitemap_issues = []
    for page in sorted(page_by_path):
        is_noindex = "noindex" in robots_by_path.get(page, "")
        if is_noindex and page in sitemap_index:
            sitemap_issues.append({"page": page, "issue": "noindex page appears in sitemap"})
        if not is_noindex and page not in sitemap_index:
            sitemap_issues.append({"page": page, "issue": "indexable page missing from sitemap"})
    for page in sorted(sitemap_index):
        if page not in page_by_path:
            sitemap_issues.append({"page": page, "issue": "sitemap URL has no local HTML page"})

    disallows = robots_disallows()
    robots_issues = []
    for page, robots in sorted(robots_by_path.items()):
        if "noindex" not in robots:
            continue
        for rule in disallows:
            if page.startswith(rule.rstrip("*")):
                robots_issues.append({"page": page, "issue": f"noindex page blocked by robots rule {rule}"})
                break

    oversized_assets = []
    for path in sorted((ROOT / "assets").rglob("*")):
        if not path.is_file():
            continue
        limit = ASSET_LIMITS.get(path.suffix.lower())
        if limit and path.stat().st_size > limit:
            oversized_assets.append(
                {
                    "path": f"/{path.relative_to(ROOT).as_posix()}",
                    "bytes": path.stat().st_size,
                    "limit": limit,
                }
            )

    style_scars = []
    grammar_scars = []
    for page, soup in soups.items():
        text = soup.get_text("\n", strip=True)
        for label, pattern in STYLE_SCARS.items():
            if pattern.search(text):
                style_scars.append({"page": page, "issue": label})
        for label, pattern in GRAMMAR_SCARS.items():
            if pattern.search(text):
                grammar_scars.append({"page": page, "issue": label})

    summary = {
        "pages_scanned": len(pages),
        "broken_links": len(broken_links),
        "duplicate_ids": len(duplicate_ids),
        "repeated_headings": len(repeated_headings),
        "prompt_number_issues": len(prompt_number_issues),
        "orphan_pages": len(orphan_pages),
        "oversized_assets": len(oversized_assets),
        "style_scars": len(style_scars),
        "grammar_scars": len(grammar_scars),
        "seo_issues": len(seo_issues),
        "duplicate_titles": len(duplicate_titles),
        "duplicate_descriptions": len(duplicate_descriptions),
        "json_ld_issues": len(json_ld_issues),
        "sitemap_issues": len(sitemap_issues),
        "robots_issues": len(robots_issues),
    }
    return {
        "summary": summary,
        "broken_links": broken_links,
        "duplicate_ids": duplicate_ids,
        "repeated_headings": repeated_headings,
        "prompt_number_issues": prompt_number_issues,
        "orphan_pages": orphan_pages,
        "oversized_assets": oversized_assets,
        "style_scars": style_scars,
        "grammar_scars": grammar_scars,
        "seo_issues": seo_issues,
        "duplicate_titles": duplicate_titles,
        "duplicate_descriptions": duplicate_descriptions,
        "json_ld_issues": json_ld_issues,
        "sitemap_issues": sitemap_issues,
        "robots_issues": robots_issues,
    }


def write_report(payload: dict) -> None:
    (QUALITY_DIR / "site-audit.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    summary = payload["summary"]
    lines = [
        "# Site Audit",
        "",
        f"- Pages scanned: {summary['pages_scanned']}",
        f"- Broken internal links: {summary['broken_links']}",
        f"- Duplicate IDs: {summary['duplicate_ids']}",
        f"- Repeated headings: {summary['repeated_headings']}",
        f"- Prompt numbering issues: {summary['prompt_number_issues']}",
        f"- Orphan pages: {summary['orphan_pages']}",
        f"- Oversized assets: {summary['oversized_assets']}",
        f"- Style scars: {summary['style_scars']}",
        f"- Grammar scars: {summary['grammar_scars']}",
        f"- SEO issues: {summary['seo_issues']}",
        f"- Duplicate titles: {summary['duplicate_titles']}",
        f"- Duplicate descriptions: {summary['duplicate_descriptions']}",
        f"- JSON-LD issues: {summary['json_ld_issues']}",
        f"- Sitemap issues: {summary['sitemap_issues']}",
        f"- Robots/noindex issues: {summary['robots_issues']}",
        "",
    ]

    def add_block(title: str, rows: list[str]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        lines.extend(rows[:50] if rows else ["- none"])
        lines.append("")

    add_block("Broken Links", [f"- `{row['page']}` -> `{row['href']}` ({row['reason']})" for row in payload["broken_links"]])
    add_block("Duplicate IDs", [f"- `{row['page']}` -> `{row['id']}` x{row['count']}" for row in payload["duplicate_ids"]])
    add_block("Repeated Headings", [f"- `{row['page']}` -> {row['heading']}" for row in payload["repeated_headings"]])
    add_block("Prompt Numbering Issues", [f"- `{row['page']}` -> {row['numbers']}" for row in payload["prompt_number_issues"]])
    add_block("Orphan Pages", [f"- `{row}`" for row in payload["orphan_pages"]])
    add_block("Oversized Assets", [f"- `{row['path']}` -> {row['bytes']} bytes (limit {row['limit']})" for row in payload["oversized_assets"]])
    add_block("Style Scars", [f"- `{row['page']}` -> {row['issue']}" for row in payload["style_scars"]])
    add_block("Grammar Scars", [f"- `{row['page']}` -> {row['issue']}" for row in payload["grammar_scars"]])
    add_block("SEO Issues", [f"- `{row['page']}` -> {row['issue']}" for row in payload["seo_issues"]])
    add_block("Duplicate Titles", [f"- {row['title']} x{row['count']}" for row in payload["duplicate_titles"]])
    add_block("Duplicate Descriptions", [f"- {row['description']} x{row['count']}" for row in payload["duplicate_descriptions"]])
    add_block("JSON-LD Issues", [f"- `{row['page']}` -> {row['issue']}" for row in payload["json_ld_issues"]])
    add_block("Sitemap Issues", [f"- `{row['page']}` -> {row['issue']}" for row in payload["sitemap_issues"]])
    add_block("Robots/Noindex Issues", [f"- `{row['page']}` -> {row['issue']}" for row in payload["robots_issues"]])
    (QUALITY_DIR / "site-audit.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    payload = audit()
    write_report(payload)
    summary = payload["summary"]
    print(
        "Site audit:"
        f" pages={summary['pages_scanned']}"
        f" broken_links={summary['broken_links']}"
        f" duplicate_ids={summary['duplicate_ids']}"
        f" prompt_number_issues={summary['prompt_number_issues']}"
        f" orphans={summary['orphan_pages']}"
        f" oversized_assets={summary['oversized_assets']}"
        f" style_scars={summary['style_scars']}"
        f" grammar_scars={summary['grammar_scars']}"
        f" seo_issues={summary['seo_issues']}"
        f" json_ld_issues={summary['json_ld_issues']}"
        f" sitemap_issues={summary['sitemap_issues']}"
        f" robots_issues={summary['robots_issues']}"
    )


if __name__ == "__main__":
    main()
