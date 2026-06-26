# Byteseismic Editorial Audit Tracker

Generated: 2026-06-26
Batch size: 50 pages
Current cycle: 2
Current queue start: 101 of 528

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
| 101 | Philosophers | [John Stuart Mill](../philosophers/john-stuart-mill/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 102 | Philosophers | [Judith Butler](../philosophers/judith-butler/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 103 | Philosophers | [Jurgen Habermas](../philosophers/jurgen-habermas/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 104 | Philosophers | [Karl Marx](../philosophers/karl-marx/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 105 | Philosophers | [Laozi](../philosophers/laozi/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 106 | Philosophers | [Maimonides](../philosophers/maimonides/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 107 | Philosophers | [Marcus Aurelius](../philosophers/marcus-aurelius/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 108 | Philosophers | [Mary Wollstonecraft](../philosophers/mary-wollstonecraft/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 109 | Philosophers | [Maurice Merleau-Ponty](../philosophers/maurice-merleau-ponty/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 110 | Philosophers | [Mencius](../philosophers/mencius/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 111 | Philosophers | [Mozi](../philosophers/mozi/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 112 | Philosophers | [Nagarjuna](../philosophers/nagarjuna/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 113 | Philosophers | [Niccolo Machiavelli](../philosophers/niccolo-machiavelli/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 114 | Philosophers | [Parmenides](../philosophers/parmenides/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 115 | Philosophers | [Plato](../philosophers/plato/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 116 | Philosophers | [Plotinus](../philosophers/plotinus/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 117 | Philosophers | [Pragmatists](../philosophers/pragmatists/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 118 | Philosophers | [Rationalists](../philosophers/rationalists/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 119 | Philosophers | [Saul Kripke](../philosophers/saul-kripke/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 120 | Philosophers | [Scholastics](../philosophers/scholastics/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 121 | Philosophers | [Seneca](../philosophers/seneca/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 122 | Philosophers | [Shankara](../philosophers/shankara/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 123 | Philosophers | [Theodor Adorno](../philosophers/theodor-adorno/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 124 | Philosophers | [Theodor W. Adorno](../philosophers/theodor-w-adorno/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 125 | Philosophers | [Walter Benjamin](../philosophers/walter-benjamin/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 126 | Philosophers | [William of Ockham](../philosophers/william-of-ockham/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 127 | Philosophers | [Xunzi](../philosophers/xunzi/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 128 | Philosophers | [Zhuangzi](../philosophers/zhuangzi/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 129 | Philosophers | [Aquinas’ Five Ways](../philosophers/aquinas-five-ways/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 130 | Philosophers | [Philosopher Club Membership](../philosophers/philosopher-club-membership/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 131 | Philosophers | [Philosophers or Philosophy?](../philosophers/philosophers-or-philosophy/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 132 | Philosophers | [Philosophical Gradients](../philosophers/philosophical-gradients/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 133 | Humanistic Philosophies | [Shoe-Tips & Hiddenness](../humanistic-philosophies/shoe-tips-hiddenness/) | polish | 86 | 3 prompt sections are polish opportunities |
| 134 | Philosophical Inquiry | [Dangers: Untestable Ideologies](../philosophical-inquiry/dangers-untestable-ideologies/) | polish | 86 | 3 prompt sections are polish opportunities |
| 135 | Philosophy of Science | [Observable Regularities](../philosophy-of-science/observable-regularity/) | polish | 86 | 3 prompt sections are polish opportunities |
| 136 | Epistemology | [Abduction: Utility and Issues](../epistemology/abduction-utility-and-issues/) | polish | 88 | 5 prompt sections are polish opportunities |
| 137 | Epistemology | [Establishing Cognitive Reliability (#2)](../epistemology/establishing-cognitive-reliability-2/) | polish | 88 | 3 prompt sections are polish opportunities |
| 138 | Epistemology | [Faith vs Science](../epistemology/faith-vs-science/) | polish | 88 | 3 prompt sections are polish opportunities |
| 139 | Epistemology | [Recent Issues in Epistemology](../epistemology/recent-issues-in-epistemology/) | polish | 88 | 3 prompt sections are polish opportunities |
| 140 | Epistemology | [Swapping Ideologies](../epistemology/swapping-ideologies/) | polish | 88 | 3 prompt sections are polish opportunities |
| 141 | Epistemology | [‘A Priori’ Knowledge Issues](../epistemology/a-priori-knowledge-issues/) | polish | 88 | 3 prompt sections are polish opportunities |
| 142 | Ethics | [Intrinsic Human Value](../ethics/intrinsic-human-value/) | polish | 89 | 5 prompt sections are polish opportunities |
| 143 | Philosophy of Language | [What is Etymology?](../philosophy-of-language/what-is-etymology/) | polish | 89 | 5 prompt sections are polish opportunities |
| 144 | Epistemology | [Avoiding Single-Cause Dogmatism](../epistemology/avoiding-single-cause-dogmatism/) | polish | 89 | 4 prompt sections are polish opportunities |
| 145 | Ethics | [⌁ Finite Agency, Moral Demand, and Happiness](../ethics/finite-agency-moral-demand-and-happiness/) | polish | 89 | 4 prompt sections are polish opportunities |
| 146 | Rational Thought | [Perverse Incentives](../rational-thought/perverse-incentives/) | polish | 89 | 4 prompt sections are polish opportunities |
| 147 | Epistemology | [Doxastic Voluntarism](../epistemology/doxastic-voluntarism/) | polish | 89 | 3 prompt sections are polish opportunities |
| 148 | Humanistic Philosophies | [Can Humans Change?](../humanistic-philosophies/can-humans-change/) | polish | 90 | 5 prompt sections are polish opportunities |
| 149 | Humanistic Philosophies | [Do Humans have an Essence?](../humanistic-philosophies/do-humans-have-an-essence/) | polish | 90 | 4 prompt sections are polish opportunities |
| 150 | Rational Thought | [Factual Disagreements vs Semantic Misunderstandings](../rational-thought/factual-disagreements-vs-semantic-misunderstandings/) | polish | 90 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 2, queue positions 151-200

- `polish` 90 [Epistemology / Logic](../epistemology/logic/)
- `polish` 91 [Epistemology / Epistemological Case Studies](../epistemology/epistemological-case-studies/)
- `polish` 91 [Ethics / Moral Black Boxes](../ethics/moral-black-boxes/)
- `polish` 91 [Ethics / Morality & Human Rights](../ethics/morality-human-rights/)
- `polish` 92 [Economics / Economics – Core Concepts](../economics/economics-core-concepts/)
- `polish` 92 [Philosophical Inquiry / Personal Truth?](../philosophical-inquiry/personal-truth/)
- `polish` 92 [Humanistic Philosophies / Anthropomorphized Gods](../humanistic-philosophies/anthropomorphized-gods/)
- `polish` 92 [Rational Thought / Regret Assessment](../rational-thought/regret-assessment/)
- `polish` 93 [Epistemology / Belief/Evidence Graphic](../epistemology/belief-evidence-graphic/)
- `polish` 93 [Epistemology / Pascal’s Wager](../epistemology/pascals-wager/)

### Next +2: cycle 2, queue positions 201-250

- `polish` 98 [Philosophical Inquiry / Conspiracies & Misunderstanding Human Nature](../philosophical-inquiry/conspiracies-misunderstanding-human-nature/)
- `polish` 98 [Philosophy of Mind / Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/)
- `polish` 98 [Philosophy of Mind / Subjective/Objective Free Will](../philosophy-of-mind/subjective-objective-free-will/)
- `polish` 98 [Rational Thought / Training Data Bias](../rational-thought/training-data-bias/)
- `polish` 98 [Economics / Wealth Creation](../economics/wealth-creation/)
- `polish` 98 [Epistemology / Case #1 – Credence Complexity](../epistemology/case-1-credence-complexity/)
- `polish` 98 [Epistemology / Case #4 – Recursive Credences](../epistemology/case-4-recursive-credences/)
- `polish` 98 [Ethics / Harris’ Notion of Morality](../ethics/harris-notion-of-morality/)
- `polish` 98 [Humanistic Philosophies / Accounting for X](../humanistic-philosophies/accounting-for-x/)
- `polish` 98 [Humanistic Philosophies / Religions](../humanistic-philosophies/religions/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 428
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 396
- review: 46
