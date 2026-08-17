# Byteseismic Editorial Audit Tracker

Generated: 2026-08-17
Batch size: 50 pages
Current cycle: 6
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
| 1 | Philosophy of Mind | [Subjective/Objective Free Will](../philosophy-of-mind/subjective-objective-free-will/) | review | 44 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 2 | Humanistic Philosophies | [Accounting for X](../humanistic-philosophies/accounting-for-x/) | review | 44 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 3 | Philosophy of Language | [What is Language?](../philosophy-of-language/what-is-language/) | review | 52 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 4 | Economics | [What is Economics?](../economics/what-is-economics/) | review | 54 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 5 | Economics | [Schools of Economic Thought](../economics/schools-of-economic-thought/) | review | 54 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 6 | Economics | [Economic Comparisons](../economics/economic-comparisons/) | review | 60 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 7 | Economics | [Wealth Creation](../economics/wealth-creation/) | review | 60 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 8 | Economics | [Taxation](../economics/taxation/) | review | 68 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 9 | Ethics | [Fictional Meta-Ethics Debate](../ethics/fictional-meta-ethics-debate/) | review | 73 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 10 | Philosophy of Mind | [What is Consciousness?](../philosophy-of-mind/what-is-consciousness/) | review | 73 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 11 | Metaphysics | [Jeremy Sherman on Emergence](../metaphysics/jeremy-sherman-on-emergence/) | review | 73 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 12 | Economics | [What are Moral Hazards?](../economics/what-are-moral-hazards/) | review | 75 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 13 | Economics | [Economic Stability](../economics/economic-stability/) | review | 76 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 14 | Economics | [Minimum Wage](../economics/minimum-wage/) | review | 76 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 15 | Humanistic Philosophies | [What is Existentialism?](../humanistic-philosophies/what-is-existentialism/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 16 | Philosophical Inquiry | [Dangers: The Notion of Fate](../philosophical-inquiry/dangers-the-notion-of-fate/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 17 | Philosophy of Mind | [Elitzur on Consciousness](../philosophy-of-mind/elitzur-on-consciousness/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 18 | Epistemology | [Rationality Discussion](../epistemology/rationality-discussion/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 19 | Introduction | [Miscellaneous Philosophers](../introduction/miscellaneous-philosophers/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 20 | Epistemology | [Collapsing Epistemological Terms](../epistemology/collapsing-epistemological-terms/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 21 | Rational Thought | [Training Data Bias](../rational-thought/training-data-bias/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 22 | Epistemology | [“Adequate” Evidence](../epistemology/adequate-evidence/) | review | 81 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 23 | Epistemology | [Preponderance of Evidence?](../epistemology/preponderance-of-evidence/) | review | 82 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 24 | Rational Thought | [1 at 99.5% or 5 at 95%?](../rational-thought/1-at-99-5-or-5-at-95/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 25 | Philosophers | [Daniel Dennett](../philosophers/daniel-dennett/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 26 | Philosophers | [David Hume](../philosophers/david-hume/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 27 | Philosophers | [Plato](../philosophers/plato-2/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 28 | Philosophers | [René Descartes](../philosophers/rene-descartes/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 29 | Philosophers | [Socrates](../philosophers/socrates/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 30 | Philosophers | [Søren Kierkegaard](../philosophers/soren-kierkegaard/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 31 | Philosophers | [Bertrand Russell](../philosophers/bertrand-russell/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 32 | Philosophers | [Charles Sanders Peirce](../philosophers/charles-sanders-peirce/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 33 | Philosophers | [Jacques Derrida](../philosophers/jacques-derrida/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 34 | Philosophers | [John Locke](../philosophers/john-locke/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 35 | Philosophers | [Thomas Aquinas](../philosophers/thomas-aquinas/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 36 | Philosophers | [Immanuel Kant](../philosophers/immanuel-kant/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 37 | Philosophers | [Martin Heidegger](../philosophers/martin-heidegger/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 38 | Philosophers | [Thomas Hobbes](../philosophers/thomas-hobbes/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 39 | Philosophers | [Willard Van Orman Quine](../philosophers/willard-van-orman-quine/) | gap-fill | 95 | 4 prompt sections need gap fill |
| 40 | Philosophers | [Baruch Spinoza](../philosophers/baruch-spinoza/) | gap-fill | 97 | 4 prompt sections need gap fill |
| 41 | Philosophers | [Edmund Husserl](../philosophers/edmund-husserl/) | gap-fill | 97 | 4 prompt sections need gap fill |
| 42 | Philosophers | [Epicurus](../philosophers/epicurus/) | gap-fill | 97 | 4 prompt sections need gap fill |
| 43 | Philosophers | [Gottfried Wilhelm Leibniz](../philosophers/gottfried-wilhelm-leibniz/) | gap-fill | 97 | 4 prompt sections need gap fill |
| 44 | Philosophers | [Empiricists](../philosophers/empiricists/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 45 | Philosophers | [Phenomenologists](../philosophers/phenomenologists/) | gap-fill | 98 | 4 prompt sections need gap fill |
| 46 | Philosophers | [Duns Scotus](../philosophers/duns-scotus/) | gap-fill | 99 | 4 prompt sections need gap fill |
| 47 | Philosophers | [Michel Foucault](../philosophers/michel-foucault/) | gap-fill | 99 | 4 prompt sections need gap fill |
| 48 | Philosophers | [William James](../philosophers/william-james/) | gap-fill | 99 | 4 prompt sections need gap fill |
| 49 | Philosophers | [Al-Ghazali](../philosophers/al-ghazali/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 50 | Philosophers | [Analytic Philosophers](../philosophers/analytic-philosophers/) | gap-fill | 100 | 4 prompt sections need gap fill |

## Upcoming Batch Preview

### Next +1: cycle 6, queue positions 51-100

- `gap-fill` 100 [Philosophers / Ancient Philosophers](../philosophers/ancient-philosophers/)
- `gap-fill` 100 [Philosophers / Anselm of Canterbury](../philosophers/anselm-of-canterbury/)
- `gap-fill` 100 [Philosophers / Arthur Schopenhauer](../philosophers/arthur-schopenhauer/)
- `gap-fill` 100 [Philosophers / At the Edge of Miracles](../philosophers/at-the-edge-of-miracles/)
- `gap-fill` 100 [Philosophers / Augustine of Hippo](../philosophers/augustine-of-hippo/)
- `gap-fill` 100 [Philosophers / Averroes](../philosophers/averroes/)
- `gap-fill` 100 [Philosophers / Avicenna](../philosophers/avicenna/)
- `gap-fill` 100 [Philosophers / Cicero](../philosophers/cicero/)
- `gap-fill` 100 [Philosophers / Confucius](../philosophers/confucius/)
- `gap-fill` 100 [Philosophers / Continental Philosophers](../philosophers/continental-philosophers/)

### Next +2: cycle 6, queue positions 101-150

- `gap-fill` 100 [Philosophers / Xunzi](../philosophers/xunzi/)
- `gap-fill` 100 [Philosophers / Zhuangzi](../philosophers/zhuangzi/)
- `gap-fill` 100 [Philosophers / Aquinas’ Five Ways](../philosophers/aquinas-five-ways/)
- `gap-fill` 100 [Philosophers / Philosopher Club Membership](../philosophers/philosopher-club-membership/)
- `gap-fill` 100 [Philosophers / Philosophers or Philosophy?](../philosophers/philosophers-or-philosophy/)
- `gap-fill` 100 [Philosophers / Philosophical Gradients](../philosophers/philosophical-gradients/)
- `polish` 86 [Epistemology / Counterfactual Reasoning](../epistemology/counterfactual-reasoning/)
- `polish` 86 [Philosophical Inquiry / Dangers: Untestable Ideologies](../philosophical-inquiry/dangers-untestable-ideologies/)
- `polish` 86 [Philosophy of Science / Observable Regularities](../philosophy-of-science/observable-regularity/)
- `polish` 88 [Epistemology / Abduction: Utility and Issues](../epistemology/abduction-utility-and-issues/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 346
- Estimated batches per cycle: 7

- gap-fill: 82
- polish: 240
- review: 24
