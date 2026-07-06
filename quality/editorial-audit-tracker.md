# Byteseismic Editorial Audit Tracker

Generated: 2026-07-06
Batch size: 50 pages
Current cycle: 3
Current queue start: 104 of 346

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
| 104 | Philosophy of Mind | [Elitzur on Consciousness](../philosophy-of-mind/elitzur-on-consciousness/) | polish | 93 | 2 prompt sections are polish opportunities |
| 105 | Philosophy of Science | [Is Logic Acquired Inductively?](../philosophy-of-science/is-logic-acquired-inductively/) | polish | 94 | 5 prompt sections are polish opportunities |
| 106 | Epistemology | [Case #6 – Insatiable Loops](../epistemology/case-6-insatiable-loops/) | polish | 94 | 3 prompt sections are polish opportunities |
| 107 | Humanistic Philosophies | [What is Existentialism?](../humanistic-philosophies/what-is-existentialism/) | polish | 94 | 3 prompt sections are polish opportunities |
| 108 | Introduction | [Miscellaneous Philosophers](../introduction/miscellaneous-philosophers/) | polish | 94 | 3 prompt sections are polish opportunities |
| 109 | Epistemology | [Decision-Making](../epistemology/decision-making/) | polish | 95 | 4 prompt sections are polish opportunities |
| 110 | Ethics | [Fictional Meta-Ethics Debate](../ethics/fictional-meta-ethics-debate/) | polish | 95 | 4 prompt sections are polish opportunities |
| 111 | Philosophical Inquiry | [Dangers: Strong Leaders](../philosophical-inquiry/dangers-strong-leaders/) | polish | 95 | 4 prompt sections are polish opportunities |
| 112 | Philosophical Inquiry | [Dangers: Co-opted Wonders](../philosophical-inquiry/dangers-co-opted-wonders/) | polish | 95 | 3 prompt sections are polish opportunities |
| 113 | Philosophical Inquiry | [Dangers: Half-Searches](../philosophical-inquiry/dangers-half-searches/) | polish | 95 | 3 prompt sections are polish opportunities |
| 114 | Ethics | [Ethics — Core Concepts](../ethics/ethics-core-concepts/) | polish | 96 | 5 prompt sections are polish opportunities |
| 115 | Philosophy of Language | [Gradient Concepts and Binary Terms](../philosophy-of-language/gradient-concepts-and-binary-terms/) | polish | 96 | 5 prompt sections are polish opportunities |
| 116 | Philosophy of Mind | [What is Consciousness?](../philosophy-of-mind/what-is-consciousness/) | polish | 96 | 5 prompt sections are polish opportunities |
| 117 | Epistemology | [Epistemology — Core Concepts](../epistemology/epistemology-core-concepts/) | polish | 96 | 4 prompt sections are polish opportunities |
| 118 | Epistemology | [Rationality Discussion](../epistemology/rationality-discussion/) | polish | 96 | 4 prompt sections are polish opportunities |
| 119 | Philosophy of Language | [Philosophy of Language — Core Concepts](../philosophy-of-language/core-concepts-philosophy-of-language/) | polish | 96 | 4 prompt sections are polish opportunities |
| 120 | Ethics | [Coherent Moral Systems](../ethics/coherent-moral-systems/) | polish | 97 | 5 prompt sections are polish opportunities |
| 121 | Philosophical Inquiry | [Selective Pressures on Ideologies](../philosophical-inquiry/selective-pressures-on-ideologies/) | polish | 97 | 5 prompt sections are polish opportunities |
| 122 | Epistemology | [Counterfactual Reasoning](../epistemology/counterfactual-reasoning/) | polish | 97 | 4 prompt sections are polish opportunities |
| 123 | Philosophical Inquiry | [Dangers: Narrative](../philosophical-inquiry/dangers-narrative/) | polish | 97 | 4 prompt sections are polish opportunities |
| 124 | Philosophical Inquiry | [Dangers: Ontological Buffet](../philosophical-inquiry/dangers-ontological-buffet/) | polish | 97 | 4 prompt sections are polish opportunities |
| 125 | Philosophical Inquiry | [Dangers: Unnuanced Conclusions](../philosophical-inquiry/dangers-unnuanced-conclusions/) | polish | 97 | 4 prompt sections are polish opportunities |
| 126 | Philosophical Inquiry | [Do I need a “worldview”?](../philosophical-inquiry/do-i-need-a-worldview/) | polish | 97 | 4 prompt sections are polish opportunities |
| 127 | Ethics | [Meta-Ethics](../ethics/meta-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 128 | Ethics | [Moral Systems: Required Elements](../ethics/moral-systems-required-elements/) | polish | 97 | 3 prompt sections are polish opportunities |
| 129 | Ethics | [What are Ethics?](../ethics/what-are-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 130 | Ethics | [“Is” vs “Ought”](../ethics/is-vs-ought/) | polish | 97 | 3 prompt sections are polish opportunities |
| 131 | Philosophical Inquiry | [How Minds are Changed](../philosophical-inquiry/how-minds-are-changed/) | polish | 97 | 3 prompt sections are polish opportunities |
| 132 | Epistemology | [Preponderance of Evidence?](../epistemology/preponderance-of-evidence/) | polish | 98 | 5 prompt sections are polish opportunities |
| 133 | Epistemology | [The Burden of Proof](../epistemology/the-burden-of-proof/) | polish | 98 | 5 prompt sections are polish opportunities |
| 134 | Philosophical Inquiry | [The Danger of “Resulting”](../philosophical-inquiry/the-danger-of-resulting/) | polish | 98 | 5 prompt sections are polish opportunities |
| 135 | Philosophy of Language | [What is Language?](../philosophy-of-language/what-is-language/) | polish | 98 | 5 prompt sections are polish opportunities |
| 136 | Epistemology | [Collapsing Epistemological Terms](../epistemology/collapsing-epistemological-terms/) | polish | 98 | 4 prompt sections are polish opportunities |
| 137 | Epistemology | [“Adequate” Evidence](../epistemology/adequate-evidence/) | polish | 98 | 4 prompt sections are polish opportunities |
| 138 | Metaphysics | [Jeremy Sherman on Emergence](../metaphysics/jeremy-sherman-on-emergence/) | polish | 98 | 4 prompt sections are polish opportunities |
| 139 | Philosophical Inquiry | [Conspiracies & Misunderstanding Human Nature](../philosophical-inquiry/conspiracies-misunderstanding-human-nature/) | polish | 98 | 4 prompt sections are polish opportunities |
| 140 | Philosophy of Mind | [Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/) | polish | 98 | 4 prompt sections are polish opportunities |
| 141 | Philosophy of Mind | [Subjective/Objective Free Will](../philosophy-of-mind/subjective-objective-free-will/) | polish | 98 | 4 prompt sections are polish opportunities |
| 142 | Rational Thought | [Training Data Bias](../rational-thought/training-data-bias/) | polish | 98 | 4 prompt sections are polish opportunities |
| 143 | Economics | [Wealth Creation](../economics/wealth-creation/) | polish | 98 | 3 prompt sections are polish opportunities |
| 144 | Epistemology | [Case #1 – Credence Complexity](../epistemology/case-1-credence-complexity/) | polish | 98 | 3 prompt sections are polish opportunities |
| 145 | Epistemology | [Case #4 – Recursive Credences](../epistemology/case-4-recursive-credences/) | polish | 98 | 3 prompt sections are polish opportunities |
| 146 | Humanistic Philosophies | [Accounting for X](../humanistic-philosophies/accounting-for-x/) | polish | 98 | 3 prompt sections are polish opportunities |
| 147 | Philosophical Inquiry | [Dangers: Carrot & Stick](../philosophical-inquiry/dangers-carrot-stick/) | polish | 98 | 3 prompt sections are polish opportunities |
| 148 | Philosophical Inquiry | [Dangers: The Notion of Fate](../philosophical-inquiry/dangers-the-notion-of-fate/) | polish | 98 | 3 prompt sections are polish opportunities |
| 149 | Philosophical Inquiry | [Testing Ideologies](../philosophical-inquiry/testing-ideologies/) | polish | 98 | 3 prompt sections are polish opportunities |
| 150 | Rational Thought | [Scope of Influence](../rational-thought/scope-of-influence/) | polish | 98 | 3 prompt sections are polish opportunities |
| 151 | Humanistic Philosophies | [Christian Apologetics](../humanistic-philosophies/christian-apologetics/) | polish | 99 | 4 prompt sections are polish opportunities |
| 152 | Rational Thought | [1 at 99.5% or 5 at 95%?](../rational-thought/1-at-99-5-or-5-at-95/) | polish | 99 | 4 prompt sections are polish opportunities |
| 153 | Philosophical Inquiry | [Dangers: Ideologies of Mystery](../philosophical-inquiry/dangers-ideologies-of-mystery/) | polish | 99 | 2 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 3, queue positions 154-203

- `polish` 100 [Economics / Economic Comparisons](../economics/economic-comparisons/)
- `polish` 100 [Economics / Economic Stability](../economics/economic-stability/)
- `polish` 100 [Economics / Minimum Wage](../economics/minimum-wage/)
- `polish` 100 [Economics / Schools of Economic Thought](../economics/schools-of-economic-thought/)
- `polish` 100 [Economics / Taxation](../economics/taxation/)
- `polish` 100 [Economics / What are Moral Hazards?](../economics/what-are-moral-hazards/)
- `polish` 100 [Economics / What is Economics?](../economics/what-is-economics/)
- `polish` 100 [Epistemology / Black Boxes & Epistemology](../epistemology/black-boxes-epistemology/)
- `polish` 100 [Epistemology / Core & Deep Rationality](../epistemology/core-deep-rationality/)
- `polish` 100 [Epistemology / Deduction: Utility and Issues](../epistemology/deduction-utility-and-issues/)

### Next +2: cycle 3, queue positions 204-253

- `polish` 100 [Philosophy of Science / Correlation and Causation](../philosophy-of-science/correlation-and-causation/)
- `polish` 100 [Philosophy of Science / Elements of Research Design](../philosophy-of-science/elements-of-research-design/)
- `polish` 100 [Philosophy of Science / Is History Science?](../philosophy-of-science/is-history-science/)
- `polish` 100 [Philosophy of Science / Research Design](../philosophy-of-science/research-design/)
- `polish` 100 [Philosophy of Science / Scientism & Faith](../philosophy-of-science/scientism-faith/)
- `polish` 100 [Philosophy of Science / The Power of Thought Experiments](../philosophy-of-science/the-power-of-thought-experiments/)
- `polish` 100 [Philosophy of Science / What is Induction?](../philosophy-of-science/what-is-induction/)
- `polish` 100 [Philosophy of Science / What is Parsimony?](../philosophy-of-science/what-is-parsimony/)
- `polish` 100 [Political Philosophy / Peaceful Revolutions](../political-philosophy/peaceful-revolutions/)
- `polish` 100 [Political Philosophy / Political Philosophy Basics](../political-philosophy/political-philosophy-basics/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 243
- Estimated batches per cycle: 7

- gap-fill: 82
- polish: 264
