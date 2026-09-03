# Byteseismic Editorial Audit Tracker

Generated: 2026-09-03
Batch size: 50 pages
Current cycle: 7
Current queue start: 101 of 346

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
| 101 | Philosophers | [Philosopher Club Membership](../philosophers/philosopher-club-membership/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 102 | Philosophers | [Philosophers or Philosophy?](../philosophers/philosophers-or-philosophy/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 103 | Philosophers | [Philosophical Gradients](../philosophers/philosophical-gradients/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 104 | Philosophical Inquiry | [Dangers: Untestable Ideologies](../philosophical-inquiry/dangers-untestable-ideologies/) | polish | 86 | 3 prompt sections are polish opportunities |
| 105 | Philosophy of Science | [Observable Regularities](../philosophy-of-science/observable-regularity/) | polish | 86 | 3 prompt sections are polish opportunities |
| 106 | Epistemology | [Abduction: Utility and Issues](../epistemology/abduction-utility-and-issues/) | polish | 88 | 5 prompt sections are polish opportunities |
| 107 | Ethics | [Intrinsic Human Value](../ethics/intrinsic-human-value/) | polish | 89 | 5 prompt sections are polish opportunities |
| 108 | Philosophy of Language | [What is Etymology?](../philosophy-of-language/what-is-etymology/) | polish | 89 | 5 prompt sections are polish opportunities |
| 109 | Epistemology | [Avoiding Single-Cause Dogmatism](../epistemology/avoiding-single-cause-dogmatism/) | polish | 89 | 4 prompt sections are polish opportunities |
| 110 | Epistemology | [Collapsing Epistemological Terms](../epistemology/collapsing-epistemological-terms/) | polish | 89 | 4 prompt sections are polish opportunities |
| 111 | Ethics | [⌁ Finite Agency, Moral Demand, and Happiness](../ethics/finite-agency-moral-demand-and-happiness/) | polish | 89 | 4 prompt sections are polish opportunities |
| 112 | Rational Thought | [Perverse Incentives](../rational-thought/perverse-incentives/) | polish | 89 | 4 prompt sections are polish opportunities |
| 113 | Epistemology | [Doxastic Voluntarism](../epistemology/doxastic-voluntarism/) | polish | 89 | 3 prompt sections are polish opportunities |
| 114 | Epistemology | [The Burden of Proof](../epistemology/the-burden-of-proof/) | polish | 90 | 5 prompt sections are polish opportunities |
| 115 | Humanistic Philosophies | [Can Humans Change?](../humanistic-philosophies/can-humans-change/) | polish | 90 | 5 prompt sections are polish opportunities |
| 116 | Humanistic Philosophies | [Do Humans have an Essence?](../humanistic-philosophies/do-humans-have-an-essence/) | polish | 90 | 4 prompt sections are polish opportunities |
| 117 | Epistemology | [Epistemological Case Studies](../epistemology/epistemological-case-studies/) | polish | 91 | 3 prompt sections are polish opportunities |
| 118 | Ethics | [Moral Black Boxes](../ethics/moral-black-boxes/) | polish | 91 | 3 prompt sections are polish opportunities |
| 119 | Economics | [Economics – Core Concepts](../economics/economics-core-concepts/) | polish | 92 | 5 prompt sections are polish opportunities |
| 120 | Miscellany | [Complexity Theory](../miscellany/complexity-theory/) | polish | 92 | 4 prompt sections are polish opportunities |
| 121 | Philosophical Inquiry | [Personal Truth?](../philosophical-inquiry/personal-truth/) | polish | 92 | 4 prompt sections are polish opportunities |
| 122 | Rational Thought | [Regret Assessment](../rational-thought/regret-assessment/) | polish | 92 | 3 prompt sections are polish opportunities |
| 123 | Epistemology | [Belief/Evidence Graphic](../epistemology/belief-evidence-graphic/) | polish | 93 | 5 prompt sections are polish opportunities |
| 124 | Epistemology | [Pascal’s Wager](../epistemology/pascals-wager/) | polish | 93 | 5 prompt sections are polish opportunities |
| 125 | Epistemology | [The Inductive Paradox](../epistemology/the-inductive-paradox/) | polish | 93 | 4 prompt sections are polish opportunities |
| 126 | Humanistic Philosophies | [Christian Apologetics](../humanistic-philosophies/christian-apologetics/) | polish | 93 | 4 prompt sections are polish opportunities |
| 127 | Philosophical Inquiry | [Common Sense Blunders](../philosophical-inquiry/common-sense-blunders/) | polish | 93 | 3 prompt sections are polish opportunities |
| 128 | Philosophical Inquiry | [Packaged vs Eclectic Ideologies](../philosophical-inquiry/packaged-vs-eclectic-ideologies/) | polish | 93 | 3 prompt sections are polish opportunities |
| 129 | Philosophical Inquiry | [Selective Pressures on Ideologies](../philosophical-inquiry/selective-pressures-on-ideologies/) | polish | 94 | 5 prompt sections are polish opportunities |
| 130 | Philosophical Inquiry | [The Danger of “Resulting”](../philosophical-inquiry/the-danger-of-resulting/) | polish | 94 | 5 prompt sections are polish opportunities |
| 131 | Philosophy of Science | [Is Logic Acquired Inductively?](../philosophy-of-science/is-logic-acquired-inductively/) | polish | 94 | 5 prompt sections are polish opportunities |
| 132 | Epistemology | [Case #6 – Insatiable Loops](../epistemology/case-6-insatiable-loops/) | polish | 94 | 3 prompt sections are polish opportunities |
| 133 | Ethics | [Fictional Meta-Ethics Debate](../ethics/fictional-meta-ethics-debate/) | polish | 95 | 5 prompt sections are polish opportunities |
| 134 | Epistemology | [Decision-Making](../epistemology/decision-making/) | polish | 95 | 4 prompt sections are polish opportunities |
| 135 | Philosophical Inquiry | [Dangers: Strong Leaders](../philosophical-inquiry/dangers-strong-leaders/) | polish | 95 | 4 prompt sections are polish opportunities |
| 136 | Philosophical Inquiry | [Dangers: Co-opted Wonders](../philosophical-inquiry/dangers-co-opted-wonders/) | polish | 95 | 3 prompt sections are polish opportunities |
| 137 | Philosophical Inquiry | [Dangers: Half-Searches](../philosophical-inquiry/dangers-half-searches/) | polish | 95 | 3 prompt sections are polish opportunities |
| 138 | Ethics | [Ethics — Core Concepts](../ethics/ethics-core-concepts/) | polish | 96 | 5 prompt sections are polish opportunities |
| 139 | Philosophy of Language | [Gradient Concepts and Binary Terms](../philosophy-of-language/gradient-concepts-and-binary-terms/) | polish | 96 | 5 prompt sections are polish opportunities |
| 140 | Epistemology | [Epistemology — Core Concepts](../epistemology/epistemology-core-concepts/) | polish | 96 | 4 prompt sections are polish opportunities |
| 141 | Philosophical Inquiry | [Do I need a “worldview”?](../philosophical-inquiry/do-i-need-a-worldview/) | polish | 96 | 4 prompt sections are polish opportunities |
| 142 | Philosophy of Language | [Philosophy of Language — Core Concepts](../philosophy-of-language/core-concepts-philosophy-of-language/) | polish | 96 | 4 prompt sections are polish opportunities |
| 143 | Rational Thought | [Training Data Bias](../rational-thought/training-data-bias/) | polish | 96 | 4 prompt sections are polish opportunities |
| 144 | Ethics | [Coherent Moral Systems](../ethics/coherent-moral-systems/) | polish | 97 | 5 prompt sections are polish opportunities |
| 145 | Epistemology | [Counterfactual Reasoning](../epistemology/counterfactual-reasoning/) | polish | 97 | 4 prompt sections are polish opportunities |
| 146 | Philosophical Inquiry | [Dangers: Narrative](../philosophical-inquiry/dangers-narrative/) | polish | 97 | 4 prompt sections are polish opportunities |
| 147 | Philosophical Inquiry | [Dangers: Ontological Buffet](../philosophical-inquiry/dangers-ontological-buffet/) | polish | 97 | 4 prompt sections are polish opportunities |
| 148 | Philosophical Inquiry | [Dangers: Unnuanced Conclusions](../philosophical-inquiry/dangers-unnuanced-conclusions/) | polish | 97 | 4 prompt sections are polish opportunities |
| 149 | Ethics | [Meta-Ethics](../ethics/meta-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 150 | Ethics | [Moral Systems: Required Elements](../ethics/moral-systems-required-elements/) | polish | 97 | 3 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 7, queue positions 151-200

- `polish` 97 [Ethics / What are Ethics?](../ethics/what-are-ethics/)
- `polish` 97 [Ethics / “Is” vs “Ought”](../ethics/is-vs-ought/)
- `polish` 97 [Philosophical Inquiry / How Minds are Changed](../philosophical-inquiry/how-minds-are-changed/)
- `polish` 98 [Economics / Economic Comparisons](../economics/economic-comparisons/)
- `polish` 98 [Epistemology / Preponderance of Evidence?](../epistemology/preponderance-of-evidence/)
- `polish` 98 [Philosophy of Language / What is Language?](../philosophy-of-language/what-is-language/)
- `polish` 98 [Miscellany / Domains of Aesthetics](../miscellany/domains-of-aesthetics/)
- `polish` 98 [Philosophical Inquiry / Conspiracies & Misunderstanding Human Nature](../philosophical-inquiry/conspiracies-misunderstanding-human-nature/)
- `polish` 98 [Philosophy of Mind / Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/)
- `polish` 98 [Philosophy of Mind / Subjective/Objective Free Will](../philosophy-of-mind/subjective-objective-free-will/)

### Next +2: cycle 7, queue positions 201-250

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

- Tracked pages: 346
- Pages remaining in current cycle: 246
- Estimated batches per cycle: 7

- gap-fill: 63
- polish: 243
- review: 40
