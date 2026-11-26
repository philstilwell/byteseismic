# Editorial revision requirements

Effective September 6, 2026, at the curator's request. These requirements supersede the earlier repeated polish approach. The new pass starts at the beginning of the authoritative queue; earlier passes do not count toward its completion.

## Original pages govern the revision

For every page, locate and read the complete original source before editing. Use the original WordPress post in `.cache/byteseismic-posts-with-content.json`, matching its URL, title, and prompt sequence. Retrieve the original published source or earliest reliable repository version if the cache is insufficient. Record the source used. A previously reconstructed or polished page alone is not an adequate original-source baseline. If no reliable original can be established, report the affected page as blocked and leave the batch incomplete.

Follow the original order and structure as closely as possible: prompts, responses, follow-up questions, curator corrections, dialogue turns, lists, tables, and other requested forms. Include the full original prompts verbatim and in their original order. Keep each revised response directly associated with its prompt. Respect requested counts, examples, comparisons, and formats, and explain any necessary limitation honestly. Preserve the curator's stances, tone, and conceptual priorities.

Read each prompt and its entire response together. Improve the actual response where it needs clarity, coherence, examples, transitions, explanation, or correction. Handle each page according to its particular argument and conversational development. Do not substitute a generic essay, repeated framing, stock dialogue, or a fixed one-paragraph addition for substantive revision. Retain effective original material. Add expansions only when they help answer the relevant prompt and fit the page's existing progression.

## Daily batch and completion

Read `quality/editorial-audit-tracker.json` first. Effective November 21, 2026, review 20 previously unreviewed pages per calendar day in America/New_York. Count pages fully reviewed and verified earlier that day toward the total; source recovery and automated checks alone do not count. Work sequentially within `currentBatch.pages`, normally 50 pages. The daily target does not reset or resize the saved tracker batch. Maintain per-page partial-batch progress. If a day finishes a batch, verify it completely and advance under the conditions below before continuing the newly current batch toward the daily total. If fewer than 20 pages remain in cycle 8, finish only those remaining pages and follow the endpoint instructions. Continue from the saved cursor; never restart the queue. Report any genuine blocker and exact shortfall honestly; do not routinely stop after one page.

Check each revised page against its original source for structure, prompt completeness and order, response relevance, curator exchanges, and page-specific treatment. Automated structural scores do not establish editorial quality. Keep a per-page report identifying the original source, substantive changes, preservation checks, and remaining concerns.

Build and verify in an isolated directory. The archive builder runs a real build even with `--help`; never invoke it in the dirty main checkout. Ensure subsequent builds preserve reviewed content. Preserve unrelated working changes and stage only the batch's authorized files.

Only after every page in the batch has been meaningfully revised or explicitly reviewed and retained with a page-specific reason, and verified, run `python3 scripts/advance_editorial_audit_tracker.py --complete-current`. Confirm that its completed paths exactly match the batch just handled. An incomplete or blocked batch must retain its cursor.

Commit and push the completed work. Provide a progress report every run, including the pages reviewed, specific improvements, fidelity to original prompts and structure, verification results, commit/push status, completed and remaining page counts for this new pass, the next batch, and unresolved follow-up. Report partial work honestly.

## Persistence and completion gate — November 24, 2026

The daily target is a completion requirement, not a time-boxed attempt. Do not stop at inspection, an inventory, preliminary findings, or a report-only commit while authorized editorial work remains possible. Continue until the daily target is fully source-read, individually revised or justified as retained, fidelity-verified, isolated-build-verified, committed and successfully pushed, or the authorized cycle endpoint is reached.

Read large sources in bounded, numbered chunks and save a coverage record. If output is truncated, immediately reread the omitted range in smaller chunks. Truncation, long pages, elapsed time, an inconvenient working tree, lack of delegation, and context compaction are not blockers. Preserve exact per-page progress and resume after compaction in the same task. Give concise progress updates without asking the user to say continue. Resolve routine tool failures through available remedies and fallbacks.

Before a final response, check the daily total, full verification, commit and remote push. If the target is unmet and no demonstrated external blocker remains, continue working. A genuine blocker report must identify the exact failing operation and evidence, attempted remedies, affected pages and shortfall. Never invent a blocker or relax original fidelity, editorial depth, or batch-advancement requirements to claim completion.

## Executable daily assignment and publication gate — November 26, 2026

The existing prose persistence rule was not enough: subsequent runs still stopped after one or two pages without an external blocker. Each run must now use a frozen daily assignment and the executable gate in `scripts/editorial_daily_gate.py`.

