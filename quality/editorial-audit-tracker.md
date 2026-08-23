# Byteseismic Editorial Audit Tracker

Generated: 2026-08-23
Batch size: 50 pages
Current cycle: 6
Current queue start: 151 of 346

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
| 151 | Ethics | [“Is” vs “Ought”](../ethics/is-vs-ought/) | polish | 97 | 3 prompt sections are polish opportunities |
| 152 | Philosophical Inquiry | [How Minds are Changed](../philosophical-inquiry/how-minds-are-changed/) | polish | 97 | 3 prompt sections are polish opportunities |
| 153 | Philosophical Inquiry | [Conspiracies & Misunderstanding Human Nature](../philosophical-inquiry/conspiracies-misunderstanding-human-nature/) | polish | 98 | 4 prompt sections are polish opportunities |
| 154 | Philosophy of Mind | [Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/) | polish | 98 | 4 prompt sections are polish opportunities |
| 155 | Epistemology | [Case #1 – Credence Complexity](../epistemology/case-1-credence-complexity/) | polish | 98 | 3 prompt sections are polish opportunities |
| 156 | Epistemology | [Case #4 – Recursive Credences](../epistemology/case-4-recursive-credences/) | polish | 98 | 3 prompt sections are polish opportunities |
| 157 | Philosophical Inquiry | [Dangers: Carrot & Stick](../philosophical-inquiry/dangers-carrot-stick/) | polish | 98 | 3 prompt sections are polish opportunities |
| 158 | Philosophical Inquiry | [Testing Ideologies](../philosophical-inquiry/testing-ideologies/) | polish | 98 | 3 prompt sections are polish opportunities |
| 159 | Rational Thought | [Scope of Influence](../rational-thought/scope-of-influence/) | polish | 98 | 3 prompt sections are polish opportunities |
| 160 | Philosophical Inquiry | [Dangers: Ideologies of Mystery](../philosophical-inquiry/dangers-ideologies-of-mystery/) | polish | 99 | 2 prompt sections are polish opportunities |
| 161 | Epistemology | [Black Boxes & Epistemology](../epistemology/black-boxes-epistemology/) | polish | 100 | 5 prompt sections are polish opportunities |
| 162 | Epistemology | [Core & Deep Rationality](../epistemology/core-deep-rationality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 163 | Epistemology | [Deduction: Utility and Issues](../epistemology/deduction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 164 | Epistemology | [Extraordinary Claims](../epistemology/extraordinary-claims/) | polish | 100 | 5 prompt sections are polish opportunities |
| 165 | Epistemology | [Induction: Utility and Issues](../epistemology/induction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 166 | Epistemology | [Pragmatic Considerations vs Epistemic Assessments](../epistemology/pragmatic-considerations-vs-epistemic-assessments/) | polish | 100 | 5 prompt sections are polish opportunities |
| 167 | Epistemology | [Predictive Power](../epistemology/predictive-power/) | polish | 100 | 5 prompt sections are polish opportunities |
| 168 | Epistemology | [Presuppositions?](../epistemology/presuppositions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 169 | Epistemology | [Properly Basic Beliefs](../epistemology/properly-basic-beliefs/) | polish | 100 | 5 prompt sections are polish opportunities |
| 170 | Epistemology | [Reasoned Probabilities and Decisions](../epistemology/reasoned-probabilities-and-decisions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 171 | Epistemology | [The Abuse of “Self-Evident”](../epistemology/the-abuse-of-self-evident/) | polish | 100 | 5 prompt sections are polish opportunities |
| 172 | Epistemology | [What is Doubt?](../epistemology/what-is-doubt/) | polish | 100 | 5 prompt sections are polish opportunities |
| 173 | Epistemology | [What is Evidence?](../epistemology/what-is-evidence/) | polish | 100 | 5 prompt sections are polish opportunities |
| 174 | Ethics | [Assisted Suicide](../ethics/assisted-suicide/) | polish | 100 | 5 prompt sections are polish opportunities |
| 175 | Ethics | [Conditions for Culpability](../ethics/conditions-for-culpability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 176 | Ethics | [Evidences of Moral Facts](../ethics/evidences-of-moral-facts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 177 | Ethics | [Model of Ethical Dynamics](../ethics/model-of-ethical-dynamics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 178 | Ethics | [Self-Evident Morality?](../ethics/self-evident-morality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 179 | Humanistic Philosophies | [Personal & Cosmic Meaning](../humanistic-philosophies/personal-cosmic-meaning/) | polish | 100 | 5 prompt sections are polish opportunities |
| 180 | Humanistic Philosophies | [Russell on Faith](../humanistic-philosophies/russell-on-faith/) | polish | 100 | 5 prompt sections are polish opportunities |
| 181 | Humanistic Philosophies | [The Legitimacy of Divine Revelation](../humanistic-philosophies/the-legitimacy-of-divine-revelation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 182 | Humanistic Philosophies | [“Unpalatable” Religions](../humanistic-philosophies/unpalatable-religions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 183 | Introduction | [Careers in Philosophy](../introduction/careers-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |
| 184 | Introduction | [Philosophy: Higher Education](../introduction/philosophy-higher-education/) | polish | 100 | 5 prompt sections are polish opportunities |
| 185 | Introduction | [Women’s Interest in Philosophy](../introduction/womens-interest-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |
| 186 | Metaphysics | [Categories of Nihilism](../metaphysics/categories-of-nihilism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 187 | Metaphysics | [Dualism vs Materialism](../metaphysics/dualismvsmaterialism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 188 | Metaphysics | [Establishing the Spiritual](../metaphysics/establishing-the-spiritual/) | polish | 100 | 5 prompt sections are polish opportunities |
| 189 | Miscellany | [COVID19 & Science](../miscellany/covid-19-science/) | polish | 100 | 5 prompt sections are polish opportunities |
| 190 | Philosophical Inquiry | [Dangers: Ideologies of Emotion](../philosophical-inquiry/dangers-ideologies-of-emotion/) | polish | 100 | 5 prompt sections are polish opportunities |
| 191 | Philosophical Inquiry | [Inscrutability Case Studies](../philosophical-inquiry/inscrutability-case-studies/) | polish | 100 | 5 prompt sections are polish opportunities |
| 192 | Philosophical Inquiry | [Seeker Scenarios](../philosophical-inquiry/seeker-scenarios/) | polish | 100 | 5 prompt sections are polish opportunities |
| 193 | Philosophy of AI | [Feedback Loops](../philosophy-of-ai/feedback-loops/) | polish | 100 | 5 prompt sections are polish opportunities |
| 194 | Philosophy of AI | [Human Reaction to AI](../philosophy-of-ai/human-reaction-to-ai/) | polish | 100 | 5 prompt sections are polish opportunities |
| 195 | Philosophy of AI | [Philosophy of AI – Core Concepts](../philosophy-of-ai/philosophy-of-ai-core-concepts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 196 | Philosophy of Language | [Linguistic Abstraction](../philosophy-of-language/linguistic-abstraction/) | polish | 100 | 5 prompt sections are polish opportunities |
| 197 | Philosophy of Language | [Semantics: Convention vs Stipulation](../philosophy-of-language/semantics-convention-vs-stipulation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 198 | Philosophy of Language | [The Linearity of Language](../philosophy-of-language/the-linearity-of-language/) | polish | 100 | 5 prompt sections are polish opportunities |
| 199 | Philosophy of Mind | [Assessing Mind with Mind](../philosophy-of-mind/assessing-mind-with-mind/) | polish | 100 | 5 prompt sections are polish opportunities |
| 200 | Philosophy of Mind | [Manufacturer or Method?](../philosophy-of-mind/manufacturer-or-method/) | polish | 100 | 5 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 6, queue positions 201-250

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

### Next +2: cycle 6, queue positions 251-300

- `polish` 100 [Ethics / Value & Morality in Diversity?](../ethics/value-morality-in-diversity/)
- `polish` 100 [Humanistic Philosophies / Are Humans More Egoistic or Altruistic?](../humanistic-philosophies/are-humans-more-egoistic-or-altruistic/)
- `polish` 100 [Humanistic Philosophies / Existentialism: Key Concepts](../humanistic-philosophies/existentialism-key-concepts/)
- `polish` 100 [Humanistic Philosophies / New Manifestations of Theism](../humanistic-philosophies/new-manifestations-of-theism/)
- `polish` 100 [Introduction / Studying Philosophy: Resources](../introduction/studying-philosophy-resources/)
- `polish` 100 [Metaphysics / A Taxonomy of Impossibilities](../metaphysics/a-taxonomy-of-impossibilities/)
- `polish` 100 [Metaphysics / Are Quantum Physics “Spiritual”?](../metaphysics/are-quantum-physics-spiritual/)
- `polish` 100 [Metaphysics / Could Mind be Fundamental?](../metaphysics/could-mind-be-fundamental/)
- `polish` 100 [Metaphysics / Emergence](../metaphysics/emergence/)
- `polish` 100 [Metaphysics / Energy & Psychic Phenomena](../metaphysics/energy-psychic-phenomena/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 196
- Estimated batches per cycle: 7

- gap-fill: 64
- polish: 242
- review: 40
