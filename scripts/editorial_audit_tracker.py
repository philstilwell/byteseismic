#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


DEFAULT_BATCH_SIZE = 50
HISTORY_LIMIT = 120
TRACKER_JSON_NAME = "editorial-audit-tracker.json"
TRACKER_MD_NAME = "editorial-audit-tracker.md"


def _safe_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def _priority_band(page: dict) -> str:
    if page["needsReviewCount"] or page["editorialIssues"]:
        return "review"
    if page["needsGapFillCount"]:
        return "gap-fill"
    if page["polishOpportunityCount"]:
        return "polish"
    return "maintenance"


def _priority_rank(page: dict) -> tuple:
    band_rank = {
        "review": 0,
        "gap-fill": 1,
        "polish": 2,
        "maintenance": 3,
    }
    return (
        band_rank[page["priorityBand"]],
        0 if page["editorialIssues"] else 1,
        page["worstScore"],
        -page["needsReviewCount"],
        -page["needsGapFillCount"],
        -page["polishOpportunityCount"],
        page["sectionName"].lower(),
        page["pageTitle"].lower(),
        page["pagePath"],
    )


def _compact_focus_section(section: dict) -> dict:
    return {
        "anchor": section["anchor"],
        "url": section["url"],
        "heading": section["heading"],
        "score": section["score"],
        "level": section["level"],
        "needsReview": section["needsReview"],
        "needsGapFill": section["needsGapFill"],
        "polishOpportunity": section["polishOpportunity"],
        "editorialIssues": list(section["editorialIssues"]),
    }


def _compact_page(page: dict) -> dict:
    return {
        "queueIndex": page["queueIndex"],
        "sectionName": page["sectionName"],
        "pageTitle": page["pageTitle"],
        "pagePath": page["pagePath"],
        "priorityBand": page["priorityBand"],
        "worstScore": page["worstScore"],
        "averageScore": page["averageScore"],
        "totalPromptSections": page["totalPromptSections"],
        "needsReviewCount": page["needsReviewCount"],
        "needsGapFillCount": page["needsGapFillCount"],
        "polishOpportunityCount": page["polishOpportunityCount"],
        "editorialIssues": list(page["editorialIssues"]),
        "attentionSummary": list(page["attentionSummary"]),
        "focusAnchors": list(page["focusAnchors"]),
        "focusSections": [_compact_focus_section(section) for section in page["focusSections"][:6]],
    }


def _aggregate_page_records(report: dict) -> list[dict]:
    by_page: dict[str, list[dict]] = defaultdict(list)
    for record in report.get("records", []):
        by_page[record["pagePath"]].append(record)

    pages: list[dict] = []
    for page_path, records in by_page.items():
        ordered_records = sorted(records, key=lambda item: (item["score"], item["anchor"]))
        page_title = ordered_records[0]["pageTitle"]
        section_name = ordered_records[0]["sectionName"]
        needs_review_count = sum(1 for record in ordered_records if record["needsReview"])
        gap_fill_count = sum(1 for record in ordered_records if record["needsGapFill"])
        polish_count = sum(1 for record in ordered_records if record.get("polishOpportunity"))
        editorial_issues = _dedupe(
            [issue for record in ordered_records for issue in record.get("editorialIssues", [])]
        )
        focus_sections = [
            {
                "anchor": record["anchor"],
                "url": record["url"],
                "heading": record["heading"],
                "score": record["score"],
                "level": record["level"],
                "needsReview": record["needsReview"],
                "needsGapFill": record["needsGapFill"],
                "polishOpportunity": record.get("polishOpportunity", False),
                "editorialIssues": list(record.get("editorialIssues", [])),
            }
            for record in ordered_records
            if (
                record["needsReview"]
                or record["needsGapFill"]
                or record.get("polishOpportunity")
                or record.get("editorialIssues")
            )
        ]
        attention_summary: list[str] = []
        if needs_review_count:
            attention_summary.append(f"{needs_review_count} prompt sections need review")
        if gap_fill_count:
            attention_summary.append(f"{gap_fill_count} prompt sections need gap fill")
        if polish_count:
            attention_summary.append(f"{polish_count} prompt sections are polish opportunities")
        if editorial_issues:
            attention_summary.append("editorial issues: " + ", ".join(editorial_issues[:4]))

        page = {
            "sectionName": section_name,
            "pageTitle": page_title,
            "pagePath": page_path,
            "totalPromptSections": len(ordered_records),
            "worstScore": min(record["score"] for record in ordered_records),
            "averageScore": round(
                sum(record["score"] for record in ordered_records) / max(len(ordered_records), 1), 1
            ),
            "needsReviewCount": needs_review_count,
            "needsGapFillCount": gap_fill_count,
            "polishOpportunityCount": polish_count,
            "editorialIssues": editorial_issues,
            "focusAnchors": [section["anchor"] for section in focus_sections],
            "focusSections": focus_sections,
            "attentionSummary": attention_summary or ["maintenance pass"],
        }
        page["priorityBand"] = _priority_band(page)
        pages.append(page)

    pages.sort(key=_priority_rank)
    for index, page in enumerate(pages, start=1):
        page["queueIndex"] = index
    return pages


