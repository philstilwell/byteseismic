# Byteseismic Editorial Audit Tracker

Generated: 2026-06-28
Batch size: 50 pages
Current cycle: 2
Current queue start: 151 of 528

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
| 151 | Epistemology | [Logic](../epistemology/logic/) | polish | 90 | 3 prompt sections are polish opportunities |
| 152 | Epistemology | [Epistemological Case Studies](../epistemology/epistemological-case-studies/) | polish | 91 | 3 prompt sections are polish opportunities |
| 153 | Ethics | [Moral Black Boxes](../ethics/moral-black-boxes/) | polish | 91 | 3 prompt sections are polish opportunities |
| 154 | Ethics | [Morality & Human Rights](../ethics/morality-human-rights/) | polish | 91 | 3 prompt sections are polish opportunities |
| 155 | Economics | [Economics – Core Concepts](../economics/economics-core-concepts/) | polish | 92 | 5 prompt sections are polish opportunities |
| 156 | Philosophical Inquiry | [Personal Truth?](../philosophical-inquiry/personal-truth/) | polish | 92 | 4 prompt sections are polish opportunities |
| 157 | Humanistic Philosophies | [Anthropomorphized Gods](../humanistic-philosophies/anthropomorphized-gods/) | polish | 92 | 3 prompt sections are polish opportunities |
| 158 | Rational Thought | [Regret Assessment](../rational-thought/regret-assessment/) | polish | 92 | 3 prompt sections are polish opportunities |
| 159 | Epistemology | [Belief/Evidence Graphic](../epistemology/belief-evidence-graphic/) | polish | 93 | 5 prompt sections are polish opportunities |
| 160 | Epistemology | [Pascal’s Wager](../epistemology/pascals-wager/) | polish | 93 | 5 prompt sections are polish opportunities |
| 161 | Epistemology | [The Inductive Paradox](../epistemology/the-inductive-paradox/) | polish | 93 | 4 prompt sections are polish opportunities |
| 162 | Epistemology | [I Don’t Know](../epistemology/i-dont-know/) | polish | 93 | 3 prompt sections are polish opportunities |
| 163 | Philosophical Inquiry | [Common Sense Blunders](../philosophical-inquiry/common-sense-blunders/) | polish | 93 | 3 prompt sections are polish opportunities |
| 164 | Philosophical Inquiry | [Packaged vs Eclectic Ideologies](../philosophical-inquiry/packaged-vs-eclectic-ideologies/) | polish | 93 | 3 prompt sections are polish opportunities |
| 165 | Philosophy of Mind | [Elitzur on Consciousness](../philosophy-of-mind/elitzur-on-consciousness/) | polish | 93 | 2 prompt sections are polish opportunities |
| 166 | Philosophy of Science | [Is Logic Acquired Inductively?](../philosophy-of-science/is-logic-acquired-inductively/) | polish | 94 | 5 prompt sections are polish opportunities |
| 167 | Epistemology | [Case #6 – Insatiable Loops](../epistemology/case-6-insatiable-loops/) | polish | 94 | 3 prompt sections are polish opportunities |
| 168 | Humanistic Philosophies | [What is Existentialism?](../humanistic-philosophies/what-is-existentialism/) | polish | 94 | 3 prompt sections are polish opportunities |
| 169 | Introduction | [Miscellaneous Philosophers](../introduction/miscellaneous-philosophers/) | polish | 94 | 3 prompt sections are polish opportunities |
| 170 | Epistemology | [Decision-Making](../epistemology/decision-making/) | polish | 95 | 4 prompt sections are polish opportunities |
| 171 | Ethics | [Fictional Meta-Ethics Debate](../ethics/fictional-meta-ethics-debate/) | polish | 95 | 4 prompt sections are polish opportunities |
| 172 | Philosophical Inquiry | [Dangers: Strong Leaders](../philosophical-inquiry/dangers-strong-leaders/) | polish | 95 | 4 prompt sections are polish opportunities |
| 173 | Philosophical Inquiry | [Dangers: Co-opted Wonders](../philosophical-inquiry/dangers-co-opted-wonders/) | polish | 95 | 3 prompt sections are polish opportunities |
| 174 | Philosophical Inquiry | [Dangers: Half-Searches](../philosophical-inquiry/dangers-half-searches/) | polish | 95 | 3 prompt sections are polish opportunities |
| 175 | Ethics | [Ethics — Core Concepts](../ethics/ethics-core-concepts/) | polish | 96 | 5 prompt sections are polish opportunities |
| 176 | Philosophy of Language | [Gradient Concepts and Binary Terms](../philosophy-of-language/gradient-concepts-and-binary-terms/) | polish | 96 | 5 prompt sections are polish opportunities |
| 177 | Philosophy of Mind | [What is Consciousness?](../philosophy-of-mind/what-is-consciousness/) | polish | 96 | 5 prompt sections are polish opportunities |
| 178 | Epistemology | [Epistemology — Core Concepts](../epistemology/epistemology-core-concepts/) | polish | 96 | 4 prompt sections are polish opportunities |
| 179 | Epistemology | [Rationality Discussion](../epistemology/rationality-discussion/) | polish | 96 | 4 prompt sections are polish opportunities |
| 180 | Philosophy of Language | [Philosophy of Language — Core Concepts](../philosophy-of-language/core-concepts-philosophy-of-language/) | polish | 96 | 4 prompt sections are polish opportunities |
| 181 | Ethics | [Coherent Moral Systems](../ethics/coherent-moral-systems/) | polish | 97 | 5 prompt sections are polish opportunities |
| 182 | Philosophical Inquiry | [Selective Pressures on Ideologies](../philosophical-inquiry/selective-pressures-on-ideologies/) | polish | 97 | 5 prompt sections are polish opportunities |
| 183 | Epistemology | [Counterfactual Reasoning](../epistemology/counterfactual-reasoning/) | polish | 97 | 4 prompt sections are polish opportunities |
| 184 | Philosophical Inquiry | [Dangers: Narrative](../philosophical-inquiry/dangers-narrative/) | polish | 97 | 4 prompt sections are polish opportunities |
| 185 | Philosophical Inquiry | [Dangers: Ontological Buffet](../philosophical-inquiry/dangers-ontological-buffet/) | polish | 97 | 4 prompt sections are polish opportunities |
| 186 | Philosophical Inquiry | [Dangers: Unnuanced Conclusions](../philosophical-inquiry/dangers-unnuanced-conclusions/) | polish | 97 | 4 prompt sections are polish opportunities |
| 187 | Philosophical Inquiry | [Do I need a “worldview”?](../philosophical-inquiry/do-i-need-a-worldview/) | polish | 97 | 4 prompt sections are polish opportunities |
| 188 | Epistemology | [Shades of Certainty](../epistemology/shades-of-certainty/) | polish | 97 | 3 prompt sections are polish opportunities |
| 189 | Ethics | [Meta-Ethics](../ethics/meta-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 190 | Ethics | [Moral Systems: Required Elements](../ethics/moral-systems-required-elements/) | polish | 97 | 3 prompt sections are polish opportunities |
| 191 | Ethics | [What are Ethics?](../ethics/what-are-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 192 | Ethics | [“Is” vs “Ought”](../ethics/is-vs-ought/) | polish | 97 | 3 prompt sections are polish opportunities |
| 193 | Philosophical Inquiry | [How Minds are Changed](../philosophical-inquiry/how-minds-are-changed/) | polish | 97 | 3 prompt sections are polish opportunities |
| 194 | Epistemology | [Preponderance of Evidence?](../epistemology/preponderance-of-evidence/) | polish | 98 | 5 prompt sections are polish opportunities |
| 195 | Epistemology | [The Burden of Proof](../epistemology/the-burden-of-proof/) | polish | 98 | 5 prompt sections are polish opportunities |
| 196 | Philosophical Inquiry | [The Danger of “Resulting”](../philosophical-inquiry/the-danger-of-resulting/) | polish | 98 | 5 prompt sections are polish opportunities |
| 197 | Philosophy of Language | [What is Language?](../philosophy-of-language/what-is-language/) | polish | 98 | 5 prompt sections are polish opportunities |
| 198 | Epistemology | [Collapsing Epistemological Terms](../epistemology/collapsing-epistemological-terms/) | polish | 98 | 4 prompt sections are polish opportunities |
| 199 | Epistemology | [“Adequate” Evidence](../epistemology/adequate-evidence/) | polish | 98 | 4 prompt sections are polish opportunities |
| 200 | Metaphysics | [Jeremy Sherman on Emergence](../metaphysics/jeremy-sherman-on-emergence/) | polish | 98 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 2, queue positions 201-250

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

### Next +2: cycle 2, queue positions 251-300

- `polish` 100 [Metaphysics / Categories of Nihilism](../metaphysics/categories-of-nihilism/)
- `polish` 100 [Metaphysics / Dualism vs Materialism](../metaphysics/dualismvsmaterialism/)
- `polish` 100 [Metaphysics / Establishing the Spiritual](../metaphysics/establishing-the-spiritual/)
- `polish` 100 [Miscellany / COVID19 & Science](../miscellany/covid-19-science/)
- `polish` 100 [Philosophical Inquiry / Dangers: Ideologies of Emotion](../philosophical-inquiry/dangers-ideologies-of-emotion/)
- `polish` 100 [Philosophical Inquiry / Inscrutability Case Studies](../philosophical-inquiry/inscrutability-case-studies/)
- `polish` 100 [Philosophical Inquiry / Seeker Scenarios](../philosophical-inquiry/seeker-scenarios/)
- `polish` 100 [Philosophy of AI / Feedback Loops](../philosophy-of-ai/feedback-loops/)
- `polish` 100 [Philosophy of AI / Human Reaction to AI](../philosophy-of-ai/human-reaction-to-ai/)
- `polish` 100 [Philosophy of AI / Philosophy of AI – Core Concepts](../philosophy-of-ai/philosophy-of-ai-core-concepts/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 378
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 396
- review: 46
