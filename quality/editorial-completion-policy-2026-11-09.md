# Original-preserving project endpoint

On November 9, 2026, the curator requested stopping after the initial original-preserving cycle and considering maintenance separately. This is cycle 8, restarted September 6, with 346 queued pages.

Set protocol.stopAfterCurrentCycle in the saved tracker. Completion now retains the cycle and all completed paths, produces an empty current batch and no future-cycle preview, and makes repeated completion calls harmless. Rebuilds retain the policy and completed state. Restart is rejected while this policy is enabled. Existing recurring behavior remains available when the flag is absent.

Updated the existing daily automation through the Codex automation tool. It remains active with its existing schedule, model, reasoning setting and project. Its instructions now require pausing itself after the final verified batch is committed and successfully pushed, followed by a final completion report. A blocked final push permits only finalization work, not another review cycle. Maintenance requires separate user authorization.

Verification: five regression tests passed (final completion, repeated completion, rebuild persistence, unfinished progression, restart restriction and legacy rollover are covered across five tests). An additional in-memory simulation completed the real saved queue at 346/346 in cycle 8 and rebuilt the tracker from the committed quality report without reopening the queue. The live tracker cursor, batch and counts were not advanced; only protocol fields changed. Rebuilding refreshes score-related page metadata, so the active-batch comparison checks exact path order rather than stale score records. All 476 inherited modifications were hash-verified unchanged. No website build or page edits were needed for this scheduling/tracker change.

Progress remains 153 substantively reviewed, 193 pending; the whole-batch tracker remains 150 completed and 196 remaining. The current batch has 3 reviewed and 47 pending. Commit/push outcome is recorded in automation memory.