def _resolve_cursor(existing_tracker: dict | None, pages: list[dict]) -> dict:
    total_pages = len(pages)
    if total_pages == 0:
        return {
            "cycle": 1,
            "currentPageIndex": 0,
            "nextPagePath": "",
            "nextPageTitle": "",
            "lastAdvancedAt": "",
            "lastCompletedBatch": {},
        }

    existing_tracker = existing_tracker or {}
    existing_cursor = existing_tracker.get("cursor", {}) if isinstance(existing_tracker, dict) else {}
    page_paths = [page["pagePath"] for page in pages]
    completed_paths = _dedupe(
        [
            path
            for path in existing_cursor.get("completedPagePathsInCurrentCycle", [])
            if path in page_paths
        ]
    )
    stored_path = existing_cursor.get("nextPagePath", "")

    current_batch_pages = (
        existing_tracker.get("currentBatch", {}).get("pages", [])
        if isinstance(existing_tracker, dict)
        else []
    )
    current_batch_paths = [page.get("pagePath", "") for page in current_batch_pages]
    remaining_paths = [path for path in page_paths if path not in set(completed_paths)]
    next_path = next(
        (
            path
            for path in current_batch_paths
            if path in remaining_paths
        ),
        stored_path if stored_path in remaining_paths else remaining_paths[0],
    )

    cycle = max(_safe_int(existing_cursor.get("cycle", 1), 1), 1)
    current_page = pages[page_paths.index(next_path)]
    return {
        "cycle": cycle,
        "currentPageIndex": len(completed_paths),
        "nextPagePath": current_page["pagePath"],
        "nextPageTitle": current_page["pageTitle"],
        "lastAdvancedAt": existing_cursor.get("lastAdvancedAt", ""),
        "lastCompletedBatch": existing_cursor.get("lastCompletedBatch", {}),
        "completedPagePathsInCurrentCycle": completed_paths,
    }


def _preserve_existing_current_batch(existing_tracker: dict | None, pages: list[dict], cursor: dict, batch_size: int) -> dict:
    completed_paths = set(cursor.get("completedPagePathsInCurrentCycle", []))
    if not isinstance(existing_tracker, dict):
        return _batch_from_remaining(pages, completed_paths, batch_size, cursor["cycle"])

    existing_batch = existing_tracker.get("currentBatch", {})
    existing_pages = existing_batch.get("pages", []) if isinstance(existing_batch, dict) else []
    if not existing_pages:
        return _batch_from_remaining(pages, completed_paths, batch_size, cursor["cycle"])

    page_lookup = {page["pagePath"]: page for page in pages}
    preserved = [
        page_lookup[path]
        for path in [page.get("pagePath", "") for page in existing_pages]
        if path in page_lookup and path not in completed_paths
    ]
    if not preserved:
        return _batch_from_remaining(pages, completed_paths, batch_size, cursor["cycle"])

    preserved_paths = {page["pagePath"] for page in preserved}
    for page in pages:
        if len(preserved) >= batch_size:
            break
        if page["pagePath"] in completed_paths or page["pagePath"] in preserved_paths:
            continue
        preserved.append(page)
        preserved_paths.add(page["pagePath"])

    start_index = len(completed_paths)

    return {
        "cycle": _safe_int(existing_batch.get("cycle", cursor["cycle"]), cursor["cycle"]),
        "startIndex": start_index,
        "endIndexExclusive": start_index + len(preserved),
        "pageCount": len(preserved),
        "wrapsToNextCycle": start_index + len(preserved) >= len(pages),
        "priorityCounts": dict(Counter(page["priorityBand"] for page in preserved)),
        "pages": [_compact_page(page) for page in preserved],
    }


