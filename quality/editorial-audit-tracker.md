# Byteseismic Editorial Audit Tracker

Generated: 2026-07-23
Batch size: 50 pages
Current cycle: 4
Current queue start: 184 of 346

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
| 184 | Philosophy of Language | [Connotative Equivocation](../philosophy-of-language/connotative-equivocation/) | polish | 98 | 4 prompt sections are polish opportunities |
| 185 | Philosophy of Mind | [Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/) | polish | 98 | 4 prompt sections are polish opportunities |
| 186 | Philosophy of Mind | [Subjective/Objective Free Will](../philosophy-of-mind/subjective-objective-free-will/) | polish | 98 | 4 prompt sections are polish opportunities |
| 187 | Economics | [Wealth Creation](../economics/wealth-creation/) | polish | 98 | 3 prompt sections are polish opportunities |
| 188 | Epistemology | [Case #1 – Credence Complexity](../epistemology/case-1-credence-complexity/) | polish | 98 | 3 prompt sections are polish opportunities |
| 189 | Epistemology | [Case #4 – Recursive Credences](../epistemology/case-4-recursive-credences/) | polish | 98 | 3 prompt sections are polish opportunities |
| 190 | Humanistic Philosophies | [Accounting for X](../humanistic-philosophies/accounting-for-x/) | polish | 98 | 3 prompt sections are polish opportunities |
| 191 | Philosophical Inquiry | [Dangers: Carrot & Stick](../philosophical-inquiry/dangers-carrot-stick/) | polish | 98 | 3 prompt sections are polish opportunities |
| 192 | Philosophical Inquiry | [Dangers: The Notion of Fate](../philosophical-inquiry/dangers-the-notion-of-fate/) | polish | 98 | 3 prompt sections are polish opportunities |
| 193 | Philosophical Inquiry | [Testing Ideologies](../philosophical-inquiry/testing-ideologies/) | polish | 98 | 3 prompt sections are polish opportunities |
| 194 | Rational Thought | [Scope of Influence](../rational-thought/scope-of-influence/) | polish | 98 | 3 prompt sections are polish opportunities |
| 195 | Philosophical Inquiry | [Dangers: Ideologies of Mystery](../philosophical-inquiry/dangers-ideologies-of-mystery/) | polish | 99 | 2 prompt sections are polish opportunities |
| 196 | Economics | [Economic Comparisons](../economics/economic-comparisons/) | polish | 100 | 5 prompt sections are polish opportunities |
| 197 | Economics | [Economic Stability](../economics/economic-stability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 198 | Economics | [Minimum Wage](../economics/minimum-wage/) | polish | 100 | 5 prompt sections are polish opportunities |
| 199 | Economics | [Schools of Economic Thought](../economics/schools-of-economic-thought/) | polish | 100 | 5 prompt sections are polish opportunities |
| 200 | Economics | [Taxation](../economics/taxation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 201 | Economics | [What are Moral Hazards?](../economics/what-are-moral-hazards/) | polish | 100 | 5 prompt sections are polish opportunities |
| 202 | Economics | [What is Economics?](../economics/what-is-economics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 203 | Epistemology | [Black Boxes & Epistemology](../epistemology/black-boxes-epistemology/) | polish | 100 | 5 prompt sections are polish opportunities |
| 204 | Epistemology | [Core & Deep Rationality](../epistemology/core-deep-rationality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 205 | Epistemology | [Deduction: Utility and Issues](../epistemology/deduction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 206 | Epistemology | [Extraordinary Claims](../epistemology/extraordinary-claims/) | polish | 100 | 5 prompt sections are polish opportunities |
| 207 | Epistemology | [Induction: Utility and Issues](../epistemology/induction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 208 | Epistemology | [Pragmatic Considerations vs Epistemic Assessments](../epistemology/pragmatic-considerations-vs-epistemic-assessments/) | polish | 100 | 5 prompt sections are polish opportunities |
| 209 | Epistemology | [Predictive Power](../epistemology/predictive-power/) | polish | 100 | 5 prompt sections are polish opportunities |
| 210 | Epistemology | [Presuppositions?](../epistemology/presuppositions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 211 | Epistemology | [Properly Basic Beliefs](../epistemology/properly-basic-beliefs/) | polish | 100 | 5 prompt sections are polish opportunities |
| 212 | Epistemology | [Reasoned Probabilities and Decisions](../epistemology/reasoned-probabilities-and-decisions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 213 | Epistemology | [The Abuse of “Self-Evident”](../epistemology/the-abuse-of-self-evident/) | polish | 100 | 5 prompt sections are polish opportunities |
| 214 | Epistemology | [What is Doubt?](../epistemology/what-is-doubt/) | polish | 100 | 5 prompt sections are polish opportunities |
| 215 | Epistemology | [What is Evidence?](../epistemology/what-is-evidence/) | polish | 100 | 5 prompt sections are polish opportunities |
| 216 | Ethics | [Assisted Suicide](../ethics/assisted-suicide/) | polish | 100 | 5 prompt sections are polish opportunities |
| 217 | Ethics | [Conditions for Culpability](../ethics/conditions-for-culpability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 218 | Ethics | [Evidences of Moral Facts](../ethics/evidences-of-moral-facts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 219 | Ethics | [Model of Ethical Dynamics](../ethics/model-of-ethical-dynamics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 220 | Ethics | [Self-Evident Morality?](../ethics/self-evident-morality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 221 | Humanistic Philosophies | [Personal & Cosmic Meaning](../humanistic-philosophies/personal-cosmic-meaning/) | polish | 100 | 5 prompt sections are polish opportunities |
| 222 | Humanistic Philosophies | [Russell on Faith](../humanistic-philosophies/russell-on-faith/) | polish | 100 | 5 prompt sections are polish opportunities |
| 223 | Humanistic Philosophies | [The Legitimacy of Divine Revelation](../humanistic-philosophies/the-legitimacy-of-divine-revelation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 224 | Humanistic Philosophies | [“Unpalatable” Religions](../humanistic-philosophies/unpalatable-religions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 225 | Introduction | [Careers in Philosophy](../introduction/careers-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |
| 226 | Introduction | [Philosophy: Higher Education](../introduction/philosophy-higher-education/) | polish | 100 | 5 prompt sections are polish opportunities |
| 227 | Introduction | [Women’s Interest in Philosophy](../introduction/womens-interest-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |
| 228 | Metaphysics | [Categories of Nihilism](../metaphysics/categories-of-nihilism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 229 | Metaphysics | [Dualism vs Materialism](../metaphysics/dualismvsmaterialism/) | polish | 100 | 5 prompt sections are polish opportunities |
| 230 | Metaphysics | [Establishing the Spiritual](../metaphysics/establishing-the-spiritual/) | polish | 100 | 5 prompt sections are polish opportunities |
| 231 | Miscellany | [COVID19 & Science](../miscellany/covid-19-science/) | polish | 100 | 5 prompt sections are polish opportunities |
| 232 | Philosophical Inquiry | [Dangers: Ideologies of Emotion](../philosophical-inquiry/dangers-ideologies-of-emotion/) | polish | 100 | 5 prompt sections are polish opportunities |
| 233 | Philosophical Inquiry | [Inscrutability Case Studies](../philosophical-inquiry/inscrutability-case-studies/) | polish | 100 | 5 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 4, queue positions 234-283

- `polish` 100 [Philosophical Inquiry / Seeker Scenarios](../philosophical-inquiry/seeker-scenarios/)
- `polish` 100 [Philosophy of AI / Feedback Loops](../philosophy-of-ai/feedback-loops/)
- `polish` 100 [Philosophy of AI / Human Reaction to AI](../philosophy-of-ai/human-reaction-to-ai/)
- `polish` 100 [Philosophy of AI / Philosophy of AI – Core Concepts](../philosophy-of-ai/philosophy-of-ai-core-concepts/)
- `polish` 100 [Philosophy of Language / Linguistic Abstraction](../philosophy-of-language/linguistic-abstraction/)
- `polish` 100 [Philosophy of Language / Semantics: Convention vs Stipulation](../philosophy-of-language/semantics-convention-vs-stipulation/)
- `polish` 100 [Philosophy of Language / The Linearity of Language](../philosophy-of-language/the-linearity-of-language/)
- `polish` 100 [Philosophy of Mind / Assessing Mind with Mind](../philosophy-of-mind/assessing-mind-with-mind/)
- `polish` 100 [Philosophy of Mind / Manufacturer or Method?](../philosophy-of-mind/manufacturer-or-method/)
- `polish` 100 [Philosophy of Mind / Philosophy of Mind Basics](../philosophy-of-mind/philosophy-of-mind-basics/)

### Next +2: cycle 4, queue positions 284-333

- `polish` 100 [Epistemology / Vicious & Virtuous Circularity](../epistemology/vicious-virtuous-circularity/)
- `polish` 100 [Epistemology / What are Syllogisms?](../epistemology/what-are-syllogisms/)
- `polish` 100 [Epistemology / What is Bayes Theorem?](../epistemology/what-is-bayes-theorem/)
- `polish` 100 [Epistemology / What is Faith?](../epistemology/what-is-faith/)
- `polish` 100 [Ethics / Assuming Objective Evil](../ethics/assuming-objective-evil/)
- `polish` 100 [Ethics / Divine Command Theory](../ethics/divine-command-theory/)
- `polish` 100 [Ethics / Ethical Edge Case #1](../ethics/ethical-edge-case-1/)
- `polish` 100 [Ethics / No Morality = Chaos?](../ethics/no-morality-chaos/)
- `polish` 100 [Ethics / Trolley Problems](../ethics/trolley-problems/)
- `polish` 100 [Humanistic Philosophies / Are Humans More Egoistic or Altruistic?](../humanistic-philosophies/are-humans-more-egoistic-or-altruistic/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 163
- Estimated batches per cycle: 7

- gap-fill: 82
- polish: 225
- review: 39
