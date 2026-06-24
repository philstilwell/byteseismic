# Byteseismic Editorial Audit Tracker

Generated: 2026-06-24
Batch size: 50 pages
Current cycle: 2
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
| 1 | Humanistic Philosophies | [Increasing Religious Humility](../humanistic-philosophies/increasing-religious-humility/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 2 | Rational Thought | [Where Framing Goes Awry](../rational-thought/where-framing-goes-awry/) | review | 89 | 4 prompt sections are polish opportunities; editorial issues: work-order heading |
| 3 | Epistemology | [Inductive Invariance & Consistency](../epistemology/https-byteseismic-com-2024-04-10-inductive-invariance-conistency/) | review | 91 | 3 prompt sections are polish opportunities; editorial issues: work-order heading |
| 4 | Humanistic Philosophies | [Faith or Evidence?](../humanistic-philosophies/faith-or-evidence/) | review | 94 | 3 prompt sections are polish opportunities; editorial issues: work-order heading |
| 5 | Ethics | [Species-Dependent Mercy](../ethics/species-dependent-mercy/) | review | 100 | 3 prompt sections are polish opportunities; editorial issues: work-order heading |
| 6 | Humanistic Philosophies | [Deism & Theism](../humanistic-philosophies/deism-theism/) | review | 52 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 7 | Rational Thought | [The Primacy of Emotions](../rational-thought/the-primacy-of-emotions/) | review | 59 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 8 | Rational Thought | [What is “Design Thinking”?](../rational-thought/what-is-design-thinking/) | review | 65 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 9 | Introduction | [Are Philosophers Argumentative?](../introduction/are-philosophers-argumentative/) | review | 65 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 10 | Economics | [Micro/Macro Economics](../economics/micro-macro-economics/) | review | 68 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 11 | Economics | [Behavioral Economics](../economics/behavioral-economics/) | review | 68 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 12 | Economics | [Government Interventions](../economics/government-interventions/) | review | 68 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 13 | Rational Thought | [Are Averages “Not Always True”?](../rational-thought/are-averages-not-always-true/) | review | 71 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 14 | Rational Thought | [Fine-Tuned Rationality](../rational-thought/fine-tuned-rationality/) | review | 72 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 15 | Rational Thought | [Monetary Goals](../rational-thought/monetary-goals/) | review | 72 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 16 | Rational Thought | [The Power of Statistics](../rational-thought/the-power-of-statistics/) | review | 72 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 17 | Ethics | [Utility Functions](../ethics/utility-functions/) | review | 72 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 18 | Humanistic Philosophies | [Leaving Christianity](../humanistic-philosophies/leaving-christianity/) | review | 72 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 19 | Epistemology | [Charles Darwin](../epistemology/charles-darwin/) | review | 73 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 20 | Epistemology | [⌁ Perceived Responsibility and Perceived Control](../epistemology/perceived-responsibility-and-perceived-control/) | review | 75 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 21 | Ethics | [⌁ Bounded Compassionate Agency](../ethics/bounded-compassionate-agency/) | review | 75 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 22 | Ethics | [⌁ Scope Leakage of Happiness](../ethics/scope-leakage-of-happiness/) | review | 75 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 23 | Epistemology | [Many Logics?](../epistemology/many-logics/) | review | 75 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 24 | Economics | [Minimum Wage Thresholds](../economics/minimum-wage-thresholds/) | review | 76 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 25 | Ethics | [Recommendations vs Moral Claims](../ethics/recommendations-vs-moral-claims/) | review | 76 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 26 | Humanistic Philosophies | [What is Religion?](../humanistic-philosophies/what-is-religion/) | review | 76 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 27 | Introduction | [What is the Value of Philosophy?](../introduction/what-is-the-value-of-philosophy/) | review | 78 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 28 | Economics | [The 15-Hour Workweek](../economics/the-15-hour-workweek/) | review | 78 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 29 | Ethics | [Equivocation on “Wrong”](../ethics/equivocation-on-wrong/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 30 | Economics | [Homo Economicus](../economics/homo-economicus/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 31 | Philosophers | [Georg Wilhelm Friedrich Hegel](../philosophers/georg-wilhelm-friedrich-hegel/) | review | 79 | 1 prompt sections need review; 4 prompt sections need gap fill |
| 32 | Philosophy of Science | [What is Falsifiability?](../philosophy-of-science/what-is-falsifiability/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 33 | Rational Thought | [Tu Quoque or “You too!”](../rational-thought/tu-quoque-or-you-too/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 34 | Rational Thought | [⌁ Finite Agency in an Infinite Feed](../rational-thought/finite-agency-in-an-infinite-feed/) | review | 80 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 35 | Epistemology | [Case #2 – The Telephone Game](../epistemology/case-2-the-telephone-game/) | review | 80 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 36 | Ethics | [The Value Selection Hypothesis](../ethics/the-value-selection-hypothesis/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 37 | Ethics | [⌁ Legitimate Culpability vs Borrowed Guilt](../ethics/legitimate-culpability-vs-borrowed-guilt/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 38 | Ethics | [Competing Ethical Considerations](../ethics/competing-ethical-considerations/) | review | 81 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 39 | Ethics | [Moral Realism & Intuition](../ethics/moral-realism-intuition/) | review | 82 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 40 | Philosophy of Science | [What are Pseudosciences?](../philosophy-of-science/what-are-pseudosciences/) | review | 82 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 41 | Philosophers | [Jean-Paul Sartre](../philosophers/jean-paul-sartre/) | review | 83 | 1 prompt sections need review; 4 prompt sections need gap fill |
| 42 | Philosophy of Science | [The Value of Surveys](../philosophy-of-science/the-value-of-surveys/) | review | 83 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 43 | Epistemology | [AI Reasoning Case Study](../epistemology/ai-reasoning-case-study/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 44 | Epistemology | [Induction: Forecasting](../epistemology/induction-forecasting/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 45 | Rational Thought | [Sample Size & Margin of Error](../rational-thought/sample-size-margin-of-error/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 46 | Ethics | [Compassion vs Moral Systems](../ethics/compassion-vs-moral-systems/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 47 | Philosophers | [Herbert Marcuse](../philosophers/herbert-marcuse/) | gap-fill | 86 | 4 prompt sections need gap fill |
| 48 | Philosophers | [Ludwig Wittgenstein](../philosophers/ludwig-wittgenstein/) | gap-fill | 86 | 4 prompt sections need gap fill |
| 49 | Philosophers | [Simone de Beauvoir](../philosophers/simone-de-beauvoir/) | gap-fill | 86 | 4 prompt sections need gap fill |
| 50 | Philosophers | [Aristotle](../philosophers/aristotle/) | gap-fill | 90 | 4 prompt sections need gap fill |

## Upcoming Batch Preview

### Next +1: cycle 2, queue positions 51-100

- `gap-fill` 90 [Philosophers / Daniel Dennett](../philosophers/daniel-dennett/)
- `gap-fill` 90 [Philosophers / David Hume](../philosophers/david-hume/)
- `gap-fill` 90 [Philosophers / Plato](../philosophers/plato-2/)
- `gap-fill` 90 [Philosophers / René Descartes](../philosophers/rene-descartes/)
- `gap-fill` 90 [Philosophers / Socrates](../philosophers/socrates/)
- `gap-fill` 90 [Philosophers / Søren Kierkegaard](../philosophers/soren-kierkegaard/)
- `gap-fill` 93 [Philosophers / Bertrand Russell](../philosophers/bertrand-russell/)
- `gap-fill` 93 [Philosophers / Charles Sanders Peirce](../philosophers/charles-sanders-peirce/)
- `gap-fill` 93 [Philosophers / Jacques Derrida](../philosophers/jacques-derrida/)
- `gap-fill` 93 [Philosophers / John Locke](../philosophers/john-locke/)

### Next +2: cycle 2, queue positions 101-150

- `gap-fill` 100 [Philosophers / John Stuart Mill](../philosophers/john-stuart-mill/)
- `gap-fill` 100 [Philosophers / Judith Butler](../philosophers/judith-butler/)
- `gap-fill` 100 [Philosophers / Jurgen Habermas](../philosophers/jurgen-habermas/)
- `gap-fill` 100 [Philosophers / Karl Marx](../philosophers/karl-marx/)
- `gap-fill` 100 [Philosophers / Laozi](../philosophers/laozi/)
- `gap-fill` 100 [Philosophers / Maimonides](../philosophers/maimonides/)
- `gap-fill` 100 [Philosophers / Marcus Aurelius](../philosophers/marcus-aurelius/)
- `gap-fill` 100 [Philosophers / Mary Wollstonecraft](../philosophers/mary-wollstonecraft/)
- `gap-fill` 100 [Philosophers / Maurice Merleau-Ponty](../philosophers/maurice-merleau-ponty/)
- `gap-fill` 100 [Philosophers / Mencius](../philosophers/mencius/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 528
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 396
- review: 46
