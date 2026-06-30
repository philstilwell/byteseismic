# Byteseismic Editorial Audit Tracker

Generated: 2026-06-30
Batch size: 50 pages
Current cycle: 2
Current queue start: 251 of 528

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
| 251 | Metaphysics | [Categories of Nihilism](../metaphysics/categories-of-nihilism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 252 | Metaphysics | [Dualism vs Materialism](../metaphysics/dualismvsmaterialism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 253 | Metaphysics | [Establishing the Spiritual](../metaphysics/establishing-the-spiritual/) | polish | 100 | 5 prompt sections are polish opportunities |
| 254 | Miscellany | [COVID19 & Science](../miscellany/covid-19-science/) | polish | 100 | 5 prompt sections are polish opportunities |
| 255 | Philosophical Inquiry | [Dangers: Ideologies of Emotion](../philosophical-inquiry/dangers-ideologies-of-emotion/) | polish | 100 | 5 prompt sections are polish opportunities |
| 256 | Philosophical Inquiry | [Inscrutability Case Studies](../philosophical-inquiry/inscrutability-case-studies/) | polish | 100 | 5 prompt sections are polish opportunities |
| 257 | Philosophical Inquiry | [Seeker Scenarios](../philosophical-inquiry/seeker-scenarios/) | polish | 100 | 5 prompt sections are polish opportunities |
| 258 | Philosophy of AI | [Feedback Loops](../philosophy-of-ai/feedback-loops/) | polish | 100 | 5 prompt sections are polish opportunities |
| 259 | Philosophy of AI | [Human Reaction to AI](../philosophy-of-ai/human-reaction-to-ai/) | polish | 100 | 5 prompt sections are polish opportunities |
| 260 | Philosophy of AI | [Philosophy of AI – Core Concepts](../philosophy-of-ai/philosophy-of-ai-core-concepts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 261 | Philosophy of Language | [Linguistic Abstraction](../philosophy-of-language/linguistic-abstraction/) | polish | 100 | 5 prompt sections are polish opportunities |
| 262 | Philosophy of Language | [Semantics: Convention vs Stipulation](../philosophy-of-language/semantics-convention-vs-stipulation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 263 | Philosophy of Language | [The Linearity of Language](../philosophy-of-language/the-linearity-of-language/) | polish | 100 | 5 prompt sections are polish opportunities |
| 264 | Philosophy of Mind | [Assessing Mind with Mind](../philosophy-of-mind/assessing-mind-with-mind/) | polish | 100 | 5 prompt sections are polish opportunities |
| 265 | Philosophy of Mind | [Manufacturer or Method?](../philosophy-of-mind/manufacturer-or-method/) | polish | 100 | 5 prompt sections are polish opportunities |
| 266 | Philosophy of Mind | [Philosophy of Mind Basics](../philosophy-of-mind/philosophy-of-mind-basics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 267 | Philosophy of Mind | [Where are our Thoughts?](../philosophy-of-mind/where-are-our-thoughts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 268 | Philosophy of Science | [Asymmetric Counterfactuals](../philosophy-of-science/asymmetric-counterfactuals/) | polish | 100 | 5 prompt sections are polish opportunities |
| 269 | Philosophy of Science | [Correlation and Causation](../philosophy-of-science/correlation-and-causation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 270 | Philosophy of Science | [Elements of Research Design](../philosophy-of-science/elements-of-research-design/) | polish | 100 | 5 prompt sections are polish opportunities |
| 271 | Philosophy of Science | [Is History Science?](../philosophy-of-science/is-history-science/) | polish | 100 | 5 prompt sections are polish opportunities |
| 272 | Philosophy of Science | [Research Design](../philosophy-of-science/research-design/) | polish | 100 | 5 prompt sections are polish opportunities |
| 273 | Philosophy of Science | [Scientism & Faith](../philosophy-of-science/scientism-faith/) | polish | 100 | 5 prompt sections are polish opportunities |
| 274 | Philosophy of Science | [The Power of Thought Experiments](../philosophy-of-science/the-power-of-thought-experiments/) | polish | 100 | 5 prompt sections are polish opportunities |
| 275 | Philosophy of Science | [What is Induction?](../philosophy-of-science/what-is-induction/) | polish | 100 | 5 prompt sections are polish opportunities |
| 276 | Philosophy of Science | [What is Parsimony?](../philosophy-of-science/what-is-parsimony/) | polish | 100 | 5 prompt sections are polish opportunities |
| 277 | Political Philosophy | [Peaceful Revolutions](../political-philosophy/peaceful-revolutions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 278 | Political Philosophy | [Political Philosophy Basics](../political-philosophy/political-philosophy-basics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 279 | Political Philosophy | [Political Philosophy – Core Concepts](../political-philosophy/political-philosophy-core-concepts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 280 | Rational Thought | [AI “Logic” & “Intelligence”](../rational-thought/ai-logic-intelligence/) | polish | 100 | 5 prompt sections are polish opportunities |
| 281 | Rational Thought | [Case #2 – Autism](../rational-thought/case-2-autism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 282 | Rational Thought | [Do Rationalists Skew Neurodivergent?](../rational-thought/do-rationalists-skew-neurodivergent/) | polish | 100 | 5 prompt sections are polish opportunities |
| 283 | Rational Thought | [The Professional Application of Rationality](../rational-thought/the-professional-application-of-rationality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 284 | Rational Thought | [What is Futurism?](../rational-thought/what-is-futurism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 285 | Rational Thought | [What is Game Theory?](../rational-thought/what-is-game-theory/) | polish | 100 | 5 prompt sections are polish opportunities |
| 286 | Rational Thought | [What is Rational Thought?](../rational-thought/what-is-rational-thought/) | polish | 100 | 5 prompt sections are polish opportunities |
| 287 | Economics | [A Living Wage](../economics/a-living-wage/) | polish | 100 | 4 prompt sections are polish opportunities |
| 288 | Economics | [AI & the Future of Work](../economics/ai-the-future-of-work/) | polish | 100 | 4 prompt sections are polish opportunities |
| 289 | Economics | [Business Risks](../economics/business-risks/) | polish | 100 | 4 prompt sections are polish opportunities |
| 290 | Economics | [Economic Complexity](../economics/economic-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 291 | Economics | [Economic Entitlements](../economics/economic-entitlements/) | polish | 100 | 4 prompt sections are polish opportunities |
| 292 | Economics | [Economic Optimism](../economics/economic-optimism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 293 | Economics | [Innovation Attractors](../economics/innovation-attractors/) | polish | 100 | 4 prompt sections are polish opportunities |
| 294 | Economics | [Justified Optimism](../economics/justified-optimism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 295 | Economics | [The Poverty Line](../economics/the-poverty-line/) | polish | 100 | 4 prompt sections are polish opportunities |
| 296 | Economics | [What Makes Economics “Dismal”?](../economics/what-makes-economics-dismal/) | polish | 100 | 4 prompt sections are polish opportunities |
| 297 | Epistemology | [Absolute Certainty](../epistemology/absolute-certainty/) | polish | 100 | 4 prompt sections are polish opportunities |
| 298 | Epistemology | [Case #5 – Vanishing Probabilities](../epistemology/case-5-vanishing-probabilities/) | polish | 100 | 4 prompt sections are polish opportunities |
| 299 | Epistemology | [Cromwell’s Rule](../epistemology/cromwells-rule/) | polish | 100 | 4 prompt sections are polish opportunities |
| 300 | Epistemology | [Establishing Cognitive Reliability (#1)](../epistemology/establishing-cognitive-reliability-1/) | polish | 100 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 2, queue positions 301-350

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

### Next +2: cycle 2, queue positions 351-400

- `polish` 100 [Philosophy of Language / Abandoned Words](../philosophy-of-language/abandoned-words/)
- `polish` 100 [Philosophy of Language / Connotative Equivocation](../philosophy-of-language/connotative-equivocation/)
- `polish` 100 [Philosophy of Language / Language & the Brain](../philosophy-of-language/language-the-brain/)
- `polish` 100 [Philosophy of Language / Linguistic Scaffolding](../philosophy-of-language/linguistic-scaffolding/)
- `polish` 100 [Philosophy of Language / Needless Semantic Complexity](../philosophy-of-language/needless-semantic-complexity/)
- `polish` 100 [Philosophy of Language / Nomological Density of Grammar](../philosophy-of-language/nomological-density-of-grammar/)
- `polish` 100 [Philosophy of Language / The Power of Analogy](../philosophy-of-language/the-power-of-analogy/)
- `polish` 100 [Philosophy of Language / Thought = Language?](../philosophy-of-language/thought-language/)
- `polish` 100 [Philosophy of Mind / Are there Selfless Acts?](../philosophy-of-mind/are-there-selfless-acts/)
- `polish` 100 [Philosophy of Mind / Land Ownership](../philosophy-of-mind/land-ownership/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 278
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 396
- review: 46