1. Read the saved progress and memory. Run `python3 scripts/editorial_daily_gate.py plan --date YYYY-MM-DD`, using the assignment date in America/New_York. Resume an interrupted assignment using its existing date, even across midnight. The saved `quality/editorial-runs/YYYY-MM-DD.json` selects twenty distinct pages, including earlier reviews that day, or the actual smaller remainder of cycle 8. Never shorten or recreate it to pass the check.
2. Work through every assigned page in order. Save exact reading coverage, individual editorial decisions, source/edits, dated fidelity verification, and the next recovery step. Checkpointing does not end the run: immediately continue with the next unfinished page. Do not ask the user to say continue or defer the work to a replacement automation.
3. Build the exact final pages in an isolated directory and preserve all reviewed page hashes. Save `quality/original-source-revisions/batch-verification-YYYY-MM-DD.json` with `build.isolated`, the real `build.log`, and `build.reviewedPageHashes`. Per-page verification must match the final file, source snapshot and build hash, with source coverage and actual fidelity results. Automated checks cannot establish editorial quality; complete the original reading and substantive review first.
4. Run `python3 scripts/editorial_daily_gate.py check --date YYYY-MM-DD --phase ready`. Resolve every failure. READY only permits moving to commit and push; it does not permit a final completion response.
5. Commit and push only authorized files, including the assignment and all its evidence. Run `python3 scripts/editorial_daily_gate.py check --date YYYY-MM-DD --phase published`. End successfully only after COMPLETE/exit zero confirms all assigned evidence matches, required files are committed, and local HEAD equals remote `origin/main`. Do not weaken the checker to claim completion. Preserve unrelated working changes.

A genuine external blocker still requires the exact failure, attempted remedies, affected pages, shortfall and saved recovery step. Mark that result incomplete. The checker verifies evidence and publication; it is not a scheduler restart mechanism and cannot override application shutdown or service limits. If an interrupted assignment exists, the next available run resumes it before starting a new assignment. At the already-published cycle endpoint, follow the existing pause instructions instead of creating an empty new assignment.

## Runtime continuation controller — November 26, 2026

The executable gate alone cannot keep an agent working. The trusted project hooks in `.codex/hooks.json` now invoke `scripts/editorial_run_controller.py` independently of the model:

- `UserPromptSubmit` recognizes the exact automation marker, binds the chat to a saved assignment date, and creates/reopens its plan before the model starts. Other project conversations remain unaffected.
- `Stop` also recognizes desktop scheduler launches delivered as tool messages: it reads the runtime-provided transcript and checks the matching session, project, automation source, named scheduler tool output, exact automation ID and marker. This closes the gap where no `UserPromptSubmit` event occurs. It then independently runs the published completion check. Failure returns Codex’s supported `decision: block` with the outstanding work, causing an automatic continuation prompt. This applies to every premature finish, even when `stop_hook_active` is already true. There is no one-retry escape or successful partial-completion path.
- Successful verification and remote-push confirmation release the run and mark its controller state complete. State lives in the automation’s `controller-sessions` directory, separate from editorial artifacts.
- `Interrupt` suspends continuation when the user manually stops work. Pausing the existing automation also disables continuation. Neither mechanism is overridden.

The controller is active runtime behavior, not a request for the model to remember a check. Its hooks must remain enabled and trusted for the configured project path. The installed hooks were checked through Codex’s hooks/list API. A local Codex integration test with a simulated model verified two automatic continuations after deliberate early finishes, followed by termination only after the simulated publication gate passed; it used no paid model calls. Ordinary unit tests cover repeated stops, failed publication, midnight/restart recovery, unrelated chats and manual interruption.

This controller handles attempted final responses while Codex is running. It cannot run while the application is shut down or force an unavailable model service to respond. A subsequent scheduled run binds to the oldest saved unfinished assignment. It does not install an independent operating-system restart service or create a replacement automation. The schedule, source-fidelity rules and fifty-page batch advancement requirements remain unchanged.

## Recorded source resolutions — September 21, 2026

The curator explicitly approved the earliest repository editions of **Al-Ghazali**, **Anselm of Canterbury**, and **Arthur Schopenhauer** as **site-native baselines**, preserving each page’s four prompts. This exception applies only to `/philosophers/al-ghazali/`, `/philosophers/anselm-of-canterbury/`, and `/philosophers/arthur-schopenhauer/`. These baselines are editorial/reconstructed site pages, not original WordPress posts. Label their provenance accurately; do not infer an original WordPress conversation or attribute composite responses to a particular model.

