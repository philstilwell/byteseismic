# Editorial revision requirements

Effective September 6, 2026, at the curator's request. These requirements supersede the earlier repeated polish approach. The new pass starts at the beginning of the authoritative queue; earlier passes do not count toward its completion.

## Original pages govern the revision

For every page, locate and read the complete original source before editing. Use the original WordPress post in `.cache/byteseismic-posts-with-content.json`, matching its URL, title, and prompt sequence. Retrieve the original published source or earliest reliable repository version if the cache is insufficient. Record the source used. A previously reconstructed or polished page alone is not an adequate original-source baseline. If no reliable original can be established, report the affected page as blocked and leave the batch incomplete.

Follow the original order and structure as closely as possible: prompts, responses, follow-up questions, curator corrections, dialogue turns, lists, tables, and other requested forms. Include the full original prompts verbatim and in their original order. Keep each revised response directly associated with its prompt. Respect requested counts, examples, comparisons, and formats, and explain any necessary limitation honestly. Preserve the curator's stances, tone, and conceptual priorities.

Read each prompt and its entire response together. Improve the actual response where it needs clarity, coherence, examples, transitions, explanation, or correction. Handle each page according to its particular argument and conversational development. Do not substitute a generic essay, repeated framing, stock dialogue, or a fixed one-paragraph addition for substantive revision. Retain effective original material. Add expansions only when they help answer the relevant prompt and fit the page's existing progression.

## Daily batch and completion

Read `quality/editorial-audit-tracker.json` first and work only on `currentBatch.pages`, normally 50 pages. Continue from the saved cursor on subsequent days; the reset is a one-time change, not a daily instruction to restart.

Check each revised page against its original source for structure, prompt completeness and order, response relevance, curator exchanges, and page-specific treatment. Automated structural scores do not establish editorial quality. Keep a per-page report identifying the original source, substantive changes, preservation checks, and remaining concerns.

Build and verify in an isolated directory. The archive builder runs a real build even with `--help`; never invoke it in the dirty main checkout. Ensure subsequent builds preserve reviewed content. Preserve unrelated working changes and stage only the batch's authorized files.

Only after every page in the batch has been meaningfully revised or explicitly reviewed and retained with a page-specific reason, and verified, run `python3 scripts/advance_editorial_audit_tracker.py --complete-current`. Confirm that its completed paths exactly match the batch just handled. An incomplete or blocked batch must retain its cursor.

Commit and push the completed work. Provide a progress report every run, including the pages reviewed, specific improvements, fidelity to original prompts and structure, verification results, commit/push status, completed and remaining page counts for this new pass, the next batch, and unresolved follow-up. Report partial work honestly.
