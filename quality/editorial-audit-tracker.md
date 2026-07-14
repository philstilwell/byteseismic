# Byteseismic Editorial Audit Tracker

Generated: 2026-07-14
Batch size: 50 pages
Current cycle: 4
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
| 1 | Philosophy of Mind | [Elitzur on Consciousness](../philosophy-of-mind/elitzur-on-consciousness/) | review | 69 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 2 | Humanistic Philosophies | [Christian Apologetics](../humanistic-philosophies/christian-apologetics/) | review | 70 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 3 | Rational Thought | [Training Data Bias](../rational-thought/training-data-bias/) | review | 70 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 4 | Epistemology | [The Burden of Proof](../epistemology/the-burden-of-proof/) | review | 72 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 5 | Epistemology | [“Adequate” Evidence](../epistemology/adequate-evidence/) | review | 72 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 6 | Philosophy of Mind | [What is Consciousness?](../philosophy-of-mind/what-is-consciousness/) | review | 73 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 7 | Philosophical Inquiry | [The Danger of “Resulting”](../philosophical-inquiry/the-danger-of-resulting/) | review | 76 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 8 | Philosophical Inquiry | [Selective Pressures on Ideologies](../philosophical-inquiry/selective-pressures-on-ideologies/) | review | 76 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 9 | Philosophy of Science | [Is Logic Acquired Inductively?](../philosophy-of-science/is-logic-acquired-inductively/) | review | 76 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 10 | Philosophical Inquiry | [Dangers: Ontological Buffet](../philosophical-inquiry/dangers-ontological-buffet/) | review | 77 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 11 | Humanistic Philosophies | [What is Existentialism?](../humanistic-philosophies/what-is-existentialism/) | review | 77 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 12 | Epistemology | [Rationality Discussion](../epistemology/rationality-discussion/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 13 | Metaphysics | [Jeremy Sherman on Emergence](../metaphysics/jeremy-sherman-on-emergence/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 14 | Philosophical Inquiry | [Do I need a “worldview”?](../philosophical-inquiry/do-i-need-a-worldview/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 15 | Philosophical Inquiry | [Dangers: The Notion of Fate](../philosophical-inquiry/dangers-the-notion-of-fate/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 16 | Introduction | [Miscellaneous Philosophers](../introduction/miscellaneous-philosophers/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 17 | Philosophers | [Empiricists](../philosophers/empiricists/) | gap-fill | 87 | 4 prompt sections need gap fill |
| 18 | Philosophers | [Phenomenologists](../philosophers/phenomenologists/) | gap-fill | 88 | 4 prompt sections need gap fill |
| 19 | Philosophers | [Daniel Dennett](../philosophers/daniel-dennett/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 20 | Philosophers | [David Hume](../philosophers/david-hume/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 21 | Philosophers | [Plato](../philosophers/plato-2/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 22 | Philosophers | [René Descartes](../philosophers/rene-descartes/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 23 | Philosophers | [Socrates](../philosophers/socrates/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 24 | Philosophers | [Søren Kierkegaard](../philosophers/soren-kierkegaard/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 25 | Philosophers | [Analytic Philosophers](../philosophers/analytic-philosophers/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 26 | Philosophers | [Baruch Spinoza](../philosophers/baruch-spinoza/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 27 | Philosophers | [Immanuel Kant](../philosophers/immanuel-kant/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 28 | Philosophers | [Ancient Philosophers](../philosophers/ancient-philosophers/) | gap-fill | 94 | 4 prompt sections need gap fill |
| 29 | Philosophers | [Martin Heidegger](../philosophers/martin-heidegger/) | gap-fill | 94 | 4 prompt sections need gap fill |
| 30 | Philosophers | [Thomas Hobbes](../philosophers/thomas-hobbes/) | gap-fill | 94 | 4 prompt sections need gap fill |
| 31 | Philosophers | [At the Edge of Miracles](../philosophers/at-the-edge-of-miracles/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 32 | Philosophers | [Bertrand Russell](../philosophers/bertrand-russell/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 33 | Philosophers | [Charles Sanders Peirce](../philosophers/charles-sanders-peirce/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 34 | Philosophers | [Edmund Husserl](../philosophers/edmund-husserl/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 35 | Philosophers | [Epicurus](../philosophers/epicurus/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 36 | Philosophers | [Gottfried Wilhelm Leibniz](../philosophers/gottfried-wilhelm-leibniz/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 37 | Philosophers | [Jacques Derrida](../philosophers/jacques-derrida/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 38 | Philosophers | [John Locke](../philosophers/john-locke/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 39 | Philosophers | [Duns Scotus](../philosophers/duns-scotus/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 40 | Philosophers | [Michel Foucault](../philosophers/michel-foucault/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 41 | Philosophers | [Willard Van Orman Quine](../philosophers/willard-van-orman-quine/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 42 | Philosophers | [William James](../philosophers/william-james/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 43 | Philosophers | [Thomas Aquinas](../philosophers/thomas-aquinas/) | gap-fill | 99 | 4 prompt sections need gap fill |
| 44 | Philosophers | [Al-Ghazali](../philosophers/al-ghazali/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 45 | Philosophers | [Anselm of Canterbury](../philosophers/anselm-of-canterbury/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 46 | Philosophers | [Arthur Schopenhauer](../philosophers/arthur-schopenhauer/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 47 | Philosophers | [Augustine of Hippo](../philosophers/augustine-of-hippo/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 48 | Philosophers | [Averroes](../philosophers/averroes/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 49 | Philosophers | [Avicenna](../philosophers/avicenna/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 50 | Philosophers | [Cicero](../philosophers/cicero/) | gap-fill | 100 | 4 prompt sections need gap fill |

## Upcoming Batch Preview

### Next +1: cycle 4, queue positions 51-100

- `gap-fill` 100 [Philosophers / Confucius](../philosophers/confucius/)
- `gap-fill` 100 [Philosophers / Continental Philosophers](../philosophers/continental-philosophers/)
- `gap-fill` 100 [Philosophers / Critical Theorists](../philosophers/critical-theorists/)
- `gap-fill` 100 [Philosophers / Dogen](../philosophers/dogen/)
- `gap-fill` 100 [Philosophers / Elizabeth Anscombe](../philosophers/elizabeth-anscombe/)
- `gap-fill` 100 [Philosophers / Epictetus](../philosophers/epictetus/)
- `gap-fill` 100 [Philosophers / Existentialists](../philosophers/existentialists/)
- `gap-fill` 100 [Philosophers / Friedrich Nietzsche](../philosophers/friedrich-nietzsche/)
- `gap-fill` 100 [Philosophers / G.E. Moore](../philosophers/g-e-moore/)
- `gap-fill` 100 [Philosophers / George Berkeley](../philosophers/george-berkeley/)

### Next +2: cycle 4, queue positions 101-150

- `polish` 88 [Epistemology / Abduction: Utility and Issues](../epistemology/abduction-utility-and-issues/)
- `polish` 89 [Ethics / Intrinsic Human Value](../ethics/intrinsic-human-value/)
- `polish` 89 [Philosophy of Language / What is Etymology?](../philosophy-of-language/what-is-etymology/)
- `polish` 89 [Epistemology / Avoiding Single-Cause Dogmatism](../epistemology/avoiding-single-cause-dogmatism/)
- `polish` 89 [Ethics / ⌁ Finite Agency, Moral Demand, and Happiness](../ethics/finite-agency-moral-demand-and-happiness/)
- `polish` 89 [Rational Thought / Perverse Incentives](../rational-thought/perverse-incentives/)
- `polish` 89 [Epistemology / Doxastic Voluntarism](../epistemology/doxastic-voluntarism/)
- `polish` 90 [Humanistic Philosophies / Can Humans Change?](../humanistic-philosophies/can-humans-change/)
- `polish` 90 [Humanistic Philosophies / Do Humans have an Essence?](../humanistic-philosophies/do-humans-have-an-essence/)
- `polish` 91 [Epistemology / Epistemological Case Studies](../epistemology/epistemological-case-studies/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 346
- Estimated batches per cycle: 7

- gap-fill: 82
- polish: 248
- review: 16
