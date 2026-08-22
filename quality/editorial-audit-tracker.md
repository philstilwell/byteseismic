# Byteseismic Editorial Audit Tracker

Generated: 2026-08-22
Batch size: 50 pages
Current cycle: 6
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
| 99 | Philosophers | [Xunzi](../philosophers/xunzi/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 100 | Philosophers | [Zhuangzi](../philosophers/zhuangzi/) | gap-fill | 100 | 4 prompt sections need gap fill |
| 101 | Philosophers | [Aquinas’ Five Ways](../philosophers/aquinas-five-ways/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 102 | Philosophers | [Philosopher Club Membership](../philosophers/philosopher-club-membership/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 103 | Philosophers | [Philosophers or Philosophy?](../philosophers/philosophers-or-philosophy/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 104 | Philosophers | [Philosophical Gradients](../philosophers/philosophical-gradients/) | gap-fill | 100 | 3 prompt sections need gap fill |
| 105 | Philosophical Inquiry | [Dangers: Untestable Ideologies](../philosophical-inquiry/dangers-untestable-ideologies/) | polish | 86 | 3 prompt sections are polish opportunities |
| 106 | Philosophy of Science | [Observable Regularities](../philosophy-of-science/observable-regularity/) | polish | 86 | 3 prompt sections are polish opportunities |
| 107 | Epistemology | [Abduction: Utility and Issues](../epistemology/abduction-utility-and-issues/) | polish | 88 | 5 prompt sections are polish opportunities |
| 108 | Ethics | [Intrinsic Human Value](../ethics/intrinsic-human-value/) | polish | 89 | 5 prompt sections are polish opportunities |
| 109 | Philosophy of Language | [What is Etymology?](../philosophy-of-language/what-is-etymology/) | polish | 89 | 5 prompt sections are polish opportunities |
| 110 | Epistemology | [Avoiding Single-Cause Dogmatism](../epistemology/avoiding-single-cause-dogmatism/) | polish | 89 | 4 prompt sections are polish opportunities |
| 112 | Ethics | [⌁ Finite Agency, Moral Demand, and Happiness](../ethics/finite-agency-moral-demand-and-happiness/) | polish | 89 | 4 prompt sections are polish opportunities |
| 113 | Rational Thought | [Perverse Incentives](../rational-thought/perverse-incentives/) | polish | 89 | 4 prompt sections are polish opportunities |
| 114 | Epistemology | [Doxastic Voluntarism](../epistemology/doxastic-voluntarism/) | polish | 89 | 3 prompt sections are polish opportunities |
| 115 | Epistemology | [The Burden of Proof](../epistemology/the-burden-of-proof/) | polish | 90 | 5 prompt sections are polish opportunities |
| 116 | Humanistic Philosophies | [Can Humans Change?](../humanistic-philosophies/can-humans-change/) | polish | 90 | 5 prompt sections are polish opportunities |
| 117 | Humanistic Philosophies | [Do Humans have an Essence?](../humanistic-philosophies/do-humans-have-an-essence/) | polish | 90 | 4 prompt sections are polish opportunities |
| 118 | Epistemology | [Epistemological Case Studies](../epistemology/epistemological-case-studies/) | polish | 91 | 3 prompt sections are polish opportunities |
| 119 | Ethics | [Moral Black Boxes](../ethics/moral-black-boxes/) | polish | 91 | 3 prompt sections are polish opportunities |
| 120 | Economics | [Economics – Core Concepts](../economics/economics-core-concepts/) | polish | 92 | 5 prompt sections are polish opportunities |
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
| 134 | Epistemology | [Decision-Making](../epistemology/decision-making/) | polish | 95 | 4 prompt sections are polish opportunities |
| 135 | Philosophical Inquiry | [Dangers: Strong Leaders](../philosophical-inquiry/dangers-strong-leaders/) | polish | 95 | 4 prompt sections are polish opportunities |
| 136 | Philosophical Inquiry | [Dangers: Co-opted Wonders](../philosophical-inquiry/dangers-co-opted-wonders/) | polish | 95 | 3 prompt sections are polish opportunities |
| 137 | Philosophical Inquiry | [Dangers: Half-Searches](../philosophical-inquiry/dangers-half-searches/) | polish | 95 | 3 prompt sections are polish opportunities |
| 138 | Ethics | [Ethics — Core Concepts](../ethics/ethics-core-concepts/) | polish | 96 | 5 prompt sections are polish opportunities |
| 139 | Philosophy of Language | [Gradient Concepts and Binary Terms](../philosophy-of-language/gradient-concepts-and-binary-terms/) | polish | 96 | 5 prompt sections are polish opportunities |
| 140 | Epistemology | [Epistemology — Core Concepts](../epistemology/epistemology-core-concepts/) | polish | 96 | 4 prompt sections are polish opportunities |
| 141 | Philosophical Inquiry | [Do I need a “worldview”?](../philosophical-inquiry/do-i-need-a-worldview/) | polish | 96 | 4 prompt sections are polish opportunities |
| 142 | Philosophy of Language | [Philosophy of Language — Core Concepts](../philosophy-of-language/core-concepts-philosophy-of-language/) | polish | 96 | 4 prompt sections are polish opportunities |
| 143 | Ethics | [Coherent Moral Systems](../ethics/coherent-moral-systems/) | polish | 97 | 5 prompt sections are polish opportunities |
| 144 | Epistemology | [Counterfactual Reasoning](../epistemology/counterfactual-reasoning/) | polish | 97 | 4 prompt sections are polish opportunities |
| 145 | Philosophical Inquiry | [Dangers: Narrative](../philosophical-inquiry/dangers-narrative/) | polish | 97 | 4 prompt sections are polish opportunities |
| 146 | Philosophical Inquiry | [Dangers: Ontological Buffet](../philosophical-inquiry/dangers-ontological-buffet/) | polish | 97 | 4 prompt sections are polish opportunities |
| 147 | Philosophical Inquiry | [Dangers: Unnuanced Conclusions](../philosophical-inquiry/dangers-unnuanced-conclusions/) | polish | 97 | 4 prompt sections are polish opportunities |
| 148 | Ethics | [Meta-Ethics](../ethics/meta-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 149 | Ethics | [Moral Systems: Required Elements](../ethics/moral-systems-required-elements/) | polish | 97 | 3 prompt sections are polish opportunities |
| 150 | Ethics | [What are Ethics?](../ethics/what-are-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 6, queue positions 151-200

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

### Next +2: cycle 6, queue positions 201-250

- `polish` 100 [Philosophy of Mind / Philosophy of Mind Basics](../philosophy-of-mind/philosophy-of-mind-basics/)
- `polish` 100 [Philosophy of Mind / Where are our Thoughts?](../philosophy-of-mind/where-are-our-thoughts/)
- `polish` 100 [Philosophy of Science / Asymmetric Counterfactuals](../philosophy-of-science/asymmetric-counterfactuals/)
- `polish` 100 [Philosophy of Science / Correlation and Causation](../philosophy-of-science/correlation-and-causation/)
- `polish` 100 [Philosophy of Science / Elements of Research Design](../philosophy-of-science/elements-of-research-design/)
- `polish` 100 [Philosophy of Science / Is History Science?](../philosophy-of-science/is-history-science/)
- `polish` 100 [Philosophy of Science / Research Design](../philosophy-of-science/research-design/)
- `polish` 100 [Philosophy of Science / Scientism & Faith](../philosophy-of-science/scientism-faith/)
- `polish` 100 [Philosophy of Science / The Power of Thought Experiments](../philosophy-of-science/the-power-of-thought-experiments/)
- `polish` 100 [Philosophy of Science / What is Induction?](../philosophy-of-science/what-is-induction/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 246
- Estimated batches per cycle: 7

- gap-fill: 64
- polish: 242
- review: 40
