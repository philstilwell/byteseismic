# Byteseismic Editorial Audit Tracker

Generated: 2026-06-17
Batch size: 50 pages
Current cycle: 1
Current queue start: 183 of 528

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
| 183 | Economics | [Schools of Economic Thought](../economics/schools-of-economic-thought/) | polish | 100 | 5 prompt sections are polish opportunities |
| 184 | Economics | [Taxation](../economics/taxation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 185 | Economics | [What are Moral Hazards?](../economics/what-are-moral-hazards/) | polish | 100 | 5 prompt sections are polish opportunities |
| 186 | Economics | [What is Economics?](../economics/what-is-economics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 187 | Epistemology | [Black Boxes & Epistemology](../epistemology/black-boxes-epistemology/) | polish | 100 | 5 prompt sections are polish opportunities |
| 188 | Epistemology | [Core & Deep Rationality](../epistemology/core-deep-rationality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 189 | Epistemology | [Deduction: Utility and Issues](../epistemology/deduction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 190 | Epistemology | [Extraordinary Claims](../epistemology/extraordinary-claims/) | polish | 100 | 5 prompt sections are polish opportunities |
| 191 | Epistemology | [Induction: Utility and Issues](../epistemology/induction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 192 | Epistemology | [Pragmatic Considerations vs Epistemic Assessments](../epistemology/pragmatic-considerations-vs-epistemic-assessments/) | polish | 100 | 5 prompt sections are polish opportunities |
| 193 | Epistemology | [Predictive Power](../epistemology/predictive-power/) | polish | 100 | 5 prompt sections are polish opportunities |
| 194 | Epistemology | [Presuppositions?](../epistemology/presuppositions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 195 | Epistemology | [Properly Basic Beliefs](../epistemology/properly-basic-beliefs/) | polish | 100 | 5 prompt sections are polish opportunities |
| 196 | Epistemology | [Reasoned Probabilities and Decisions](../epistemology/reasoned-probabilities-and-decisions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 197 | Epistemology | [The Abuse of “Self-Evident”](../epistemology/the-abuse-of-self-evident/) | polish | 100 | 5 prompt sections are polish opportunities |
| 198 | Epistemology | [What is Doubt?](../epistemology/what-is-doubt/) | polish | 100 | 5 prompt sections are polish opportunities |
| 199 | Epistemology | [What is Evidence?](../epistemology/what-is-evidence/) | polish | 100 | 5 prompt sections are polish opportunities |
| 200 | Ethics | [Assisted Suicide](../ethics/assisted-suicide/) | polish | 100 | 5 prompt sections are polish opportunities |
| 201 | Ethics | [Conditions for Culpability](../ethics/conditions-for-culpability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 202 | Ethics | [Evidences of Moral Facts](../ethics/evidences-of-moral-facts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 203 | Ethics | [Model of Ethical Dynamics](../ethics/model-of-ethical-dynamics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 204 | Ethics | [Self-Evident Morality?](../ethics/self-evident-morality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 205 | Humanistic Philosophies | [Personal & Cosmic Meaning](../humanistic-philosophies/personal-cosmic-meaning/) | polish | 100 | 5 prompt sections are polish opportunities |
| 206 | Humanistic Philosophies | [Russell on Faith](../humanistic-philosophies/russell-on-faith/) | polish | 100 | 5 prompt sections are polish opportunities |
| 207 | Humanistic Philosophies | [The Legitimacy of Divine Revelation](../humanistic-philosophies/the-legitimacy-of-divine-revelation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 208 | Humanistic Philosophies | [“Unpalatable” Religions](../humanistic-philosophies/unpalatable-religions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 209 | Introduction | [Careers in Philosophy](../introduction/careers-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |
| 210 | Introduction | [Philosophy: Higher Education](../introduction/philosophy-higher-education/) | polish | 100 | 5 prompt sections are polish opportunities |
| 211 | Introduction | [Women’s Interest in Philosophy](../introduction/womens-interest-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |
| 212 | Metaphysics | [Categories of Nihilism](../metaphysics/categories-of-nihilism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 213 | Metaphysics | [Dualism vs Materialism](../metaphysics/dualismvsmaterialism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 214 | Metaphysics | [Establishing the Spiritual](../metaphysics/establishing-the-spiritual/) | polish | 100 | 5 prompt sections are polish opportunities |
| 215 | Miscellany | [COVID19 & Science](../miscellany/covid-19-science/) | polish | 100 | 5 prompt sections are polish opportunities |
| 216 | Philosophical Inquiry | [Dangers: Ideologies of Emotion](../philosophical-inquiry/dangers-ideologies-of-emotion/) | polish | 100 | 5 prompt sections are polish opportunities |
| 217 | Philosophical Inquiry | [Inscrutability Case Studies](../philosophical-inquiry/inscrutability-case-studies/) | polish | 100 | 5 prompt sections are polish opportunities |
| 218 | Philosophical Inquiry | [Seeker Scenarios](../philosophical-inquiry/seeker-scenarios/) | polish | 100 | 5 prompt sections are polish opportunities |
| 219 | Philosophy of AI | [Feedback Loops](../philosophy-of-ai/feedback-loops/) | polish | 100 | 5 prompt sections are polish opportunities |
| 220 | Philosophy of AI | [Human Reaction to AI](../philosophy-of-ai/human-reaction-to-ai/) | polish | 100 | 5 prompt sections are polish opportunities |
| 221 | Philosophy of AI | [Philosophy of AI – Core Concepts](../philosophy-of-ai/philosophy-of-ai-core-concepts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 222 | Philosophy of Language | [Linguistic Abstraction](../philosophy-of-language/linguistic-abstraction/) | polish | 100 | 5 prompt sections are polish opportunities |
| 223 | Philosophy of Language | [Semantics: Convention vs Stipulation](../philosophy-of-language/semantics-convention-vs-stipulation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 224 | Philosophy of Language | [The Linearity of Language](../philosophy-of-language/the-linearity-of-language/) | polish | 100 | 5 prompt sections are polish opportunities |
| 225 | Philosophy of Mind | [Assessing Mind with Mind](../philosophy-of-mind/assessing-mind-with-mind/) | polish | 100 | 5 prompt sections are polish opportunities |
| 226 | Philosophy of Mind | [Manufacturer or Method?](../philosophy-of-mind/manufacturer-or-method/) | polish | 100 | 5 prompt sections are polish opportunities |
| 227 | Philosophy of Mind | [Philosophy of Mind Basics](../philosophy-of-mind/philosophy-of-mind-basics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 228 | Philosophy of Mind | [Where are our Thoughts?](../philosophy-of-mind/where-are-our-thoughts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 229 | Philosophy of Science | [Asymmetric Counterfactuals](../philosophy-of-science/asymmetric-counterfactuals/) | polish | 100 | 5 prompt sections are polish opportunities |
| 230 | Philosophy of Science | [Correlation and Causation](../philosophy-of-science/correlation-and-causation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 231 | Philosophy of Science | [Elements of Research Design](../philosophy-of-science/elements-of-research-design/) | polish | 100 | 5 prompt sections are polish opportunities |
| 232 | Philosophy of Science | [Is History Science?](../philosophy-of-science/is-history-science/) | polish | 100 | 5 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 1, queue positions 233-282

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

### Next +2: cycle 1, queue positions 283-332

- `polish` 100 [Metaphysics / Are Quantum Physics “Spiritual”?](../metaphysics/are-quantum-physics-spiritual/)
- `polish` 100 [Metaphysics / Could Mind be Fundamental?](../metaphysics/could-mind-be-fundamental/)
- `polish` 100 [Metaphysics / Emergence](../metaphysics/emergence/)
- `polish` 100 [Metaphysics / Energy & Psychic Phenomena](../metaphysics/energy-psychic-phenomena/)
- `polish` 100 [Metaphysics / Explanations](../metaphysics/explanations/)
- `polish` 100 [Metaphysics / Matthew Pirkowski on Emergence](../metaphysics/matthew-pirkowski-on-emergence/)
- `polish` 100 [Metaphysics / Metaphysics – Core Concepts](../metaphysics/metaphysics-core-concepts/)
- `polish` 100 [Metaphysics / Ontological Domains](../metaphysics/ontological-domains/)
- `polish` 100 [Metaphysics / Stuart Kauffman on Emergence](../metaphysics/stuart-kauffman-on-emergence/)
- `polish` 100 [Metaphysics / The Principle of Sufficient Reason](../metaphysics/the-principle-of-sufficient-reason/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 346
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 420
- review: 22
