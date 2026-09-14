#!/usr/bin/env python3
"""Fail when known curator-pushback exchanges disappear from the rebuilt site."""

from __future__ import annotations

import html
import json
from pathlib import Path

from bs4 import BeautifulSoup

import build_archive
import revise_source_conversations


ROOT = Path(__file__).resolve().parents[1]
SOURCE_CACHE = ROOT / ".cache" / "byteseismic-posts-with-content.json"

EXPECTED = {
    "categories-of-questions": (3, "appreciate that realignment"),
    "the-primacy-of-induction": (2, "subsumed by induction"),
    "the-value-selection-hypothesis": (2, "without this circularity"),
    "torturing-babies": (1, "responses from 3 AIs"),
    "non-scientific-ways-of-knowing": (3, "Internal coherence and consistency"),
    "assisted-suicide": (1, "Address the following two issues"),
    "testing-prayer": (3, "does not remove the choice whether to worship"),
    "peaceful-revolutions": (1, "continue to push back"),
    "recommendations-vs-moral-claims": (5, "previous response was circular"),
    "compassion-vs-moral-systems": (2, "rational compassion"),
    "belief-evidence-graphic": (5, "There is no “whim”"),
    "reasoned-probabilities-and-decisions": (4, "observable predictive strength"),
    "is-logic-acquired-inductively": (2, "inductive substrate"),
    "what-is-truth": (1, "provisional status of our beliefs"),
    "what-is-knowledge": (6, "conflating distinct concepts"),
    "extraordinary-claims": (2, "Sagan Standard"),
    "minimum-wage": (2, "take any job I wish"),
}


def page_for_slug(slug: str) -> Path | None:
    matches = list(ROOT.glob(f"*/{slug}/index.html"))
    return matches[0] if len(matches) == 1 else None


def verify_original_edition(slug: str, post: dict, page_path: Path) -> bool:
    """Check source-positioned exchanges instead of requiring a duplicate appendix.

    An editorial marker is not an exemption: require the exact cached original,
    its edit map, and the full source-preservation check on the actual built page.
    Return False only for pages still using the older recovered-section layout.
    """
    rendered = page_path.read_text()
    if 'EDITORIALLY MAINTAINED: original-preserving cycle 8;' not in rendered:
        return False
    data = ROOT / 'quality/original-source-revisions'
    config = json.loads((data / f'{slug}-edits.json').read_text())
    assert config['wordpressId'] == post['ID'], 'WordPress ID mismatch'
    assert config['sourceUrl'] == post['URL'], 'WordPress URL mismatch'
    assert config['pageFile'] == page_path.relative_to(ROOT).as_posix(), 'Page path mismatch'
    assert (data / config['snapshot']).read_bytes() == post['content'].encode(), 'Cached original mismatch'
    revise_source_conversations.verify(config, rendered)
    return True


def main() -> int:
    posts = {
        post["slug"]: post
        for post in json.loads(SOURCE_CACHE.read_text())
    }
    failures: list[str] = []
    recovered_pages = 0

    for slug, post in posts.items():
        exchanges = build_archive.extract_dialectical_exchanges(
            post.get("content", ""),
            html.unescape(post.get("title", "")),
        )
        if not exchanges:
            continue
        recovered_pages += 1
        page_path = page_for_slug(slug)
        if page_path is None:
            failures.append(f"{slug}: rebuilt page was not found uniquely")
            continue
        soup = BeautifulSoup(page_path.read_text(), "html.parser")
        try:
            if verify_original_edition(slug, post, page_path):
                continue
        except (AssertionError, KeyError, ValueError, OSError, AttributeError) as error:
            failures.append(f"{slug}: original-edition preservation failed: {error}")
            continue
        section = soup.select_one("#dialectical-turn")
        if section is None:
            failures.append(f"{slug}: rebuilt page has no recovered-exchange section")
            continue
        expected_turns = sum(
            1 + len(exchange.get("responses", []))
            for exchange in exchanges
        )
        actual_turns = len(section.select(".dialogue-turn"))
        if actual_turns < expected_turns:
            failures.append(
                f"{slug}: rebuilt page has {actual_turns} exchange turns; expected {expected_turns}"
            )

    for slug, (minimum, needle) in EXPECTED.items():
        post = posts.get(slug)
        if not post:
            failures.append(f"{slug}: source post is missing from the local cache")
            continue

        exchanges = build_archive.extract_dialectical_exchanges(
            post.get("content", ""),
            html.unescape(post.get("title", "")),
        )
        if len(exchanges) < minimum:
            failures.append(
                f"{slug}: recovered {len(exchanges)} exchanges; expected at least {minimum}"
            )

        page_path = page_for_slug(slug)
        if page_path is None:
            failures.append(f"{slug}: rebuilt page was not found uniquely")
            continue
        soup = BeautifulSoup(page_path.read_text(), "html.parser")
        section = soup.select_one("#dialectical-turn")
        if section is None:
            failures.append(f"{slug}: rebuilt page has no recovered-exchange section")
            continue
        section_text = build_archive.clean_text(section.get_text(" ", strip=True))
        if needle.casefold() not in section_text.casefold():
            failures.append(f"{slug}: rebuilt exchange is missing the phrase {needle!r}")

    if failures:
        print("Dialectical preservation check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"Dialectical preservation check passed for all {recovered_pages} recovered pages, "
        f"including {len(EXPECTED)} high-risk regression cases."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
