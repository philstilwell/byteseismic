# Editorial blocker reconciliation — September 21, 2026

The repository is usable again, the complete Sherman transcript has been recovered, and the curator has approved explicit site-native baselines for the three profiles without WordPress originals. **All four source-selection blockers are resolved.** Their substantive editorial reviews are still pending; no page has been marked complete and the tracker has not advanced.

## Repository and working changes

Restored the configured `/Users/philstilwell/Documents/BYTESEISMIC` path with a directory link to the existing repository under `Documents - Phil’s 2024 MacBook Pro`. Codex now recognizes the saved project as a Git repository, and execution from its configured directory succeeds.

Recovered the main repository history from the existing GitHub remote and synchronized local `main` with report commit `ec062b6ca580427fd01af4a1aefe8e19d20e6fe9` before making this reconciliation commit. All **480 inherited modified files** were hashed before and after synchronization and remain byte-identical. The staging area was empty before staging this task’s files. Ordinary fetch and push dry-run checks succeed.

Original Git objects remain in `.git/objects-before-reconcile-20260921`, referenced as a fallback by the restored object store. Some private Codex checkpoint objects remain cloud-only; none of their references or files were discarded. The local `fetch.hideRefs=refs/codex/` setting prevents those private checkpoints from blocking network-fetch checks. Automatic Git cleanup is disabled while this preserved fallback remains needed. Recovery notes, the prior index/configuration and file hashes are retained in `.git/reconciliation-20260921`. This is a retained recovery backup, not temporary build output.

## Sherman transcript recovered

Recovered the publisher’s transcript from Internet Archive captures dated April 22, 2024 and June 22, 2025. Both have the same **165 transcript paragraphs**, including the opening introduction and final thanks, and the same normalized text hash. The live publisher still serves its unavailable-site error, but that no longer prevents source review.

The publisher labels the transcript rough and unrevised. Full copies are stored only in the ignored local research cache; they are not republished in this commit. [The source record](original-source-revisions/jeremy-sherman-transcript-recovery-2026-09-21.json) contains archive URLs, content hashes and cache locations. The next editorial review must read this transcript together with WordPress post 9786, then preserve all seven original page prompts, the original image and curator comment, the ten-item quiz and twenty discussion questions.

## Approved site-native baselines

The curator explicitly selected **“Use labeled site-native baselines (Recommended)”** for these three profiles. Their exact first-added repository editions are now saved with provenance and hashes:

| Page | First-added commit | Source kind | Preserved prompts |
| --- | --- | --- | ---: |
| Al-Ghazali | `c848a72c8e71d73379aa3edf5e75d01c40dd1f1e` | Site-native editorial orientation | 4 |
| Anselm of Canterbury | `345af16a41eca1c30e18e8fe0df89b4a5eeb0a5c` | Site-native reconstructed composite profile | 4 |
| Arthur Schopenhauer | `c848a72c8e71d73379aa3edf5e75d01c40dd1f1e` | Site-native editorial orientation | 4 |

All twelve prompts match the current pages. These are explicitly labeled site-native sources, **not WordPress originals**. The exception is limited to these three paths. It does not authorize substituting later reconstructed pages for originals elsewhere. The [baseline record](original-source-revisions/site-native-baselines-2026-09-21.json) includes the curator’s approval, exact prompt text, immutable snapshots and current-page comparison.

Additional local WordPress exports from February 8, March 1 and March 26, 2024 contained 54, 280 and 255 items respectively, with none of the three profile titles. Those early exports alone do not establish that a later original never existed; the repository’s first-addition provenance and earlier cache/live searches support the approved treatment.

## Protocol and automation

Updated `quality/editorial-revision-protocol.md` and the existing automation prompt with the bounded exception and the recovered transcript’s source record. Verified the saved automation remains active with the same project, daily schedule, **gpt-6-astra / high** settings and local execution. No duplicate automation was created.

## Verification and progress

The full builder completed in an isolated copy of committed content: **723 content pages generated/updated**, **840 pages audited with zero reported issues**, and **all 46 previously reviewed editions preserved byte-for-byte**. All **39 recovered-conversation checks**, including **17 high-risk cases**, passed. The first attempt reached an artificial 240-second limit; a clean rerun completed successfully in approximately 248 seconds. The main working checkout was never built. Verification evidence is recorded in `quality/original-source-revisions/reconciliation-verification-2026-09-21.json`.

The accompanying JSON report records a status for each of the fifty current-batch pages. The source-ready next work is **Jeremy Sherman on Emergence, Al-Ghazali, Anselm of Canterbury and Arthur Schopenhauer**. Each still needs full reading, page-specific revision and verification. Source recovery and baseline approval do not count as editorial completion.

- Current batch: **46 reviewed, 4 ready for substantive review, 0 missing-source blockers**.
- Restarted pass: **46/346 reviewed; 300 not yet fully reviewed**.
- Batch-level tracker: **0 completed / 346 remaining**, cycle 8, positions 0–49 unchanged.
- No later batch activated; neither tracker file changed and the completion command was not run.
- No source-page text was edited in this reconciliation. No paid generation, image creation, voice production or external code installation was used.

## Delivery

Only this report, its JSON companion, source provenance and exact approved baseline snapshots, the revision protocol and build-verification evidence are included in the reconciliation commit. The final commit and remote verification are recorded in automation memory. Temporary build/recovery staging directories are removed after verification; the original Git recovery backup and local research cache are deliberately retained.