def _batch_from_remaining(
    pages: list[dict],
    completed_paths: set[str],
    batch_size: int,
    cycle: int,
) -> dict:
    remaining = [page for page in pages if page["pagePath"] not in completed_paths]
    batch_pages = remaining[:batch_size]
    start_index = len(pages) - len(remaining)
    end_index = start_index + len(batch_pages)
    return {
        "cycle": cycle,
        "startIndex": start_index,
        "endIndexExclusive": end_index,
        "pageCount": len(batch_pages),
        "wrapsToNextCycle": bool(batch_pages) and len(batch_pages) >= len(remaining),
        "priorityCounts": dict(Counter(page["priorityBand"] for page in batch_pages)),
        "pages": [_compact_page(page) for page in batch_pages],
    }


def _batch_slice(pages: list[dict], start_index: int, batch_size: int, cycle: int) -> dict:
    total_pages = len(pages)
    if total_pages == 0:
        return {
            "cycle": cycle,
            "startIndex": 0,
            "endIndexExclusive": 0,
            "pageCount": 0,
            "wrapsToNextCycle": False,
            "priorityCounts": {},
            "pages": [],
        }

    start_index = min(max(start_index, 0), total_pages - 1)
    batch_pages = pages[start_index : start_index + batch_size]
    end_index = start_index + len(batch_pages)
    return {
        "cycle": cycle,
        "startIndex": start_index,
        "endIndexExclusive": end_index,
        "pageCount": len(batch_pages),
        "wrapsToNextCycle": end_index >= total_pages,
        "priorityCounts": dict(Counter(page["priorityBand"] for page in batch_pages)),
        "pages": [_compact_page(page) for page in batch_pages],
    }


def _upcoming_batches(pages: list[dict], start_index: int, batch_size: int, cycle: int, count: int = 2) -> list[dict]:
    total_pages = len(pages)
    previews: list[dict] = []
    if total_pages == 0:
        return previews

    preview_start = start_index
    preview_cycle = cycle
    current_batch = _batch_slice(pages, preview_start, batch_size, preview_cycle)
    preview_start = current_batch["endIndexExclusive"]
    if current_batch["wrapsToNextCycle"]:
        preview_start = 0
        preview_cycle += 1

    for _ in range(count):
        if preview_start >= total_pages:
            preview_start = 0
            preview_cycle += 1
        batch = _batch_slice(pages, preview_start, batch_size, preview_cycle)
        previews.append(
            {
                "cycle": batch["cycle"],
                "startIndex": batch["startIndex"],
                "endIndexExclusive": batch["endIndexExclusive"],
                "pageCount": batch["pageCount"],
                "priorityCounts": batch["priorityCounts"],
                "pages": batch["pages"][:10],
            }
        )
        preview_start = batch["endIndexExclusive"]
        if batch["wrapsToNextCycle"]:
            preview_start = 0
            preview_cycle += 1
    return previews


