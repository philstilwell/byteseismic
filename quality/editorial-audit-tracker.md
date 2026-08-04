# Byteseismic Editorial Audit Tracker

Generated: 2026-08-04
Batch size: 50 pages
Current cycle: 5
Current queue start: 107 of 346

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
| 107 | Rational Thought | [Regret Assessment](../rational-thought/regret-assessment/) | polish | 92 | 3 prompt sections are polish opportunities |
| 108 | Epistemology | [Belief/Evidence Graphic](../epistemology/belief-evidence-graphic/) | polish | 93 | 5 prompt sections are polish opportunities |
| 109 | Epistemology | [Pascal’s Wager](../epistemology/pascals-wager/) | polish | 93 | 5 prompt sections are polish opportunities |
| 110 | Epistemology | [The Inductive Paradox](../epistemology/the-inductive-paradox/) | polish | 93 | 4 prompt sections are polish opportunities |
| 111 | Humanistic Philosophies | [Christian Apologetics](../humanistic-philosophies/christian-apologetics/) | polish | 93 | 4 prompt sections are polish opportunities |
| 112 | Philosophical Inquiry | [Common Sense Blunders](../philosophical-inquiry/common-sense-blunders/) | polish | 93 | 3 prompt sections are polish opportunities |
| 113 | Philosophical Inquiry | [Packaged vs Eclectic Ideologies](../philosophical-inquiry/packaged-vs-eclectic-ideologies/) | polish | 93 | 3 prompt sections are polish opportunities |
| 114 | Philosophical Inquiry | [Selective Pressures on Ideologies](../philosophical-inquiry/selective-pressures-on-ideologies/) | polish | 94 | 5 prompt sections are polish opportunities |
| 115 | Philosophical Inquiry | [The Danger of “Resulting”](../philosophical-inquiry/the-danger-of-resulting/) | polish | 94 | 5 prompt sections are polish opportunities |
| 116 | Philosophy of Science | [Is Logic Acquired Inductively?](../philosophy-of-science/is-logic-acquired-inductively/) | polish | 94 | 5 prompt sections are polish opportunities |
| 117 | Epistemology | [Case #6 – Insatiable Loops](../epistemology/case-6-insatiable-loops/) | polish | 94 | 3 prompt sections are polish opportunities |
| 118 | Epistemology | [Decision-Making](../epistemology/decision-making/) | polish | 95 | 4 prompt sections are polish opportunities |
| 119 | Ethics | [Fictional Meta-Ethics Debate](../ethics/fictional-meta-ethics-debate/) | polish | 95 | 4 prompt sections are polish opportunities |
| 120 | Philosophical Inquiry | [Dangers: Strong Leaders](../philosophical-inquiry/dangers-strong-leaders/) | polish | 95 | 4 prompt sections are polish opportunities |
| 121 | Philosophical Inquiry | [Dangers: Co-opted Wonders](../philosophical-inquiry/dangers-co-opted-wonders/) | polish | 95 | 3 prompt sections are polish opportunities |
| 122 | Philosophical Inquiry | [Dangers: Half-Searches](../philosophical-inquiry/dangers-half-searches/) | polish | 95 | 3 prompt sections are polish opportunities |
| 123 | Ethics | [Ethics — Core Concepts](../ethics/ethics-core-concepts/) | polish | 96 | 5 prompt sections are polish opportunities |
| 124 | Philosophy of Language | [Gradient Concepts and Binary Terms](../philosophy-of-language/gradient-concepts-and-binary-terms/) | polish | 96 | 5 prompt sections are polish opportunities |
| 125 | Epistemology | [Epistemology — Core Concepts](../epistemology/epistemology-core-concepts/) | polish | 96 | 4 prompt sections are polish opportunities |
| 126 | Philosophical Inquiry | [Do I need a “worldview”?](../philosophical-inquiry/do-i-need-a-worldview/) | polish | 96 | 4 prompt sections are polish opportunities |
| 127 | Philosophy of Language | [Philosophy of Language — Core Concepts](../philosophy-of-language/core-concepts-philosophy-of-language/) | polish | 96 | 4 prompt sections are polish opportunities |
| 128 | Rational Thought | [Training Data Bias](../rational-thought/training-data-bias/) | polish | 96 | 4 prompt sections are polish opportunities |
| 129 | Ethics | [Coherent Moral Systems](../ethics/coherent-moral-systems/) | polish | 97 | 5 prompt sections are polish opportunities |
| 130 | Epistemology | [Counterfactual Reasoning](../epistemology/counterfactual-reasoning/) | polish | 97 | 4 prompt sections are polish opportunities |
| 131 | Philosophical Inquiry | [Dangers: Narrative](../philosophical-inquiry/dangers-narrative/) | polish | 97 | 4 prompt sections are polish opportunities |
| 132 | Philosophical Inquiry | [Dangers: Ontological Buffet](../philosophical-inquiry/dangers-ontological-buffet/) | polish | 97 | 4 prompt sections are polish opportunities |
| 133 | Philosophical Inquiry | [Dangers: Unnuanced Conclusions](../philosophical-inquiry/dangers-unnuanced-conclusions/) | polish | 97 | 4 prompt sections are polish opportunities |
| 134 | Ethics | [Meta-Ethics](../ethics/meta-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 135 | Ethics | [Moral Systems: Required Elements](../ethics/moral-systems-required-elements/) | polish | 97 | 3 prompt sections are polish opportunities |
| 136 | Ethics | [What are Ethics?](../ethics/what-are-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 137 | Ethics | [“Is” vs “Ought”](../ethics/is-vs-ought/) | polish | 97 | 3 prompt sections are polish opportunities |
| 138 | Philosophical Inquiry | [How Minds are Changed](../philosophical-inquiry/how-minds-are-changed/) | polish | 97 | 3 prompt sections are polish opportunities |
| 139 | Epistemology | [Preponderance of Evidence?](../epistemology/preponderance-of-evidence/) | polish | 98 | 5 prompt sections are polish opportunities |
| 140 | Philosophy of Language | [What is Language?](../philosophy-of-language/what-is-language/) | polish | 98 | 5 prompt sections are polish opportunities |
| 141 | Epistemology | [Collapsing Epistemological Terms](../epistemology/collapsing-epistemological-terms/) | polish | 98 | 4 prompt sections are polish opportunities |
| 142 | Philosophical Inquiry | [Conspiracies & Misunderstanding Human Nature](../philosophical-inquiry/conspiracies-misunderstanding-human-nature/) | polish | 98 | 4 prompt sections are polish opportunities |
| 143 | Philosophy of Mind | [Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/) | polish | 98 | 4 prompt sections are polish opportunities |
| 144 | Philosophy of Mind | [Subjective/Objective Free Will](../philosophy-of-mind/subjective-objective-free-will/) | polish | 98 | 4 prompt sections are polish opportunities |
| 145 | Economics | [Wealth Creation](../economics/wealth-creation/) | polish | 98 | 3 prompt sections are polish opportunities |
| 146 | Epistemology | [Case #1 – Credence Complexity](../epistemology/case-1-credence-complexity/) | polish | 98 | 3 prompt sections are polish opportunities |
| 147 | Epistemology | [Case #4 – Recursive Credences](../epistemology/case-4-recursive-credences/) | polish | 98 | 3 prompt sections are polish opportunities |
| 148 | Humanistic Philosophies | [Accounting for X](../humanistic-philosophies/accounting-for-x/) | polish | 98 | 3 prompt sections are polish opportunities |
| 149 | Philosophical Inquiry | [Dangers: Carrot & Stick](../philosophical-inquiry/dangers-carrot-stick/) | polish | 98 | 3 prompt sections are polish opportunities |
| 150 | Philosophical Inquiry | [Dangers: The Notion of Fate](../philosophical-inquiry/dangers-the-notion-of-fate/) | polish | 98 | 3 prompt sections are polish opportunities |
| 151 | Philosophical Inquiry | [Testing Ideologies](../philosophical-inquiry/testing-ideologies/) | polish | 98 | 3 prompt sections are polish opportunities |
| 152 | Rational Thought | [Scope of Influence](../rational-thought/scope-of-influence/) | polish | 98 | 3 prompt sections are polish opportunities |
| 153 | Philosophical Inquiry | [Dangers: Ideologies of Mystery](../philosophical-inquiry/dangers-ideologies-of-mystery/) | polish | 99 | 2 prompt sections are polish opportunities |
| 154 | Economics | [Economic Comparisons](../economics/economic-comparisons/) | polish | 100 | 5 prompt sections are polish opportunities |
| 155 | Economics | [Economic Stability](../economics/economic-stability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 156 | Economics | [Minimum Wage](../economics/minimum-wage/) | polish | 100 | 5 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 5, queue positions 157-206

- `polish` 100 [Economics / Schools of Economic Thought](../economics/schools-of-economic-thought/)
- `polish` 100 [Economics / Taxation](../economics/taxation/)
- `polish` 100 [Economics / What are Moral Hazards?](../economics/what-are-moral-hazards/)
- `polish` 100 [Economics / What is Economics?](../economics/what-is-economics/)
- `polish` 100 [Epistemology / Black Boxes & Epistemology](../epistemology/black-boxes-epistemology/)
- `polish` 100 [Epistemology / Core & Deep Rationality](../epistemology/core-deep-rationality/)
- `polish` 100 [Epistemology / Deduction: Utility and Issues](../epistemology/deduction-utility-and-issues/)
- `polish` 100 [Epistemology / Extraordinary Claims](../epistemology/extraordinary-claims/)
- `polish` 100 [Epistemology / Induction: Utility and Issues](../epistemology/induction-utility-and-issues/)
- `polish` 100 [Epistemology / Pragmatic Considerations vs Epistemic Assessments](../epistemology/pragmatic-considerations-vs-epistemic-assessments/)

### Next +2: cycle 5, queue positions 207-256

- `polish` 100 [Philosophy of Science / Research Design](../philosophy-of-science/research-design/)
- `polish` 100 [Philosophy of Science / Scientism & Faith](../philosophy-of-science/scientism-faith/)
- `polish` 100 [Philosophy of Science / The Power of Thought Experiments](../philosophy-of-science/the-power-of-thought-experiments/)
- `polish` 100 [Philosophy of Science / What is Induction?](../philosophy-of-science/what-is-induction/)
- `polish` 100 [Philosophy of Science / What is Parsimony?](../philosophy-of-science/what-is-parsimony/)
- `polish` 100 [Political Philosophy / Peaceful Revolutions](../political-philosophy/peaceful-revolutions/)
- `polish` 100 [Political Philosophy / Political Philosophy Basics](../political-philosophy/political-philosophy-basics/)
- `polish` 100 [Political Philosophy / Political Philosophy – Core Concepts](../political-philosophy/political-philosophy-core-concepts/)
- `polish` 100 [Rational Thought / AI “Logic” & “Intelligence”](../rational-thought/ai-logic-intelligence/)
- `polish` 100 [Rational Thought / Case #2 – Autism](../rational-thought/case-2-autism/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 240
- Estimated batches per cycle: 7

- gap-fill: 66
- polish: 256
- review: 24
