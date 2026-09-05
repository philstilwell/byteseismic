# Byteseismic Editorial Audit Tracker

Generated: 2026-09-05
Batch size: 50 pages
Current cycle: 7
Current queue start: 201 of 346

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
| 201 | Metaphysics | [Categories of Nihilism](../metaphysics/categories-of-nihilism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 202 | Metaphysics | [Dualism vs Materialism](../metaphysics/dualismvsmaterialism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 203 | Metaphysics | [Establishing the Spiritual](../metaphysics/establishing-the-spiritual/) | polish | 100 | 5 prompt sections are polish opportunities |
| 204 | Miscellany | [COVID19 & Science](../miscellany/covid-19-science/) | polish | 100 | 5 prompt sections are polish opportunities |
| 205 | Philosophical Inquiry | [Dangers: Ideologies of Emotion](../philosophical-inquiry/dangers-ideologies-of-emotion/) | polish | 100 | 5 prompt sections are polish opportunities |
| 206 | Philosophical Inquiry | [Inscrutability Case Studies](../philosophical-inquiry/inscrutability-case-studies/) | polish | 100 | 5 prompt sections are polish opportunities |
| 207 | Philosophical Inquiry | [Seeker Scenarios](../philosophical-inquiry/seeker-scenarios/) | polish | 100 | 5 prompt sections are polish opportunities |
| 208 | Philosophy of AI | [Feedback Loops](../philosophy-of-ai/feedback-loops/) | polish | 100 | 5 prompt sections are polish opportunities |
| 209 | Philosophy of AI | [Human Reaction to AI](../philosophy-of-ai/human-reaction-to-ai/) | polish | 100 | 5 prompt sections are polish opportunities |
| 210 | Philosophy of AI | [Philosophy of AI – Core Concepts](../philosophy-of-ai/philosophy-of-ai-core-concepts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 211 | Philosophy of Language | [Linguistic Abstraction](../philosophy-of-language/linguistic-abstraction/) | polish | 100 | 5 prompt sections are polish opportunities |
| 212 | Philosophy of Language | [Semantics: Convention vs Stipulation](../philosophy-of-language/semantics-convention-vs-stipulation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 213 | Philosophy of Language | [The Linearity of Language](../philosophy-of-language/the-linearity-of-language/) | polish | 100 | 5 prompt sections are polish opportunities |
| 214 | Philosophy of Mind | [Assessing Mind with Mind](../philosophy-of-mind/assessing-mind-with-mind/) | polish | 100 | 5 prompt sections are polish opportunities |
| 215 | Philosophy of Mind | [Manufacturer or Method?](../philosophy-of-mind/manufacturer-or-method/) | polish | 100 | 5 prompt sections are polish opportunities |
| 216 | Philosophy of Mind | [Philosophy of Mind Basics](../philosophy-of-mind/philosophy-of-mind-basics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 217 | Philosophy of Mind | [Where are our Thoughts?](../philosophy-of-mind/where-are-our-thoughts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 218 | Philosophy of Science | [Asymmetric Counterfactuals](../philosophy-of-science/asymmetric-counterfactuals/) | polish | 100 | 5 prompt sections are polish opportunities |
| 219 | Philosophy of Science | [Correlation and Causation](../philosophy-of-science/correlation-and-causation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 220 | Philosophy of Science | [Elements of Research Design](../philosophy-of-science/elements-of-research-design/) | polish | 100 | 5 prompt sections are polish opportunities |
| 221 | Philosophy of Science | [Is History Science?](../philosophy-of-science/is-history-science/) | polish | 100 | 5 prompt sections are polish opportunities |
| 222 | Philosophy of Science | [Research Design](../philosophy-of-science/research-design/) | polish | 100 | 5 prompt sections are polish opportunities |
| 223 | Philosophy of Science | [Scientism & Faith](../philosophy-of-science/scientism-faith/) | polish | 100 | 5 prompt sections are polish opportunities |
| 224 | Philosophy of Science | [The Power of Thought Experiments](../philosophy-of-science/the-power-of-thought-experiments/) | polish | 100 | 5 prompt sections are polish opportunities |
| 225 | Philosophy of Science | [What is Induction?](../philosophy-of-science/what-is-induction/) | polish | 100 | 5 prompt sections are polish opportunities |
| 226 | Philosophy of Science | [What is Parsimony?](../philosophy-of-science/what-is-parsimony/) | polish | 100 | 5 prompt sections are polish opportunities |
| 227 | Political Philosophy | [Peaceful Revolutions](../political-philosophy/peaceful-revolutions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 228 | Political Philosophy | [Political Philosophy Basics](../political-philosophy/political-philosophy-basics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 229 | Political Philosophy | [Political Philosophy – Core Concepts](../political-philosophy/political-philosophy-core-concepts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 230 | Rational Thought | [AI “Logic” & “Intelligence”](../rational-thought/ai-logic-intelligence/) | polish | 100 | 5 prompt sections are polish opportunities |
| 231 | Rational Thought | [Case #2 – Autism](../rational-thought/case-2-autism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 232 | Rational Thought | [Do Rationalists Skew Neurodivergent?](../rational-thought/do-rationalists-skew-neurodivergent/) | polish | 100 | 5 prompt sections are polish opportunities |
| 233 | Rational Thought | [The Professional Application of Rationality](../rational-thought/the-professional-application-of-rationality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 234 | Rational Thought | [What is Futurism?](../rational-thought/what-is-futurism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 235 | Rational Thought | [What is Game Theory?](../rational-thought/what-is-game-theory/) | polish | 100 | 5 prompt sections are polish opportunities |
| 236 | Rational Thought | [What is Rational Thought?](../rational-thought/what-is-rational-thought/) | polish | 100 | 5 prompt sections are polish opportunities |
| 237 | Economics | [A Living Wage](../economics/a-living-wage/) | polish | 100 | 4 prompt sections are polish opportunities |
| 238 | Economics | [AI & the Future of Work](../economics/ai-the-future-of-work/) | polish | 100 | 4 prompt sections are polish opportunities |
| 239 | Economics | [Business Risks](../economics/business-risks/) | polish | 100 | 4 prompt sections are polish opportunities |
| 240 | Economics | [Economic Complexity](../economics/economic-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 241 | Economics | [Economic Entitlements](../economics/economic-entitlements/) | polish | 100 | 4 prompt sections are polish opportunities |
| 242 | Economics | [Economic Optimism](../economics/economic-optimism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 243 | Economics | [Innovation Attractors](../economics/innovation-attractors/) | polish | 100 | 4 prompt sections are polish opportunities |
| 244 | Economics | [Justified Optimism](../economics/justified-optimism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 245 | Economics | [The Poverty Line](../economics/the-poverty-line/) | polish | 100 | 4 prompt sections are polish opportunities |
| 246 | Economics | [What Makes Economics “Dismal”?](../economics/what-makes-economics-dismal/) | polish | 100 | 4 prompt sections are polish opportunities |
| 247 | Epistemology | [Absolute Certainty](../epistemology/absolute-certainty/) | polish | 100 | 4 prompt sections are polish opportunities |
| 248 | Epistemology | [Case #5 – Vanishing Probabilities](../epistemology/case-5-vanishing-probabilities/) | polish | 100 | 4 prompt sections are polish opportunities |
| 249 | Epistemology | [Cromwell’s Rule](../epistemology/cromwells-rule/) | polish | 100 | 4 prompt sections are polish opportunities |
| 250 | Epistemology | [Establishing Cognitive Reliability (#1)](../epistemology/establishing-cognitive-reliability-1/) | polish | 100 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 7, queue positions 251-300

- `polish` 100 [Epistemology / Evidence Workshop](../epistemology/evidence-workshop/)
- `polish` 100 [Epistemology / Hypostatic Illogic](../epistemology/hypostatic-illogic/)
- `polish` 100 [Epistemology / Induction: Cold Reading](../epistemology/induction-cold-reading/)
- `polish` 100 [Epistemology / Mapping Belief to Evidence](../epistemology/mapping-belief-to-evidence/)
- `polish` 100 [Epistemology / Non-Scientific Ways of Knowing](../epistemology/non-scientific-ways-of-knowing/)
- `polish` 100 [Epistemology / The Primacy of Induction](../epistemology/the-primacy-of-induction/)
- `polish` 100 [Epistemology / Vicious & Virtuous Circularity](../epistemology/vicious-virtuous-circularity/)
- `polish` 100 [Epistemology / What are Syllogisms?](../epistemology/what-are-syllogisms/)
- `polish` 100 [Epistemology / What is Bayes Theorem?](../epistemology/what-is-bayes-theorem/)
- `polish` 100 [Epistemology / What is Faith?](../epistemology/what-is-faith/)

### Next +2: cycle 7, queue positions 301-346

- `polish` 100 [Philosophy of Language / Language & the Brain](../philosophy-of-language/language-the-brain/)
- `polish` 100 [Philosophy of Language / Linguistic Scaffolding](../philosophy-of-language/linguistic-scaffolding/)
- `polish` 100 [Philosophy of Language / Needless Semantic Complexity](../philosophy-of-language/needless-semantic-complexity/)
- `polish` 100 [Philosophy of Language / Nomological Density of Grammar](../philosophy-of-language/nomological-density-of-grammar/)
- `polish` 100 [Philosophy of Language / The Power of Analogy](../philosophy-of-language/the-power-of-analogy/)
- `polish` 100 [Philosophy of Language / Thought = Language?](../philosophy-of-language/thought-language/)
- `polish` 100 [Philosophy of Mind / Are there Selfless Acts?](../philosophy-of-mind/are-there-selfless-acts/)
- `polish` 100 [Philosophy of Mind / Land Ownership](../philosophy-of-mind/land-ownership/)
- `polish` 100 [Philosophy of Mind / Philosophy of Mind — Core Concepts](../philosophy-of-mind/philosophy-of-mind-core-concepts/)
- `polish` 100 [Philosophy of Mind / Preferences = Pleasures?](../philosophy-of-mind/preferences-pleasures/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 146
- Estimated batches per cycle: 7

- gap-fill: 63
- polish: 243
- review: 40