Exact first-addition commits, immutable snapshot paths, hashes, twelve prompt texts and approval evidence are recorded in `quality/original-source-revisions/site-native-baselines-2026-09-21.json`. Read each complete baseline and current page before revising. Preserve the four prompts verbatim and in order, response placement and substantive structure, while replacing weak exposition with page-specific reasoning. The ordinary factual, structural and build verification requirements still apply. Approval of a baseline is not completion of its editorial review. All other pages remain subject to the original-source rule above.

The complete supporting publisher transcript for **Jeremy Sherman on Emergence** has been recovered from two independent Internet Archive captures with identical transcript text. Use `quality/original-source-revisions/jeremy-sherman-transcript-recovery-2026-09-21.json` for archive URLs, checksums and local research-cache paths. Read the complete transcript alongside original WordPress post 9786; do not keep treating the publisher’s live HTTP 503 error as a source-availability blocker. The transcript is labeled rough/unrevised by its publisher. Preserve all seven WordPress prompts, the original image response and the curator’s exact bonus-image comment. Transcript recovery does not complete this page’s editorial review.

## Additional approved site-native baselines — September 30, 2026

The curator explicitly stated: “I Approve the 31 recorded site-native baselines for full editorial review.” This extends the site-native exception to exactly the thirty-one previously source-blocked pages recorded in `quality/original-source-revisions/current-batch-source-inventory-2026-09-23.json`, all within cycle 8’s current batch at indexes 50–99. The September 21 three-page approval remains valid.

Use the exact first-repository snapshots, commits, checksums, and four prompt texts recorded in `quality/original-source-revisions/site-native-baselines-2026-09-30.json`. Label these pages as site-native editorial/reconstructed profiles, not original WordPress conversations; do not invent model attribution. Preserve each page’s four prompts verbatim and in order, response positions, lists and follow-up questions. Read the entire approved baseline and current edition before substantive, page-specific revision. Approval only resolves source eligibility: it does not complete review or permit advancing an unfinished batch. All ordinary factual, structural and isolated-build verification requirements still apply.

## Finite Agency discretionary rewrite — October 7, 2026

The curator explicitly stated: “I approve a rewrite of 'Finite Agency' at your discetion.” This authorizes a discretionary rewrite of exactly `/ethics/finite-agency-moral-demand-and-happiness/` and resolves its previously recorded source blocker. The exact first-repository snapshot is retained as the preservation baseline in `quality/original-source-revisions/site-native-baselines-2026-10-07.json`. It is a site-native editorial/reconstructed branch cluster, not a WordPress original or an attributable model conversation. Preserve its four prompts verbatim and in order and retain the five follow-up questions. This is a one-page addition to the prior 34 approved baselines, not a general exception. Its review and verification are recorded in `quality/editorial-audit-2026-10-07-finite-agency.json`; the current 50-page batch must still remain at its saved cursor until all pages have been reviewed.

## Project endpoint — November 9, 2026

The curator authorized stopping after the initial original-preserving pass, which is cycle 8 (restarted September 6, 2026), currently covering 346 queued pages. Continue the saved batch and remaining pages; do not pause before completion or count source recovery alone as review.

`protocol.stopAfterCurrentCycle` keeps the final completed paths and cycle number, leaves the next batch empty, and prevents automatic rollover or restart. On the final batch, perform the ordinary full review, isolated-build verification and exact completed-path checks, then commit and push all authorized final work. Confirm the push before using the Codex automation tool to set `byteseismic-daily-editorial-audit` to `PAUSED`, preserving its other settings. Issue a final completion report with totals, verification, commit/push status and any limitations. If the final push is blocked, report it and continue only completion work on subsequent runs; never begin another review cycle. If a later run finds the pass already complete and pushed, pause the automation without editing more pages.

Maintenance is a separate future decision. Do not start maintenance, reset the queue, create a replacement recurring task or reactivate this automation without explicit user authorization.

Live scheduler verification on November 26, 2026: the first real trial exposed the tool-message activation gap. After repair, the actual scheduled Astra High run emitted an early final response, received one native HookPrompt without a human continuation, committed/pushed the verification record as `aa18b4819`, and passed the twenty-page publication gate. The normal daily 09:00 schedule was restored. Evidence: `quality/editorial-controller-live-verification-2026-11-26.json`.
