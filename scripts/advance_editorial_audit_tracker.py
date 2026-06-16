#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from editorial_audit_tracker import (
    TRACKER_JSON_NAME,
    TRACKER_MD_NAME,
    advance_editorial_audit_tracker,
    render_editorial_audit_tracker_markdown,
)


ROOT = Path(__file__).resolve().parents[1]
TRACKER_JSON = ROOT / "quality" / TRACKER_JSON_NAME
TRACKER_MD = ROOT / "quality" / TRACKER_MD_NAME


def load_tracker() -> dict:
    if not TRACKER_JSON.exists():
        raise SystemExit(f"Missing tracker file: {TRACKER_JSON}")
    return json.loads(TRACKER_JSON.read_text())


def write_tracker(tracker: dict) -> None:
    TRACKER_JSON.write_text(json.dumps(tracker, indent=2, ensure_ascii=False))
    TRACKER_MD.write_text(render_editorial_audit_tracker_markdown(tracker))


def print_status(tracker: dict) -> None:
    current_batch = tracker.get("currentBatch", {})
    cursor = tracker.get("cursor", {})
    print(f"Cycle: {cursor.get('cycle', 1)}")
    print(f"Start index: {cursor.get('currentPageIndex', 0) + 1}")
    print(f"Next page: {cursor.get('nextPageTitle', '')} ({cursor.get('nextPagePath', '')})")
    print(f"Batch pages: {current_batch.get('pageCount', 0)}")
    for page in current_batch.get("pages", [])[:10]:
        print(
            f"- #{page['queueIndex']} {page['sectionName']} / {page['pageTitle']} "
            f"[{page['priorityBand']}, {page['worstScore']}]"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Advance or inspect the Byteseismic editorial audit tracker.")
    parser.add_argument(
        "--complete-current",
        action="store_true",
        help="Mark the current batch complete and advance the cursor to the next batch.",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Print the current tracker status without advancing.",
    )
    args = parser.parse_args()

    tracker = load_tracker()

    if args.complete_current:
        tracker = advance_editorial_audit_tracker(tracker)
        write_tracker(tracker)

    print_status(tracker)


if __name__ == "__main__":
    main()
