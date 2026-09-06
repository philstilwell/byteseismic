# Byteseismic Editorial Audit Tracker

Generated: 2026-09-06
Batch size: 50 pages
Current cycle: 8
Current queue start: 1 of 346

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
| 1 | Philosophers | [Empiricists](../philosophers/empiricists/) | review | 54 | 3 prompt sections need review; 4 prompt sections need gap fill |
| 2 | Philosophy of Mind | [What is Consciousness?](../philosophy-of-mind/what-is-consciousness/) | review | 60 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 3 | Philosophers | [Analytic Philosophers](../philosophers/analytic-philosophers/) | review | 60 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 4 | Philosophy of Science | [The Use of Proxies](../philosophy-of-science/the-use-of-proxies/) | review | 60 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 5 | Philosophy of Science | [Methodological Naturalism](../philosophy-of-science/methodological-naturalism/) | review | 60 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 6 | Philosophers | [David Hume](../philosophers/david-hume/) | review | 62 | 3 prompt sections need review; 4 prompt sections need gap fill |
| 7 | Philosophers | [Baruch Spinoza](../philosophers/baruch-spinoza/) | review | 62 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 8 | Philosophers | [Immanuel Kant](../philosophers/immanuel-kant/) | review | 62 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 9 | Political Philosophy | [Critical Race Theory](../political-philosophy/critical-race-theory/) | review | 64 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 10 | Philosophers | [Ancient Philosophers](../philosophers/ancient-philosophers/) | review | 65 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 11 | Rational Thought | [Calculating Risks](../rational-thought/calculating-risks/) | review | 69 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 12 | Philosophy of Mind | [Elitzur on Consciousness](../philosophy-of-mind/elitzur-on-consciousness/) | review | 69 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 13 | Rational Thought | [Depth or Width of Knowledge?](../rational-thought/depth-or-width-of-knowledge/) | review | 70 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 14 | Epistemology | [“Adequate” Evidence](../epistemology/adequate-evidence/) | review | 70 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 15 | Metaphysics | [Jeremy Sherman on Emergence](../metaphysics/jeremy-sherman-on-emergence/) | review | 70 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 16 | Political Philosophy | [Identity Politics](../political-philosophy/identity-politics/) | review | 70 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 17 | Philosophy of Science | [Orthogonality](../philosophy-of-science/orthogonality/) | review | 71 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 18 | Philosophers | [René Descartes](../philosophers/rene-descartes/) | review | 72 | 3 prompt sections need review; 4 prompt sections need gap fill |
| 19 | Philosophers | [Daniel Dennett](../philosophers/daniel-dennett/) | review | 74 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 20 | Philosophers | [Søren Kierkegaard](../philosophers/soren-kierkegaard/) | review | 74 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 21 | Philosophy of Science | [The Power of Convergence](../philosophy-of-science/the-power-of-convergence/) | review | 74 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 22 | Philosophy of Science | [Improving Science](../philosophy-of-science/improving-science/) | review | 74 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 23 | Philosophers | [Plato](../philosophers/plato-2/) | review | 76 | 3 prompt sections need review; 4 prompt sections need gap fill |
| 24 | Philosophers | [Socrates](../philosophers/socrates/) | review | 76 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 25 | Philosophers | [Thomas Hobbes](../philosophers/thomas-hobbes/) | review | 77 | 3 prompt sections need review; 4 prompt sections need gap fill |
| 26 | Political Philosophy | [The Social Contract](../political-philosophy/the-social-contract/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 27 | Humanistic Philosophies | [What is Existentialism?](../humanistic-philosophies/what-is-existentialism/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 28 | Philosophers | [Gottfried Wilhelm Leibniz](../philosophers/gottfried-wilhelm-leibniz/) | review | 79 | 3 prompt sections need review; 4 prompt sections need gap fill |
| 29 | Philosophers | [Thomas Aquinas](../philosophers/thomas-aquinas/) | review | 79 | 3 prompt sections need review; 4 prompt sections need gap fill |
| 30 | Epistemology | [Rationality Discussion](../epistemology/rationality-discussion/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 31 | Introduction | [Miscellaneous Philosophers](../introduction/miscellaneous-philosophers/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 32 | Philosophers | [Martin Heidegger](../philosophers/martin-heidegger/) | review | 80 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 33 | Philosophers | [Phenomenologists](../philosophers/phenomenologists/) | review | 80 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 34 | Philosophy of Science | [P-Value Issues](../philosophy-of-science/p-value-issues/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 35 | Philosophers | [Epicurus](../philosophers/epicurus/) | review | 81 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 36 | Political Philosophy | [Elements of a Stable State](../political-philosophy/elements-of-a-stable-state/) | review | 81 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 37 | Philosophers | [Duns Scotus](../philosophers/duns-scotus/) | review | 83 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 38 | Philosophers | [William James](../philosophers/william-james/) | review | 83 | 2 prompt sections need review; 4 prompt sections need gap fill |
| 39 | Rational Thought | [1 at 99.5% or 5 at 95%?](../rational-thought/1-at-99-5-or-5-at-95/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 40 | Rational Thought | [Avoiding Logical Fallacies](../rational-thought/avoiding-logical-fallacies/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 41 | Philosophers | [Bertrand Russell](../philosophers/bertrand-russell/) | gap-fill | 85 | 4 prompt sections need gap fill |
| 42 | Philosophers | [Jacques Derrida](../philosophers/jacques-derrida/) | gap-fill | 85 | 4 prompt sections need gap fill |
| 43 | Philosophers | [John Locke](../philosophers/john-locke/) | gap-fill | 85 | 4 prompt sections need gap fill |
| 44 | Philosophers | [Edmund Husserl](../philosophers/edmund-husserl/) | gap-fill | 86 | 4 prompt sections need gap fill |
| 45 | Philosophers | [Willard Van Orman Quine](../philosophers/willard-van-orman-quine/) | gap-fill | 86 | 4 prompt sections need gap fill |
| 46 | Philosophers | [Charles Sanders Peirce](../philosophers/charles-sanders-peirce/) | gap-fill | 88 | 4 prompt sections need gap fill |
| 47 | Philosophers | [Michel Foucault](../philosophers/michel-foucault/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 48 | Philosophers | [Al-Ghazali](../philosophers/al-ghazali/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 49 | Philosophers | [Anselm of Canterbury](../philosophers/anselm-of-canterbury/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 50 | Philosophers | [Arthur Schopenhauer](../philosophers/arthur-schopenhauer/) | gap-fill | 100 | 4 prompt sections need gap fill |

## Upcoming Batch Preview

### Next +1: cycle 8, queue positions 51-100

- `gap-fill` 100 [Philosophers / At the Edge of Miracles](../philosophers/at-the-edge-of-miracles/)
- `gap-fill` 100 [Philosophers / Augustine of Hippo](../philosophers/augustine-of-hippo/)
- `gap-fill` 100 [Philosophers / Averroes](../philosophers/averroes/)
- `gap-fill` 100 [Philosophers / Avicenna](../philosophers/avicenna/)
- `gap-fill` 100 [Philosophers / Cicero](../philosophers/cicero/)
- `gap-fill` 100 [Philosophers / Confucius](../philosophers/confucius/)
- `gap-fill` 100 [Philosophers / Continental Philosophers](../philosophers/continental-philosophers/)
- `gap-fill` 100 [Philosophers / Critical Theorists](../philosophers/critical-theorists/)
- `gap-fill` 100 [Philosophers / Dogen](../philosophers/dogen/)
- `gap-fill` 100 [Philosophers / Elizabeth Anscombe](../philosophers/elizabeth-anscombe/)

### Next +2: cycle 8, queue positions 101-150

- `gap-fill` 100 [Philosophers / Philosopher Club Membership](../philosophers/philosopher-club-membership/)
- `gap-fill` 100 [Philosophers / Philosophers or Philosophy?](../philosophers/philosophers-or-philosophy/)
- `gap-fill` 100 [Philosophers / Philosophical Gradients](../philosophers/philosophical-gradients/)
- `polish` 86 [Philosophical Inquiry / Dangers: Untestable Ideologies](../philosophical-inquiry/dangers-untestable-ideologies/)
- `polish` 86 [Philosophy of Science / Observable Regularities](../philosophy-of-science/observable-regularity/)
- `polish` 88 [Epistemology / Abduction: Utility and Issues](../epistemology/abduction-utility-and-issues/)
- `polish` 89 [Ethics / Intrinsic Human Value](../ethics/intrinsic-human-value/)
- `polish` 89 [Philosophy of Language / What is Etymology?](../philosophy-of-language/what-is-etymology/)
- `polish` 89 [Epistemology / Avoiding Single-Cause Dogmatism](../epistemology/avoiding-single-cause-dogmatism/)
- `polish` 89 [Epistemology / Collapsing Epistemological Terms](../epistemology/collapsing-epistemological-terms/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 346
- Estimated batches per cycle: 7

- gap-fill: 63
- polish: 243
- review: 40
