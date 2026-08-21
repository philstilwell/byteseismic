# Byteseismic Editorial Audit Tracker

Generated: 2026-08-21
Batch size: 50 pages
Current cycle: 6
Current queue start: 51 of 346

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
| 49 | Philosophers | [Ancient Philosophers](../philosophers/ancient-philosophers/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 50 | Philosophers | [Anselm of Canterbury](../philosophers/anselm-of-canterbury/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 51 | Philosophers | [Arthur Schopenhauer](../philosophers/arthur-schopenhauer/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 52 | Philosophers | [At the Edge of Miracles](../philosophers/at-the-edge-of-miracles/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 53 | Philosophers | [Augustine of Hippo](../philosophers/augustine-of-hippo/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 54 | Philosophers | [Averroes](../philosophers/averroes/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 55 | Philosophers | [Avicenna](../philosophers/avicenna/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 56 | Philosophers | [Cicero](../philosophers/cicero/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 57 | Philosophers | [Confucius](../philosophers/confucius/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 58 | Philosophers | [Continental Philosophers](../philosophers/continental-philosophers/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 59 | Philosophers | [Critical Theorists](../philosophers/critical-theorists/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 60 | Philosophers | [Dogen](../philosophers/dogen/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 61 | Philosophers | [Elizabeth Anscombe](../philosophers/elizabeth-anscombe/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 62 | Philosophers | [Epictetus](../philosophers/epictetus/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 63 | Philosophers | [Existentialists](../philosophers/existentialists/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 64 | Philosophers | [Friedrich Nietzsche](../philosophers/friedrich-nietzsche/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 65 | Philosophers | [G.E. Moore](../philosophers/g-e-moore/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 66 | Philosophers | [George Berkeley](../philosophers/george-berkeley/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 67 | Philosophers | [Gottlob Frege](../philosophers/gottlob-frege/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 68 | Philosophers | [Hannah Arendt](../philosophers/hannah-arendt/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 69 | Philosophers | [Heraclitus](../philosophers/heraclitus/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 70 | Philosophers | [Jean-Jacques Rousseau](../philosophers/jean-jacques-rousseau/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 71 | Philosophers | [John Dewey](../philosophers/john-dewey/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 72 | Philosophers | [John Rawls](../philosophers/john-rawls/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 73 | Philosophers | [John Stuart Mill](../philosophers/john-stuart-mill/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 74 | Philosophers | [Judith Butler](../philosophers/judith-butler/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 75 | Philosophers | [Jurgen Habermas](../philosophers/jurgen-habermas/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 76 | Philosophers | [Karl Marx](../philosophers/karl-marx/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 77 | Philosophers | [Laozi](../philosophers/laozi/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 78 | Philosophers | [Maimonides](../philosophers/maimonides/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 79 | Philosophers | [Marcus Aurelius](../philosophers/marcus-aurelius/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 80 | Philosophers | [Mary Wollstonecraft](../philosophers/mary-wollstonecraft/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 81 | Philosophers | [Maurice Merleau-Ponty](../philosophers/maurice-merleau-ponty/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 82 | Philosophers | [Mencius](../philosophers/mencius/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 83 | Philosophers | [Mozi](../philosophers/mozi/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 84 | Philosophers | [Nagarjuna](../philosophers/nagarjuna/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 85 | Philosophers | [Niccolo Machiavelli](../philosophers/niccolo-machiavelli/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 86 | Philosophers | [Parmenides](../philosophers/parmenides/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 87 | Philosophers | [Plato](../philosophers/plato/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 88 | Philosophers | [Plotinus](../philosophers/plotinus/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 89 | Philosophers | [Pragmatists](../philosophers/pragmatists/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 90 | Philosophers | [Rationalists](../philosophers/rationalists/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 91 | Philosophers | [Saul Kripke](../philosophers/saul-kripke/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 92 | Philosophers | [Scholastics](../philosophers/scholastics/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 93 | Philosophers | [Seneca](../philosophers/seneca/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 94 | Philosophers | [Shankara](../philosophers/shankara/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 95 | Philosophers | [Theodor Adorno](../philosophers/theodor-adorno/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 96 | Philosophers | [Theodor W. Adorno](../philosophers/theodor-w-adorno/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 97 | Philosophers | [Walter Benjamin](../philosophers/walter-benjamin/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 98 | Philosophers | [William of Ockham](../philosophers/william-of-ockham/) | gap-fill | 100 | 4 prompt sections need gap fill |

## Upcoming Batch Preview

### Next +1: cycle 6, queue positions 101-150

- `gap-fill` 100 [Philosophers / Xunzi](../philosophers/xunzi/)
- `gap-fill` 100 [Philosophers / Zhuangzi](../philosophers/zhuangzi/)
- `gap-fill` 100 [Philosophers / Aquinas’ Five Ways](../philosophers/aquinas-five-ways/)
- `gap-fill` 100 [Philosophers / Philosopher Club Membership](../philosophers/philosopher-club-membership/)
- `gap-fill` 100 [Philosophers / Philosophers or Philosophy?](../philosophers/philosophers-or-philosophy/)
- `gap-fill` 100 [Philosophers / Philosophical Gradients](../philosophers/philosophical-gradients/)
- `polish` 86 [Philosophical Inquiry / Dangers: Untestable Ideologies](../philosophical-inquiry/dangers-untestable-ideologies/)
- `polish` 86 [Philosophy of Science / Observable Regularities](../philosophy-of-science/observable-regularity/)
- `polish` 88 [Epistemology / Abduction: Utility and Issues](../epistemology/abduction-utility-and-issues/)
- `polish` 89 [Ethics / Intrinsic Human Value](../ethics/intrinsic-human-value/)

### Next +2: cycle 6, queue positions 151-200

- `polish` 97 [Ethics / “Is” vs “Ought”](../ethics/is-vs-ought/)
- `polish` 97 [Philosophical Inquiry / How Minds are Changed](../philosophical-inquiry/how-minds-are-changed/)
- `polish` 98 [Philosophical Inquiry / Conspiracies & Misunderstanding Human Nature](../philosophical-inquiry/conspiracies-misunderstanding-human-nature/)
- `polish` 98 [Philosophy of Mind / Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/)
- `polish` 98 [Epistemology / Case #1 – Credence Complexity](../epistemology/case-1-credence-complexity/)
- `polish` 98 [Epistemology / Case #4 – Recursive Credences](../epistemology/case-4-recursive-credences/)
- `polish` 98 [Philosophical Inquiry / Dangers: Carrot & Stick](../philosophical-inquiry/dangers-carrot-stick/)
- `polish` 98 [Philosophical Inquiry / Testing Ideologies](../philosophical-inquiry/testing-ideologies/)
- `polish` 98 [Rational Thought / Scope of Influence](../rational-thought/scope-of-influence/)
- `polish` 99 [Philosophical Inquiry / Dangers: Ideologies of Mystery](../philosophical-inquiry/dangers-ideologies-of-mystery/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 296
- Estimated batches per cycle: 7

- gap-fill: 64
- polish: 242
- review: 40
