# Byteseismic Editorial Audit Tracker

Generated: 2026-06-29
Batch size: 50 pages
Current cycle: 2
Current queue start: 201 of 528

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
| 201 | Philosophical Inquiry | [Conspiracies & Misunderstanding Human Nature](../philosophical-inquiry/conspiracies-misunderstanding-human-nature/) | polish | 98 | 4 prompt sections are polish opportunities |
| 202 | Philosophy of Mind | [Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/) | polish | 98 | 4 prompt sections are polish opportunities |
| 203 | Philosophy of Mind | [Subjective/Objective Free Will](../philosophy-of-mind/subjective-objective-free-will/) | polish | 98 | 4 prompt sections are polish opportunities |
| 204 | Rational Thought | [Training Data Bias](../rational-thought/training-data-bias/) | polish | 98 | 4 prompt sections are polish opportunities |
| 205 | Economics | [Wealth Creation](../economics/wealth-creation/) | polish | 98 | 3 prompt sections are polish opportunities |
| 206 | Epistemology | [Case #1 – Credence Complexity](../epistemology/case-1-credence-complexity/) | polish | 98 | 3 prompt sections are polish opportunities |
| 207 | Epistemology | [Case #4 – Recursive Credences](../epistemology/case-4-recursive-credences/) | polish | 98 | 3 prompt sections are polish opportunities |
| 208 | Ethics | [Harris’ Notion of Morality](../ethics/harris-notion-of-morality/) | polish | 98 | 3 prompt sections are polish opportunities |
| 209 | Humanistic Philosophies | [Accounting for X](../humanistic-philosophies/accounting-for-x/) | polish | 98 | 3 prompt sections are polish opportunities |
| 210 | Humanistic Philosophies | [Religions](../humanistic-philosophies/religions/) | polish | 98 | 3 prompt sections are polish opportunities |
| 211 | Introduction | [Philosophical Maturity](../introduction/philosophical-maturity/) | polish | 98 | 3 prompt sections are polish opportunities |
| 212 | Philosophical Inquiry | [Dangers: Carrot & Stick](../philosophical-inquiry/dangers-carrot-stick/) | polish | 98 | 3 prompt sections are polish opportunities |
| 213 | Philosophical Inquiry | [Dangers: The Notion of Fate](../philosophical-inquiry/dangers-the-notion-of-fate/) | polish | 98 | 3 prompt sections are polish opportunities |
| 214 | Philosophical Inquiry | [Testing Ideologies](../philosophical-inquiry/testing-ideologies/) | polish | 98 | 3 prompt sections are polish opportunities |
| 215 | Rational Thought | [Scope of Influence](../rational-thought/scope-of-influence/) | polish | 98 | 3 prompt sections are polish opportunities |
| 216 | Humanistic Philosophies | [Christian Apologetics](../humanistic-philosophies/christian-apologetics/) | polish | 99 | 4 prompt sections are polish opportunities |
| 217 | Rational Thought | [1 at 99.5% or 5 at 95%?](../rational-thought/1-at-99-5-or-5-at-95/) | polish | 99 | 4 prompt sections are polish opportunities |
| 218 | Philosophical Inquiry | [Dangers: Ideologies of Mystery](../philosophical-inquiry/dangers-ideologies-of-mystery/) | polish | 99 | 2 prompt sections are polish opportunities |
| 219 | Economics | [Economic Comparisons](../economics/economic-comparisons/) | polish | 100 | 5 prompt sections are polish opportunities |
| 220 | Economics | [Economic Stability](../economics/economic-stability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 221 | Economics | [Minimum Wage](../economics/minimum-wage/) | polish | 100 | 5 prompt sections are polish opportunities |
| 222 | Economics | [Schools of Economic Thought](../economics/schools-of-economic-thought/) | polish | 100 | 5 prompt sections are polish opportunities |
| 223 | Economics | [Taxation](../economics/taxation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 224 | Economics | [What are Moral Hazards?](../economics/what-are-moral-hazards/) | polish | 100 | 5 prompt sections are polish opportunities |
| 225 | Economics | [What is Economics?](../economics/what-is-economics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 226 | Epistemology | [Black Boxes & Epistemology](../epistemology/black-boxes-epistemology/) | polish | 100 | 5 prompt sections are polish opportunities |
| 227 | Epistemology | [Core & Deep Rationality](../epistemology/core-deep-rationality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 228 | Epistemology | [Deduction: Utility and Issues](../epistemology/deduction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 229 | Epistemology | [Extraordinary Claims](../epistemology/extraordinary-claims/) | polish | 100 | 5 prompt sections are polish opportunities |
| 230 | Epistemology | [Induction: Utility and Issues](../epistemology/induction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 231 | Epistemology | [Pragmatic Considerations vs Epistemic Assessments](../epistemology/pragmatic-considerations-vs-epistemic-assessments/) | polish | 100 | 5 prompt sections are polish opportunities |
| 232 | Epistemology | [Predictive Power](../epistemology/predictive-power/) | polish | 100 | 5 prompt sections are polish opportunities |
| 233 | Epistemology | [Presuppositions?](../epistemology/presuppositions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 234 | Epistemology | [Properly Basic Beliefs](../epistemology/properly-basic-beliefs/) | polish | 100 | 5 prompt sections are polish opportunities |
| 235 | Epistemology | [Reasoned Probabilities and Decisions](../epistemology/reasoned-probabilities-and-decisions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 236 | Epistemology | [The Abuse of “Self-Evident”](../epistemology/the-abuse-of-self-evident/) | polish | 100 | 5 prompt sections are polish opportunities |
| 237 | Epistemology | [What is Doubt?](../epistemology/what-is-doubt/) | polish | 100 | 5 prompt sections are polish opportunities |
| 238 | Epistemology | [What is Evidence?](../epistemology/what-is-evidence/) | polish | 100 | 5 prompt sections are polish opportunities |
| 239 | Ethics | [Assisted Suicide](../ethics/assisted-suicide/) | polish | 100 | 5 prompt sections are polish opportunities |
| 240 | Ethics | [Conditions for Culpability](../ethics/conditions-for-culpability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 241 | Ethics | [Evidences of Moral Facts](../ethics/evidences-of-moral-facts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 242 | Ethics | [Model of Ethical Dynamics](../ethics/model-of-ethical-dynamics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 243 | Ethics | [Self-Evident Morality?](../ethics/self-evident-morality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 244 | Humanistic Philosophies | [Personal & Cosmic Meaning](../humanistic-philosophies/personal-cosmic-meaning/) | polish | 100 | 5 prompt sections are polish opportunities |
| 245 | Humanistic Philosophies | [Russell on Faith](../humanistic-philosophies/russell-on-faith/) | polish | 100 | 5 prompt sections are polish opportunities |
| 246 | Humanistic Philosophies | [The Legitimacy of Divine Revelation](../humanistic-philosophies/the-legitimacy-of-divine-revelation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 247 | Humanistic Philosophies | [“Unpalatable” Religions](../humanistic-philosophies/unpalatable-religions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 248 | Introduction | [Careers in Philosophy](../introduction/careers-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |
| 249 | Introduction | [Philosophy: Higher Education](../introduction/philosophy-higher-education/) | polish | 100 | 5 prompt sections are polish opportunities |
| 250 | Introduction | [Women’s Interest in Philosophy](../introduction/womens-interest-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 2, queue positions 251-300

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

### Next +2: cycle 2, queue positions 301-350

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

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 328
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 396
- review: 46
