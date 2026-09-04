# Byteseismic Editorial Audit Tracker

Generated: 2026-09-04
Batch size: 50 pages
Current cycle: 7
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
| 151 | Ethics | [What are Ethics?](../ethics/what-are-ethics/) | polish | 97 | 3 prompt sections are polish opportunities |
| 152 | Ethics | [“Is” vs “Ought”](../ethics/is-vs-ought/) | polish | 97 | 3 prompt sections are polish opportunities |
| 153 | Philosophical Inquiry | [How Minds are Changed](../philosophical-inquiry/how-minds-are-changed/) | polish | 97 | 3 prompt sections are polish opportunities |
| 154 | Economics | [Economic Comparisons](../economics/economic-comparisons/) | polish | 98 | 5 prompt sections are polish opportunities |
| 155 | Epistemology | [Preponderance of Evidence?](../epistemology/preponderance-of-evidence/) | polish | 98 | 5 prompt sections are polish opportunities |
| 156 | Philosophy of Language | [What is Language?](../philosophy-of-language/what-is-language/) | polish | 98 | 5 prompt sections are polish opportunities |
| 157 | Miscellany | [Domains of Aesthetics](../miscellany/domains-of-aesthetics/) | polish | 98 | 4 prompt sections are polish opportunities |
| 158 | Philosophical Inquiry | [Conspiracies & Misunderstanding Human Nature](../philosophical-inquiry/conspiracies-misunderstanding-human-nature/) | polish | 98 | 4 prompt sections are polish opportunities |
| 159 | Philosophy of Mind | [Functionalism & Subjectivity](../philosophy-of-mind/functionalism-subjectivity/) | polish | 98 | 4 prompt sections are polish opportunities |
| 160 | Philosophy of Mind | [Subjective/Objective Free Will](../philosophy-of-mind/subjective-objective-free-will/) | polish | 98 | 4 prompt sections are polish opportunities |
| 161 | Economics | [Wealth Creation](../economics/wealth-creation/) | polish | 98 | 3 prompt sections are polish opportunities |
| 162 | Epistemology | [Case #1 – Credence Complexity](../epistemology/case-1-credence-complexity/) | polish | 98 | 3 prompt sections are polish opportunities |
| 163 | Epistemology | [Case #4 – Recursive Credences](../epistemology/case-4-recursive-credences/) | polish | 98 | 3 prompt sections are polish opportunities |
| 164 | Humanistic Philosophies | [Accounting for X](../humanistic-philosophies/accounting-for-x/) | polish | 98 | 3 prompt sections are polish opportunities |
| 165 | Philosophical Inquiry | [Dangers: Carrot & Stick](../philosophical-inquiry/dangers-carrot-stick/) | polish | 98 | 3 prompt sections are polish opportunities |
| 166 | Philosophical Inquiry | [Dangers: The Notion of Fate](../philosophical-inquiry/dangers-the-notion-of-fate/) | polish | 98 | 3 prompt sections are polish opportunities |
| 167 | Philosophical Inquiry | [Testing Ideologies](../philosophical-inquiry/testing-ideologies/) | polish | 98 | 3 prompt sections are polish opportunities |
| 168 | Rational Thought | [Scope of Influence](../rational-thought/scope-of-influence/) | polish | 98 | 3 prompt sections are polish opportunities |
| 169 | Philosophical Inquiry | [Dangers: Ideologies of Mystery](../philosophical-inquiry/dangers-ideologies-of-mystery/) | polish | 99 | 2 prompt sections are polish opportunities |
| 170 | Economics | [Economic Stability](../economics/economic-stability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 171 | Economics | [Minimum Wage](../economics/minimum-wage/) | polish | 100 | 5 prompt sections are polish opportunities |
| 172 | Economics | [Schools of Economic Thought](../economics/schools-of-economic-thought/) | polish | 100 | 5 prompt sections are polish opportunities |
| 173 | Economics | [Taxation](../economics/taxation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 174 | Economics | [What are Moral Hazards?](../economics/what-are-moral-hazards/) | polish | 100 | 5 prompt sections are polish opportunities |
| 175 | Economics | [What is Economics?](../economics/what-is-economics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 176 | Epistemology | [Black Boxes & Epistemology](../epistemology/black-boxes-epistemology/) | polish | 100 | 5 prompt sections are polish opportunities |
| 177 | Epistemology | [Core & Deep Rationality](../epistemology/core-deep-rationality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 178 | Epistemology | [Deduction: Utility and Issues](../epistemology/deduction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 179 | Epistemology | [Extraordinary Claims](../epistemology/extraordinary-claims/) | polish | 100 | 5 prompt sections are polish opportunities |
| 180 | Epistemology | [Induction: Utility and Issues](../epistemology/induction-utility-and-issues/) | polish | 100 | 5 prompt sections are polish opportunities |
| 181 | Epistemology | [Pragmatic Considerations vs Epistemic Assessments](../epistemology/pragmatic-considerations-vs-epistemic-assessments/) | polish | 100 | 5 prompt sections are polish opportunities |
| 182 | Epistemology | [Predictive Power](../epistemology/predictive-power/) | polish | 100 | 5 prompt sections are polish opportunities |
| 183 | Epistemology | [Presuppositions?](../epistemology/presuppositions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 184 | Epistemology | [Properly Basic Beliefs](../epistemology/properly-basic-beliefs/) | polish | 100 | 5 prompt sections are polish opportunities |
| 185 | Epistemology | [Reasoned Probabilities and Decisions](../epistemology/reasoned-probabilities-and-decisions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 186 | Epistemology | [The Abuse of “Self-Evident”](../epistemology/the-abuse-of-self-evident/) | polish | 100 | 5 prompt sections are polish opportunities |
| 187 | Epistemology | [What is Doubt?](../epistemology/what-is-doubt/) | polish | 100 | 5 prompt sections are polish opportunities |
| 188 | Epistemology | [What is Evidence?](../epistemology/what-is-evidence/) | polish | 100 | 5 prompt sections are polish opportunities |
| 189 | Ethics | [Assisted Suicide](../ethics/assisted-suicide/) | polish | 100 | 5 prompt sections are polish opportunities |
| 190 | Ethics | [Conditions for Culpability](../ethics/conditions-for-culpability/) | polish | 100 | 5 prompt sections are polish opportunities |
| 191 | Ethics | [Evidences of Moral Facts](../ethics/evidences-of-moral-facts/) | polish | 100 | 5 prompt sections are polish opportunities |
| 192 | Ethics | [Model of Ethical Dynamics](../ethics/model-of-ethical-dynamics/) | polish | 100 | 5 prompt sections are polish opportunities |
| 193 | Ethics | [Self-Evident Morality?](../ethics/self-evident-morality/) | polish | 100 | 5 prompt sections are polish opportunities |
| 194 | Humanistic Philosophies | [Personal & Cosmic Meaning](../humanistic-philosophies/personal-cosmic-meaning/) | polish | 100 | 5 prompt sections are polish opportunities |
| 195 | Humanistic Philosophies | [Russell on Faith](../humanistic-philosophies/russell-on-faith/) | polish | 100 | 5 prompt sections are polish opportunities |
| 196 | Humanistic Philosophies | [The Legitimacy of Divine Revelation](../humanistic-philosophies/the-legitimacy-of-divine-revelation/) | polish | 100 | 5 prompt sections are polish opportunities |
| 197 | Humanistic Philosophies | [“Unpalatable” Religions](../humanistic-philosophies/unpalatable-religions/) | polish | 100 | 5 prompt sections are polish opportunities |
| 198 | Introduction | [Careers in Philosophy](../introduction/careers-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |
| 199 | Introduction | [Philosophy: Higher Education](../introduction/philosophy-higher-education/) | polish | 100 | 5 prompt sections are polish opportunities |
| 200 | Introduction | [Women’s Interest in Philosophy](../introduction/womens-interest-in-philosophy/) | polish | 100 | 5 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 7, queue positions 201-250

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

### Next +2: cycle 7, queue positions 251-300

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

- Tracked pages: 346
- Pages remaining in current cycle: 196
- Estimated batches per cycle: 7

- gap-fill: 63
- polish: 243
- review: 40