def _upcoming_batches_from_remaining(
    pages: list[dict],
    completed_paths: set[str],
    current_batch_paths: set[str],
    batch_size: int,
    cycle: int,
    count: int = 2,
) -> list[dict]:
    available = [
        page
        for page in pages
        if page["pagePath"] not in completed_paths and page["pagePath"] not in current_batch_paths
    ]
    previews: list[dict] = []
    preview_cycle = cycle
    offset = 0
    completed_count = len(completed_paths) + len(current_batch_paths)

    for _ in range(count):
        if offset >= len(available):
            available = list(pages)
            offset = 0
            completed_count = 0
            preview_cycle += 1
        batch_pages = available[offset : offset + batch_size]
        if not batch_pages:
            break
        start_index = completed_count + offset
        previews.append(
            {
                "cycle": preview_cycle,
                "startIndex": start_index,
                "endIndexExclusive": start_index + len(batch_pages),
                "pageCount": len(batch_pages),
                "priorityCounts": dict(Counter(page["priorityBand"] for page in batch_pages)),
                "pages": [_compact_page(page) for page in batch_pages[:10]],
            }
        )
        offset += len(batch_pages)
    return previews


def build_editorial_audit_tracker(
    report: dict,
    *,
    existing_tracker: dict | None = None,
    batch_size: int = DEFAULT_BATCH_SIZE,
) -> dict:
    pages = _aggregate_page_records(report)
    cursor = _resolve_cursor(existing_tracker, pages)
    current_batch = _preserve_existing_current_batch(existing_tracker, pages, cursor, batch_size)
    completed_paths = set(cursor.get("completedPagePathsInCurrentCycle", []))
    current_batch_paths = {page["pagePath"] for page in current_batch.get("pages", [])}
    page_count = len(pages)
    band_counts = Counter(page["priorityBand"] for page in pages)
    history = existing_tracker.get("history", []) if isinstance(existing_tracker, dict) else []
    if not isinstance(history, list):
        history = []

    return {
        "version": 1,
        "generatedAt": date.today().isoformat(),
        "batchSize": batch_size,
        "protocol": {
            "readFirst": "quality/editorial-audit-tracker.json",
            "workCurrentBatchOnly": True,
            "advanceCommand": "python3 scripts/advance_editorial_audit_tracker.py --complete-current",
            "advanceCondition": "Advance the tracker only after the current batch has been meaningfully audited, rebuilt, and prepared for commit.",
        },
        "ordering": {
            "description": "Pages are queued deterministically by priority band, then by weakest score, then by severity counts, then alphabetically.",
            "bands": [
                "review: pages with prompt sections needing review or explicit editorial issues",
                "gap-fill: pages needing stronger examples, texture, or argumentative development",
                "polish: pages ready for calmer stylistic and pedagogical tightening",
                "maintenance: remaining pages that still deserve periodic re-reading",
            ],
        },
        "summary": {
            "trackedPages": page_count,
            "pagesByPriorityBand": dict(sorted(band_counts.items())),
            "pagesRemainingInCurrentCycle": max(page_count - len(completed_paths), 0),
            "batchSize": batch_size,
            "estimatedBatchesPerCycle": (page_count + batch_size - 1) // batch_size if page_count else 0,
        },
        "cursor": cursor,
        "currentBatch": current_batch,
        "upcomingBatches": _upcoming_batches_from_remaining(
            pages,
            completed_paths,
            current_batch_paths,
            batch_size,
            cursor["cycle"],
            count=2,
        ),
        "history": history[-HISTORY_LIMIT:],
        "pages": [_compact_page(page) for page in pages],
    }


