#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
QUALITY_DIR = ROOT / "quality"
QUALITY_DIR.mkdir(exist_ok=True)

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
    duplicate_ids: list[dict] = []
    repeated_headings: list[dict] = []
    prompt_number_issues: list[dict] = []

    for path in pages:
        soup = BeautifulSoup(path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
        page = site_path(path)
        soups[page] = soup
        ids_by_path[page] = extract_ids(soup)

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
    )


if __name__ == "__main__":
    main()
