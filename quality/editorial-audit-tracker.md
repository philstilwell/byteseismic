# Byteseismic Editorial Audit Tracker

Generated: 2026-06-19
Batch size: 50 pages
Current cycle: 1
Current queue start: 297 of 528

## Protocol

- Read first: `quality/editorial-audit-tracker.json`
- Advance command: `python3 scripts/advance_editorial_audit_tracker.py --complete-current`
- Advance only when: Advance the tracker only after the current batch has been meaningfully audited, rebuilt, and prepared for commit.

## Ordering

Pages are queued deterministically by priority band, then by weakest score, then by severity counts, then alphabetically.

- review: pages with prompt sections needing review or explicit editorial issues
- gap-fill: pages needing stronger examples, texture, or argumentative development
- polish: pages ready for calmer stylistic and pedagogical tightening
- maintenance: remaining pages that still deserve periodic re-reading

## Current Batch

| # | Branch | Page | Priority | Worst | Focus |
| ---: | --- | --- | --- | ---: | --- |
| 297 | Miscellany | [Flack & Mitchell on Complexity](../miscellany/flack-mitchell-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 298 | Miscellany | [Information Theory](../miscellany/information-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 299 | Miscellany | [Sara Walker on Life’s Emergence](../miscellany/sara-walker-on-lifes-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 300 | Miscellany | [The Fantastical & Historical Truth](../miscellany/the-fantastical-historical-truth/) | polish | 100 | 4 prompt sections are polish opportunities |
| 301 | Miscellany | [Zak Stein on Complexity](../miscellany/zak-stein-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 302 | Philosophical Inquiry | [Appreciating our Insignificance](../philosophical-inquiry/appreciating-our-insignificance/) | polish | 100 | 4 prompt sections are polish opportunities |
| 303 | Philosophical Inquiry | [Charitable Engagement](../philosophical-inquiry/charitable-engagement/) | polish | 100 | 4 prompt sections are polish opportunities |
| 304 | Philosophical Inquiry | [Dangers: Anti-Intellectualism](../philosophical-inquiry/dangers-anti-intellectualism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 305 | Philosophical Inquiry | [Dangers: Gaslighting](../philosophical-inquiry/dangers-gaslighting/) | polish | 100 | 4 prompt sections are polish opportunities |
| 306 | Philosophical Inquiry | [Dangers: Limits on Doubt](../philosophical-inquiry/dangers-limits-on-doubt/) | polish | 100 | 4 prompt sections are polish opportunities |
| 307 | Philosophical Inquiry | [Dangers: Removing the Impossible](../philosophical-inquiry/dangers-removing-the-impossible/) | polish | 100 | 4 prompt sections are polish opportunities |
| 308 | Philosophy of AI | [AI Censorship Case](../philosophy-of-ai/ai-censorship-case/) | polish | 100 | 4 prompt sections are polish opportunities |
| 309 | Philosophy of AI | [AI Meta-Post — Inner Monologues](../philosophy-of-ai/ai-meta-post-inner-monologues/) | polish | 100 | 4 prompt sections are polish opportunities |
| 310 | Philosophy of AI | [AI Meta-Post — Overreach](../philosophy-of-ai/ai-meta-post-overreach/) | polish | 100 | 4 prompt sections are polish opportunities |
| 311 | Philosophy of AI | [The Double Descent Phenomenon](../philosophy-of-ai/the-double-descent-phenomenon/) | polish | 100 | 4 prompt sections are polish opportunities |
| 312 | Philosophy of Language | [Abandoned Words](../philosophy-of-language/abandoned-words/) | polish | 100 | 4 prompt sections are polish opportunities |
| 313 | Philosophy of Language | [Connotative Equivocation](../philosophy-of-language/connotative-equivocation/) | polish | 100 | 4 prompt sections are polish opportunities |
| 314 | Philosophy of Language | [Language & the Brain](../philosophy-of-language/language-the-brain/) | polish | 100 | 4 prompt sections are polish opportunities |
| 315 | Philosophy of Language | [Linguistic Scaffolding](../philosophy-of-language/linguistic-scaffolding/) | polish | 100 | 4 prompt sections are polish opportunities |
| 316 | Philosophy of Language | [Needless Semantic Complexity](../philosophy-of-language/needless-semantic-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 317 | Philosophy of Language | [Nomological Density of Grammar](../philosophy-of-language/nomological-density-of-grammar/) | polish | 100 | 4 prompt sections are polish opportunities |
| 318 | Philosophy of Language | [The Power of Analogy](../philosophy-of-language/the-power-of-analogy/) | polish | 100 | 4 prompt sections are polish opportunities |
| 319 | Philosophy of Language | [Thought = Language?](../philosophy-of-language/thought-language/) | polish | 100 | 4 prompt sections are polish opportunities |
| 320 | Philosophy of Mind | [Are there Selfless Acts?](../philosophy-of-mind/are-there-selfless-acts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 321 | Philosophy of Mind | [Land Ownership](../philosophy-of-mind/land-ownership/) | polish | 100 | 4 prompt sections are polish opportunities |
| 322 | Philosophy of Mind | [Philosophy of Mind — Core Concepts](../philosophy-of-mind/philosophy-of-mind-core-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 323 | Philosophy of Mind | [Preferences = Pleasures?](../philosophy-of-mind/preferences-pleasures/) | polish | 100 | 4 prompt sections are polish opportunities |
| 324 | Philosophy of Science | [Confounding Variables](../philosophy-of-science/confounding-variables/) | polish | 100 | 4 prompt sections are polish opportunities |
| 325 | Philosophy of Science | [Hard vs Soft Sciences](../philosophy-of-science/hard-vs-soft-sciences/) | polish | 100 | 4 prompt sections are polish opportunities |
| 326 | Philosophy of Science | [History as Forensic Science](../philosophy-of-science/history-as-forensic-science/) | polish | 100 | 4 prompt sections are polish opportunities |
| 327 | Philosophy of Science | [Improving Science](../philosophy-of-science/improving-science/) | polish | 100 | 4 prompt sections are polish opportunities |
| 328 | Philosophy of Science | [Inductive Density](../philosophy-of-science/inductive-density/) | polish | 100 | 4 prompt sections are polish opportunities |
| 329 | Philosophy of Science | [Methodological Naturalism](../philosophy-of-science/methodological-naturalism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 330 | Philosophy of Science | [Orthogonality](../philosophy-of-science/orthogonality/) | polish | 100 | 4 prompt sections are polish opportunities |
| 331 | Philosophy of Science | [P-Value Issues](../philosophy-of-science/p-value-issues/) | polish | 100 | 4 prompt sections are polish opportunities |
| 332 | Philosophy of Science | [Philosophy of Science — Core Concepts](../philosophy-of-science/philosophy-of-science-core-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 333 | Philosophy of Science | [The Notion of Laws](../philosophy-of-science/the-notion-of-laws/) | polish | 100 | 4 prompt sections are polish opportunities |
| 334 | Philosophy of Science | [The Power of Convergence](../philosophy-of-science/the-power-of-convergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 335 | Philosophy of Science | [The Use of Proxies](../philosophy-of-science/the-use-of-proxies/) | polish | 100 | 4 prompt sections are polish opportunities |
| 336 | Political Philosophy | [Critical Race Theory](../political-philosophy/critical-race-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 337 | Political Philosophy | [Elements of a Stable State](../political-philosophy/elements-of-a-stable-state/) | polish | 100 | 4 prompt sections are polish opportunities |
| 338 | Political Philosophy | [Identity Politics](../political-philosophy/identity-politics/) | polish | 100 | 4 prompt sections are polish opportunities |
| 339 | Political Philosophy | [Maintaining Scientific Credibility](../political-philosophy/maintaining-scientific-credibility/) | polish | 100 | 4 prompt sections are polish opportunities |
| 340 | Political Philosophy | [Metrics for Cultural Comparisons](../political-philosophy/metrics-for-cultural-comparisons/) | polish | 100 | 4 prompt sections are polish opportunities |
| 341 | Political Philosophy | [The Social Contract](../political-philosophy/the-social-contract/) | polish | 100 | 4 prompt sections are polish opportunities |
| 342 | Rational Thought | [Argument #1: Miraculous Event](../rational-thought/argument-1-miraculous-event/) | polish | 100 | 4 prompt sections are polish opportunities |
| 343 | Rational Thought | [Assessing Arguments](../rational-thought/assessing-arguments/) | polish | 100 | 4 prompt sections are polish opportunities |
| 344 | Rational Thought | [Avoiding Logical Fallacies](../rational-thought/avoiding-logical-fallacies/) | polish | 100 | 4 prompt sections are polish opportunities |
| 345 | Rational Thought | [Calculating Risks](../rational-thought/calculating-risks/) | polish | 100 | 4 prompt sections are polish opportunities |
| 346 | Rational Thought | [Depth or Width of Knowledge?](../rational-thought/depth-or-width-of-knowledge/) | polish | 100 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 1, queue positions 347-396

- `polish` 100 [Rational Thought / Empathy Overload](../rational-thought/empathy-overload/)
- `polish` 100 [Rational Thought / Factual Disagreements vs Semantic Misunderstandings](../rational-thought/factual-disagreements-vs-semantic-misunderstandings/)
- `polish` 100 [Rational Thought / Fine-Tuned Rationality](../rational-thought/fine-tuned-rationality/)
- `polish` 100 [Rational Thought / Monetary Goals](../rational-thought/monetary-goals/)
- `polish` 100 [Rational Thought / The Power of Statistics](../rational-thought/the-power-of-statistics/)
- `polish` 100 [Rational Thought / The Primacy of Emotions](../rational-thought/the-primacy-of-emotions/)
- `polish` 100 [Rational Thought / Tu Quoque or “You too!”](../rational-thought/tu-quoque-or-you-too/)
- `polish` 100 [Rational Thought / What is “Design Thinking”?](../rational-thought/what-is-design-thinking/)
- `polish` 100 [Rational Thought / Where Framing Goes Awry](../rational-thought/where-framing-goes-awry/)
- `polish` 100 [Economics / Behavioral Economics](../economics/behavioral-economics/)

### Next +2: cycle 1, queue positions 397-446

- `polish` 100 [Metaphysics / Objectively & Subjectively “Real”](../metaphysics/objectively-subjectively-real/)
- `polish` 100 [Metaphysics / Terrence Deacon on Emergence](../metaphysics/terrence-deacon-on-emergence/)
- `polish` 100 [Metaphysics / The Beginning of Time](../metaphysics/the-beginning-of-time/)
- `polish` 100 [Metaphysics / The Status of Evil](../metaphysics/the-status-of-evil/)
- `polish` 100 [Metaphysics / What is Metaphysics?](../metaphysics/what-is-metaphysics/)
- `polish` 100 [Miscellany / Assembly Theory](../miscellany/assembly-theory/)
- `polish` 100 [Miscellany / Cascading Factor Models](../miscellany/cascading-factor-models/)
- `polish` 100 [Miscellany / Dynamical Depth](../miscellany/dynamical-depth/)
- `polish` 100 [Miscellany / Profiling](../miscellany/profiling/)
- `polish` 100 [Miscellany / The Growing Disinclination for War](../miscellany/the-growing-disinclination-for-war/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 232
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 419
- review: 23