def restart_editorial_audit_tracker(tracker: dict) -> dict:
    """Preserve prior history while starting a new editorial pass at queue zero."""
    pages = list(tracker.get("pages", []))
    if not pages:
        raise ValueError("Cannot restart an empty editorial queue")
    previous = dict(tracker.get("cursor", {}))
    cycle = max(_safe_int(previous.get("cycle", 1), 1), 1) + 1
    batch_size = _safe_int(tracker.get("batchSize", DEFAULT_BATCH_SIZE), DEFAULT_BATCH_SIZE)
    today = date.today().isoformat()
    tracker.setdefault("restarts", []).append({
        "restartedAt": today,
        "previousCycle": previous.get("cycle", 1),
        "previousCompletedPageCount": previous.get("currentPageIndex", 0),
        "newCycle": cycle,
        "reason": "User requested a fresh original-structure-preserving revision pass with page-specific responses aligned to original prompts.",
    })
    batch = _batch_from_remaining(pages, set(), batch_size, cycle)
    tracker["generatedAt"] = today
    tracker["cursor"] = {
        "cycle": cycle,
        "currentPageIndex": 0,
        "nextPagePath": pages[0]["pagePath"],
        "nextPageTitle": pages[0]["pageTitle"],
        "lastAdvancedAt": previous.get("lastAdvancedAt", ""),
        "lastCompletedBatch": previous.get("lastCompletedBatch", {}),
        "completedPagePathsInCurrentCycle": [],
    }
    tracker["summary"]["pagesRemainingInCurrentCycle"] = len(pages)
    tracker["currentBatch"] = batch
    tracker["upcomingBatches"] = _upcoming_batches_from_remaining(
        pages, set(), {page["pagePath"] for page in batch["pages"]}, batch_size, cycle,
    )
    return tracker


def advance_editorial_audit_tracker(tracker: dict, completed_at: str | None = None) -> dict:
    pages = list(tracker.get("pages", []))
    batch_size = _safe_int(tracker.get("batchSize", DEFAULT_BATCH_SIZE), DEFAULT_BATCH_SIZE)
    cursor = dict(tracker.get("cursor", {}))
    history = list(tracker.get("history", [])) if isinstance(tracker.get("history", []), list) else []

    total_pages = len(pages)
    if total_pages == 0:
        return tracker

    cycle = max(_safe_int(cursor.get("cycle", 1), 1), 1)
    page_lookup = {page["pagePath"]: page for page in pages}
    completed_before = _dedupe(
        [
            path
            for path in cursor.get("completedPagePathsInCurrentCycle", [])
            if path in page_lookup
        ]
    )
    completed_before_set = set(completed_before)
    tracked_current_pages = tracker.get("currentBatch", {}).get("pages", [])
    current_pages = [
        page_lookup[path]
        for path in [page.get("pagePath", "") for page in tracked_current_pages]
        if path in page_lookup and path not in completed_before_set
    ]
    if not current_pages:
        current_pages = [page for page in pages if page["pagePath"] not in completed_before_set][:batch_size]

    current_paths = [page["pagePath"] for page in current_pages]
    completed_after = _dedupe(completed_before + current_paths)
    wrapped = len(completed_after) >= total_pages
    next_cycle = cycle + 1 if wrapped else cycle
    completed_for_next = [] if wrapped else completed_after
    completed_for_next_set = set(completed_for_next)
    next_batch = _batch_from_remaining(pages, completed_for_next_set, batch_size, next_cycle)

    completed_at = completed_at or date.today().isoformat()
    start_index = len(completed_before)
    history.append(
        {
            "completedAt": completed_at,
            "cycle": cycle,
            "startIndex": start_index,
            "endIndexExclusive": start_index + len(current_pages),
            "pageCount": len(current_pages),
            "wrappedToNextCycle": wrapped,
            "firstPagePath": current_pages[0]["pagePath"],
            "lastPagePath": current_pages[-1]["pagePath"],
            "pagePaths": current_paths,
        }
    )
    history = history[-HISTORY_LIMIT:]

    next_page = next_batch["pages"][0]
    tracker["generatedAt"] = date.today().isoformat()
    tracker["history"] = history
    tracker["cursor"] = {
        "cycle": next_cycle,
        "currentPageIndex": len(completed_for_next),
        "nextPagePath": next_page["pagePath"],
        "nextPageTitle": next_page["pageTitle"],
        "lastAdvancedAt": completed_at,
        "lastCompletedBatch": history[-1],
        "completedPagePathsInCurrentCycle": completed_for_next,
    }
    tracker["summary"]["pagesRemainingInCurrentCycle"] = max(total_pages - len(completed_for_next), 0)
    tracker["currentBatch"] = next_batch
    tracker["upcomingBatches"] = _upcoming_batches_from_remaining(
        pages,
        completed_for_next_set,
        {page["pagePath"] for page in next_batch.get("pages", [])},
        batch_size,
        next_cycle,
        count=2,
    )
    return tracker


