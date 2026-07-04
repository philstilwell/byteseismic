# Byteseismic Editorial Audit Tracker

Generated: 2026-07-04
Batch size: 50 pages
Current cycle: 3
Current queue start: 4 of 346

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
| 4 | Philosophers | [Daniel Dennett](../philosophers/daniel-dennett/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 5 | Philosophers | [David Hume](../philosophers/david-hume/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 6 | Philosophers | [Plato](../philosophers/plato-2/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 7 | Philosophers | [René Descartes](../philosophers/rene-descartes/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 8 | Philosophers | [Socrates](../philosophers/socrates/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 9 | Philosophers | [Søren Kierkegaard](../philosophers/soren-kierkegaard/) | gap-fill | 89 | 4 prompt sections need gap fill |
| 10 | Philosophers | [Analytic Philosophers](../philosophers/analytic-philosophers/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 11 | Philosophers | [Baruch Spinoza](../philosophers/baruch-spinoza/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 12 | Philosophers | [Continental Philosophers](../philosophers/continental-philosophers/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 13 | Philosophers | [Immanuel Kant](../philosophers/immanuel-kant/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 14 | Philosophers | [Ancient Philosophers](../philosophers/ancient-philosophers/) | gap-fill | 94 | 4 prompt sections need gap fill |
| 15 | Philosophers | [Martin Heidegger](../philosophers/martin-heidegger/) | gap-fill | 94 | 4 prompt sections need gap fill |
| 16 | Philosophers | [Thomas Hobbes](../philosophers/thomas-hobbes/) | gap-fill | 94 | 4 prompt sections need gap fill |
| 17 | Philosophers | [At the Edge of Miracles](../philosophers/at-the-edge-of-miracles/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 18 | Philosophers | [Avicenna](../philosophers/avicenna/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 19 | Philosophers | [G.E. Moore](../philosophers/g-e-moore/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 20 | Philosophers | [Gottlob Frege](../philosophers/gottlob-frege/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 21 | Philosophers | [Jean-Jacques Rousseau](../philosophers/jean-jacques-rousseau/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 22 | Philosophers | [John Rawls](../philosophers/john-rawls/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 23 | Philosophers | [Bertrand Russell](../philosophers/bertrand-russell/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 24 | Philosophers | [Charles Sanders Peirce](../philosophers/charles-sanders-peirce/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 25 | Philosophers | [Edmund Husserl](../philosophers/edmund-husserl/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 26 | Philosophers | [Epicurus](../philosophers/epicurus/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 27 | Philosophers | [Gottfried Wilhelm Leibniz](../philosophers/gottfried-wilhelm-leibniz/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 28 | Philosophers | [Jacques Derrida](../philosophers/jacques-derrida/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 29 | Philosophers | [John Locke](../philosophers/john-locke/) | gap-fill | 96 | 4 prompt sections need gap fill |
| 30 | Philosophers | [Duns Scotus](../philosophers/duns-scotus/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 31 | Philosophers | [Michel Foucault](../philosophers/michel-foucault/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 32 | Philosophers | [Willard Van Orman Quine](../philosophers/willard-van-orman-quine/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 33 | Philosophers | [William James](../philosophers/william-james/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 34 | Philosophers | [Al-Ghazali](../philosophers/al-ghazali/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 35 | Philosophers | [Anselm of Canterbury](../philosophers/anselm-of-canterbury/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 36 | Philosophers | [Arthur Schopenhauer](../philosophers/arthur-schopenhauer/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 37 | Philosophers | [Augustine of Hippo](../philosophers/augustine-of-hippo/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 38 | Philosophers | [Averroes](../philosophers/averroes/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 39 | Philosophers | [Cicero](../philosophers/cicero/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 40 | Philosophers | [Confucius](../philosophers/confucius/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 41 | Philosophers | [Critical Theorists](../philosophers/critical-theorists/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 42 | Philosophers | [Dogen](../philosophers/dogen/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 43 | Philosophers | [Elizabeth Anscombe](../philosophers/elizabeth-anscombe/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 44 | Philosophers | [Epictetus](../philosophers/epictetus/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 45 | Philosophers | [Friedrich Nietzsche](../philosophers/friedrich-nietzsche/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 46 | Philosophers | [George Berkeley](../philosophers/george-berkeley/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 47 | Philosophers | [Hannah Arendt](../philosophers/hannah-arendt/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 48 | Philosophers | [Heraclitus](../philosophers/heraclitus/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 49 | Philosophers | [John Dewey](../philosophers/john-dewey/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 50 | Philosophers | [John Stuart Mill](../philosophers/john-stuart-mill/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 51 | Philosophers | [Judith Butler](../philosophers/judith-butler/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 52 | Philosophers | [Jurgen Habermas](../philosophers/jurgen-habermas/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 53 | Philosophers | [Karl Marx](../philosophers/karl-marx/) | gap-fill | 100 | 4 prompt sections need gap fill |

## Upcoming Batch Preview

### Next +1: cycle 3, queue positions 54-103

- `gap-fill` 100 [Philosophers / Laozi](../philosophers/laozi/)
- `gap-fill` 100 [Philosophers / Maimonides](../philosophers/maimonides/)
- `gap-fill` 100 [Philosophers / Marcus Aurelius](../philosophers/marcus-aurelius/)
- `gap-fill` 100 [Philosophers / Mary Wollstonecraft](../philosophers/mary-wollstonecraft/)
- `gap-fill` 100 [Philosophers / Maurice Merleau-Ponty](../philosophers/maurice-merleau-ponty/)
- `gap-fill` 100 [Philosophers / Mencius](../philosophers/mencius/)
- `gap-fill` 100 [Philosophers / Mozi](../philosophers/mozi/)
- `gap-fill` 100 [Philosophers / Nagarjuna](../philosophers/nagarjuna/)
- `gap-fill` 100 [Philosophers / Niccolo Machiavelli](../philosophers/niccolo-machiavelli/)
- `gap-fill` 100 [Philosophers / Parmenides](../philosophers/parmenides/)

### Next +2: cycle 3, queue positions 104-153

- `polish` 93 [Philosophy of Mind / Elitzur on Consciousness](../philosophy-of-mind/elitzur-on-consciousness/)
- `polish` 94 [Philosophy of Science / Is Logic Acquired Inductively?](../philosophy-of-science/is-logic-acquired-inductively/)
- `polish` 94 [Epistemology / Case #6 – Insatiable Loops](../epistemology/case-6-insatiable-loops/)
- `polish` 94 [Humanistic Philosophies / What is Existentialism?](../humanistic-philosophies/what-is-existentialism/)
- `polish` 94 [Introduction / Miscellaneous Philosophers](../introduction/miscellaneous-philosophers/)
- `polish` 95 [Epistemology / Decision-Making](../epistemology/decision-making/)
- `polish` 95 [Ethics / Fictional Meta-Ethics Debate](../ethics/fictional-meta-ethics-debate/)
- `polish` 95 [Philosophical Inquiry / Dangers: Strong Leaders](../philosophical-inquiry/dangers-strong-leaders/)
- `polish` 95 [Philosophical Inquiry / Dangers: Co-opted Wonders](../philosophical-inquiry/dangers-co-opted-wonders/)
- `polish` 95 [Philosophical Inquiry / Dangers: Half-Searches](../philosophical-inquiry/dangers-half-searches/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 343
- Estimated batches per cycle: 7

- gap-fill: 82
- polish: 264
