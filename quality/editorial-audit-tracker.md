# Byteseismic Editorial Audit Tracker

Generated: 2026-06-16
Batch size: 50 pages
Current cycle: 1
Current queue start: 1 of 528

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
| 1 | Humanistic Philosophies | [What is Existentialism?](../humanistic-philosophies/what-is-existentialism/) | review | 94 | 3 prompt sections are polish opportunities; editorial issues: work-order heading |
| 2 | Humanistic Philosophies | [Russell on Faith](../humanistic-philosophies/russell-on-faith/) | review | 100 | 5 prompt sections are polish opportunities; editorial issues: work-order heading |
| 3 | Philosophy of Mind | [Philosophy of Mind Basics](../philosophy-of-mind/philosophy-of-mind-basics/) | review | 100 | 5 prompt sections are polish opportunities; editorial issues: work-order heading |
| 4 | Philosophy of Science | [What is Parsimony?](../philosophy-of-science/what-is-parsimony/) | review | 100 | 5 prompt sections are polish opportunities; editorial issues: work-order heading |
| 5 | Political Philosophy | [Political Philosophy Basics](../political-philosophy/political-philosophy-basics/) | review | 100 | 5 prompt sections are polish opportunities; editorial issues: work-order heading |
| 6 | Rational Thought | [The Professional Application of Rationality](../rational-thought/the-professional-application-of-rationality/) | review | 100 | 5 prompt sections are polish opportunities; editorial issues: work-order heading |
| 7 | Economics | [Innovation Attractors](../economics/innovation-attractors/) | review | 100 | 4 prompt sections are polish opportunities; editorial issues: work-order heading |
| 8 | Economics | [Justified Optimism](../economics/justified-optimism/) | review | 100 | 4 prompt sections are polish opportunities; editorial issues: overlong heading |
| 9 | Economics | [The Poverty Line](../economics/the-poverty-line/) | review | 100 | 4 prompt sections are polish opportunities; editorial issues: work-order heading |
| 10 | Epistemology | [Induction: Cold Reading](../epistemology/induction-cold-reading/) | review | 100 | 4 prompt sections are polish opportunities; editorial issues: work-order heading |
| 11 | Metaphysics | [Matthew Pirkowski on Emergence](../metaphysics/matthew-pirkowski-on-emergence/) | review | 100 | 4 prompt sections are polish opportunities; editorial issues: work-order heading |
| 12 | Metaphysics | [Stuart Kauffman on Emergence](../metaphysics/stuart-kauffman-on-emergence/) | review | 100 | 4 prompt sections are polish opportunities; editorial issues: work-order heading |
| 13 | Miscellany | [David Krakauer on Complexity](../miscellany/david-krakauer-on-complexity/) | review | 100 | 4 prompt sections are polish opportunities; editorial issues: work-order heading |
| 14 | Economics | [Micro/Macro Economics](../economics/micro-macro-economics/) | review | 100 | 3 prompt sections are polish opportunities; editorial issues: work-order heading |
| 15 | Rational Thought | [Are Averages “Not Always True”?](../rational-thought/are-averages-not-always-true/) | review | 71 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 16 | Epistemology | [Charles Darwin](../epistemology/charles-darwin/) | review | 73 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 17 | Epistemology | [⌁ Perceived Responsibility and Perceived Control](../epistemology/perceived-responsibility-and-perceived-control/) | review | 75 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 18 | Ethics | [⌁ Bounded Compassionate Agency](../ethics/bounded-compassionate-agency/) | review | 75 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 19 | Ethics | [⌁ Scope Leakage of Happiness](../ethics/scope-leakage-of-happiness/) | review | 75 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 20 | Epistemology | [Many Logics?](../epistemology/many-logics/) | review | 75 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 21 | Ethics | [Recommendations vs Moral Claims](../ethics/recommendations-vs-moral-claims/) | review | 76 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 22 | Ethics | [Equivocation on “Wrong”](../ethics/equivocation-on-wrong/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 23 | Philosophers | [Georg Wilhelm Friedrich Hegel](../philosophers/georg-wilhelm-friedrich-hegel/) | review | 79 | 1 prompt sections need review; 4 prompt sections need gap fill |
| 24 | Philosophy of Science | [What is Falsifiability?](../philosophy-of-science/what-is-falsifiability/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 25 | Rational Thought | [⌁ Finite Agency in an Infinite Feed](../rational-thought/finite-agency-in-an-infinite-feed/) | review | 80 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 26 | Epistemology | [Case #2 – The Telephone Game](../epistemology/case-2-the-telephone-game/) | review | 80 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 27 | Ethics | [The Value Selection Hypothesis](../ethics/the-value-selection-hypothesis/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 28 | Ethics | [⌁ Legitimate Culpability vs Borrowed Guilt](../ethics/legitimate-culpability-vs-borrowed-guilt/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 29 | Ethics | [Competing Ethical Considerations](../ethics/competing-ethical-considerations/) | review | 81 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 30 | Philosophy of Science | [What are Pseudosciences?](../philosophy-of-science/what-are-pseudosciences/) | review | 82 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 31 | Philosophers | [Jean-Paul Sartre](../philosophers/jean-paul-sartre/) | review | 83 | 1 prompt sections need review; 4 prompt sections need gap fill |
| 32 | Philosophy of Science | [The Value of Surveys](../philosophy-of-science/the-value-of-surveys/) | review | 83 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 33 | Epistemology | [AI Reasoning Case Study](../epistemology/ai-reasoning-case-study/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 34 | Epistemology | [Induction: Forecasting](../epistemology/induction-forecasting/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 35 | Rational Thought | [Sample Size & Margin of Error](../rational-thought/sample-size-margin-of-error/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 36 | Ethics | [Compassion vs Moral Systems](../ethics/compassion-vs-moral-systems/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 37 | Philosophers | [Herbert Marcuse](../philosophers/herbert-marcuse/) | gap-fill | 86 | 4 prompt sections need gap fill |
| 38 | Philosophers | [Ludwig Wittgenstein](../philosophers/ludwig-wittgenstein/) | gap-fill | 86 | 4 prompt sections need gap fill |
| 39 | Philosophers | [Simone de Beauvoir](../philosophers/simone-de-beauvoir/) | gap-fill | 86 | 4 prompt sections need gap fill |
| 40 | Philosophers | [Aristotle](../philosophers/aristotle/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 41 | Philosophers | [Daniel Dennett](../philosophers/daniel-dennett/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 42 | Philosophers | [David Hume](../philosophers/david-hume/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 43 | Philosophers | [Plato](../philosophers/plato-2/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 44 | Philosophers | [René Descartes](../philosophers/rene-descartes/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 45 | Philosophers | [Socrates](../philosophers/socrates/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 46 | Philosophers | [Søren Kierkegaard](../philosophers/soren-kierkegaard/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 47 | Philosophers | [Bertrand Russell](../philosophers/bertrand-russell/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 48 | Philosophers | [Charles Sanders Peirce](../philosophers/charles-sanders-peirce/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 49 | Philosophers | [Jacques Derrida](../philosophers/jacques-derrida/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 50 | Philosophers | [John Locke](../philosophers/john-locke/) | gap-fill | 93 | 4 prompt sections need gap fill |

## Upcoming Batch Preview

### Next +1: cycle 1, queue positions 51-100

- `gap-fill` 93 [Philosophers / Thomas Aquinas](../philosophers/thomas-aquinas/)
- `gap-fill` 95 [Philosophers / Immanuel Kant](../philosophers/immanuel-kant/)
- `gap-fill` 95 [Philosophers / Martin Heidegger](../philosophers/martin-heidegger/)
- `gap-fill` 95 [Philosophers / Thomas Hobbes](../philosophers/thomas-hobbes/)
- `gap-fill` 95 [Philosophers / Willard Van Orman Quine](../philosophers/willard-van-orman-quine/)
- `gap-fill` 97 [Philosophers / Baruch Spinoza](../philosophers/baruch-spinoza/)
- `gap-fill` 97 [Philosophers / Edmund Husserl](../philosophers/edmund-husserl/)
- `gap-fill` 97 [Philosophers / Epicurus](../philosophers/epicurus/)
- `gap-fill` 97 [Philosophers / Gottfried Wilhelm Leibniz](../philosophers/gottfried-wilhelm-leibniz/)
- `gap-fill` 98 [Philosophers / Empiricists](../philosophers/empiricists/)

### Next +2: cycle 1, queue positions 101-150

- `gap-fill` 100 [Philosophers / Mozi](../philosophers/mozi/)
- `gap-fill` 100 [Philosophers / Nagarjuna](../philosophers/nagarjuna/)
- `gap-fill` 100 [Philosophers / Niccolo Machiavelli](../philosophers/niccolo-machiavelli/)
- `gap-fill` 100 [Philosophers / Parmenides](../philosophers/parmenides/)
- `gap-fill` 100 [Philosophers / Plato](../philosophers/plato/)
- `gap-fill` 100 [Philosophers / Plotinus](../philosophers/plotinus/)
- `gap-fill` 100 [Philosophers / Pragmatists](../philosophers/pragmatists/)
- `gap-fill` 100 [Philosophers / Rationalists](../philosophers/rationalists/)
- `gap-fill` 100 [Philosophers / Saul Kripke](../philosophers/saul-kripke/)
- `gap-fill` 100 [Philosophers / Scholastics](../philosophers/scholastics/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 528
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 406
- review: 36