def render_editorial_audit_tracker_markdown(tracker: dict) -> str:
    lines = [
        "# Byteseismic Editorial Audit Tracker",
        "",
        f"Generated: {tracker.get('generatedAt', date.today().isoformat())}",
        f"Batch size: {tracker.get('batchSize', DEFAULT_BATCH_SIZE)} pages",
        f"Current cycle: {tracker.get('cursor', {}).get('cycle', 1)}",
        f"Current queue start: {tracker.get('cursor', {}).get('currentPageIndex', 0) + 1} of {tracker.get('summary', {}).get('trackedPages', 0)}",
        "",
        "## Protocol",
        "",
        f"- Read first: `{tracker.get('protocol', {}).get('readFirst', TRACKER_JSON_NAME)}`",
        f"- Advance command: `{tracker.get('protocol', {}).get('advanceCommand', '')}`",
        f"- Advance only when: {tracker.get('protocol', {}).get('advanceCondition', '')}",
        "",
        "## Ordering",
        "",
        tracker.get("ordering", {}).get("description", ""),
        "",
    ]
    for band in tracker.get("ordering", {}).get("bands", []):
        lines.append(f"- {band}")

    lines.extend([
        "",
        "## Current Batch",
        "",
        "| # | Branch | Page | Priority | Worst | Focus |",
        "| ---: | --- | --- | --- | ---: | --- |",
    ])
    for page in tracker.get("currentBatch", {}).get("pages", []):
        focus = "; ".join(page.get("attentionSummary", [])[:2])
        lines.append(
            f"| {page['queueIndex']} | {page['sectionName']} | [{page['pageTitle']}](..{page['pagePath']}) | {page['priorityBand']} | {page['worstScore']} | {focus} |"
        )

    lines.extend(["", "## Upcoming Batch Preview", ""])
    for index, batch in enumerate(tracker.get("upcomingBatches", []), start=1):
        lines.append(
            f"### Next +{index}: cycle {batch['cycle']}, queue positions {batch['startIndex'] + 1}-{batch['endIndexExclusive']}"
        )
        lines.append("")
        for page in batch.get("pages", []):
            lines.append(
                f"- `{page['priorityBand']}` {page['worstScore']} [{page['sectionName']} / {page['pageTitle']}](..{page['pagePath']})"
            )
        lines.append("")

    lines.extend([
        "## Summary",
        "",
        f"- Tracked pages: {tracker.get('summary', {}).get('trackedPages', 0)}",
        f"- Pages remaining in current cycle: {tracker.get('summary', {}).get('pagesRemainingInCurrentCycle', 0)}",
        f"- Estimated batches per cycle: {tracker.get('summary', {}).get('estimatedBatchesPerCycle', 0)}",
        "",
    ])
    for band, count in tracker.get("summary", {}).get("pagesByPriorityBand", {}).items():
        lines.append(f"- {band}: {count}")
    lines.append("")
    return "\n".join(lines)


def write_editorial_audit_tracker_files(
    root: Path,
    report: dict,
    *,
    batch_size: int = DEFAULT_BATCH_SIZE,
) -> dict:
    quality_dir = root / "quality"
    quality_dir.mkdir(exist_ok=True)
    tracker_json = quality_dir / TRACKER_JSON_NAME
    tracker_md = quality_dir / TRACKER_MD_NAME

    existing_tracker: dict | None = None
    if tracker_json.exists():
        try:
            existing_tracker = json.loads(tracker_json.read_text())
        except json.JSONDecodeError:
            existing_tracker = None

    tracker = build_editorial_audit_tracker(
        report,
        existing_tracker=existing_tracker,
        batch_size=batch_size,
    )
    tracker_json.write_text(json.dumps(tracker, indent=2, ensure_ascii=False))
    tracker_md.write_text(render_editorial_audit_tracker_markdown(tracker))
    return tracker
