# Byteseismic Editorial Audit Tracker

Generated: 2026-06-20
Batch size: 50 pages
Current cycle: 1
Current queue start: 347 of 528

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
| 347 | Rational Thought | [Empathy Overload](../rational-thought/empathy-overload/) | polish | 100 | 4 prompt sections are polish opportunities |
| 348 | Rational Thought | [Factual Disagreements vs Semantic Misunderstandings](../rational-thought/factual-disagreements-vs-semantic-misunderstandings/) | polish | 100 | 4 prompt sections are polish opportunities |
| 349 | Rational Thought | [Fine-Tuned Rationality](../rational-thought/fine-tuned-rationality/) | polish | 100 | 4 prompt sections are polish opportunities |
| 350 | Rational Thought | [Monetary Goals](../rational-thought/monetary-goals/) | polish | 100 | 4 prompt sections are polish opportunities |
| 351 | Rational Thought | [The Power of Statistics](../rational-thought/the-power-of-statistics/) | polish | 100 | 4 prompt sections are polish opportunities |
| 352 | Rational Thought | [The Primacy of Emotions](../rational-thought/the-primacy-of-emotions/) | polish | 100 | 4 prompt sections are polish opportunities |
| 353 | Rational Thought | [Tu Quoque or “You too!”](../rational-thought/tu-quoque-or-you-too/) | polish | 100 | 4 prompt sections are polish opportunities |
| 354 | Rational Thought | [What is “Design Thinking”?](../rational-thought/what-is-design-thinking/) | polish | 100 | 4 prompt sections are polish opportunities |
| 355 | Rational Thought | [Where Framing Goes Awry](../rational-thought/where-framing-goes-awry/) | polish | 100 | 4 prompt sections are polish opportunities |
| 356 | Economics | [Behavioral Economics](../economics/behavioral-economics/) | polish | 100 | 3 prompt sections are polish opportunities |
| 357 | Economics | [Can Prices be “Unfair”?](../economics/can-prices-be-unfair/) | polish | 100 | 3 prompt sections are polish opportunities |
| 358 | Economics | [Deflationary Spiral for AI Projects](../economics/deflationary-spiral-for-ai-projects/) | polish | 100 | 3 prompt sections are polish opportunities |
| 359 | Economics | [Government Interventions](../economics/government-interventions/) | polish | 100 | 3 prompt sections are polish opportunities |
| 360 | Economics | [Homo Economicus](../economics/homo-economicus/) | polish | 100 | 3 prompt sections are polish opportunities |
| 361 | Economics | [Micro/Macro Economics](../economics/micro-macro-economics/) | polish | 100 | 3 prompt sections are polish opportunities |
| 362 | Economics | [Minimum Wage Thresholds](../economics/minimum-wage-thresholds/) | polish | 100 | 3 prompt sections are polish opportunities |
| 363 | Economics | [Salaries and Public Judgment](../economics/salaries-and-public-judgment/) | polish | 100 | 3 prompt sections are polish opportunities |
| 364 | Economics | [The 15-Hour Workweek](../economics/the-15-hour-workweek/) | polish | 100 | 3 prompt sections are polish opportunities |
| 365 | Economics | [Universal Basic Income](../economics/universal-basic-income/) | polish | 100 | 3 prompt sections are polish opportunities |
| 366 | Epistemology | [Establishing Cognitive Reliability (#2)](../epistemology/establishing-cognitive-reliability-2/) | polish | 100 | 3 prompt sections are polish opportunities |
| 367 | Epistemology | [Faith vs Science](../epistemology/faith-vs-science/) | polish | 100 | 3 prompt sections are polish opportunities |
| 368 | Epistemology | [I Don’t Know](../epistemology/i-dont-know/) | polish | 100 | 3 prompt sections are polish opportunities |
| 369 | Epistemology | [Inductive Invariance & Consistency](../epistemology/https-byteseismic-com-2024-04-10-inductive-invariance-conistency/) | polish | 100 | 3 prompt sections are polish opportunities |
| 370 | Epistemology | [Logic](../epistemology/logic/) | polish | 100 | 3 prompt sections are polish opportunities |
| 371 | Epistemology | [Recent Issues in Epistemology](../epistemology/recent-issues-in-epistemology/) | polish | 100 | 3 prompt sections are polish opportunities |
| 372 | Epistemology | [Shades of Certainty](../epistemology/shades-of-certainty/) | polish | 100 | 3 prompt sections are polish opportunities |
| 373 | Epistemology | [Swapping Ideologies](../epistemology/swapping-ideologies/) | polish | 100 | 3 prompt sections are polish opportunities |
| 374 | Epistemology | [Syllogistic Complexity](../epistemology/syllogistic-complexity/) | polish | 100 | 3 prompt sections are polish opportunities |
| 375 | Epistemology | [What is Epistemology?](../epistemology/what-is-epistemology/) | polish | 100 | 3 prompt sections are polish opportunities |
| 376 | Epistemology | [What is Knowledge?](../epistemology/what-is-knowledge/) | polish | 100 | 3 prompt sections are polish opportunities |
| 377 | Epistemology | [‘A Priori’ Knowledge Issues](../epistemology/a-priori-knowledge-issues/) | polish | 100 | 3 prompt sections are polish opportunities |
| 378 | Ethics | [Circularity in Moral Realism](../ethics/circularity-in-moral-realism/) | polish | 100 | 3 prompt sections are polish opportunities |
| 379 | Ethics | [Harris’ Notion of Morality](../ethics/harris-notion-of-morality/) | polish | 100 | 3 prompt sections are polish opportunities |
| 380 | Ethics | [Moral Realism & Intuition](../ethics/moral-realism-intuition/) | polish | 100 | 3 prompt sections are polish opportunities |
| 381 | Ethics | [Morality & Human Rights](../ethics/morality-human-rights/) | polish | 100 | 3 prompt sections are polish opportunities |
| 382 | Ethics | [Species-Dependent Mercy](../ethics/species-dependent-mercy/) | polish | 100 | 3 prompt sections are polish opportunities |
| 383 | Ethics | [Utility Functions](../ethics/utility-functions/) | polish | 100 | 3 prompt sections are polish opportunities |
| 384 | Humanistic Philosophies | [Anthropomorphized Gods](../humanistic-philosophies/anthropomorphized-gods/) | polish | 100 | 3 prompt sections are polish opportunities |
| 385 | Humanistic Philosophies | [Deism & Theism](../humanistic-philosophies/deism-theism/) | polish | 100 | 3 prompt sections are polish opportunities |
| 386 | Humanistic Philosophies | [Faith or Evidence?](../humanistic-philosophies/faith-or-evidence/) | polish | 100 | 3 prompt sections are polish opportunities |
| 387 | Humanistic Philosophies | [Increasing Religious Humility](../humanistic-philosophies/increasing-religious-humility/) | polish | 100 | 3 prompt sections are polish opportunities |
| 388 | Humanistic Philosophies | [Leaving Christianity](../humanistic-philosophies/leaving-christianity/) | polish | 100 | 3 prompt sections are polish opportunities |
| 389 | Humanistic Philosophies | [Religions](../humanistic-philosophies/religions/) | polish | 100 | 3 prompt sections are polish opportunities |
| 390 | Humanistic Philosophies | [Shoe-Tips & Hiddenness](../humanistic-philosophies/shoe-tips-hiddenness/) | polish | 100 | 3 prompt sections are polish opportunities |
| 391 | Humanistic Philosophies | [What is Religion?](../humanistic-philosophies/what-is-religion/) | polish | 100 | 3 prompt sections are polish opportunities |
| 392 | Humanistic Philosophies | [What is Stoicism?](../humanistic-philosophies/what-is-stoicism/) | polish | 100 | 3 prompt sections are polish opportunities |
| 393 | Introduction | [Are Philosophers Argumentative?](../introduction/are-philosophers-argumentative/) | polish | 100 | 3 prompt sections are polish opportunities |
| 394 | Introduction | [Philosophical Maturity](../introduction/philosophical-maturity/) | polish | 100 | 3 prompt sections are polish opportunities |
| 395 | Introduction | [What is the Value of Philosophy?](../introduction/what-is-the-value-of-philosophy/) | polish | 100 | 3 prompt sections are polish opportunities |
| 396 | Metaphysics | [Minimal Entities to reach Unfalsifiability](../metaphysics/minimal-entities-to-reach-unfalsifiability/) | polish | 100 | 3 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 1, queue positions 397-446

- `polish` 100 [Metaphysics / Objectively & Subjectively “Real”](../metaphysics/objectively-subjectively-real/)
- `polish` 100 [Metaphysics / Terrence Deacon on Emergence](../metaphysics/terrence-deacon-on-emergence/)
- `polish` 100 [Metaphysics / The Beginning of Time](../metaphysics/the-beginning-of-time/)
- `polish` 100 [Metaphysics / The Status of Evil](../metaphysics/the-status-of-evil/)
- `polish` 100 [Metaphysics / What is Metaphysics?](../metaphysics/what-is-metaphysics/)
- `polish` 100 [Miscellany / Assembly Theory](../miscellany/assembly-theory/)
- `polish` 100 [Miscellany / Cascading Factor Models](../miscellany/cascading-factor-models/)
- `polish` 100 [Miscellany / Dynamical Depth](../miscellany/dynamical-depth/)
- `polish` 100 [Miscellany / Profiling](../miscellany/profiling/)
- `polish` 100 [Miscellany / The Growing Disinclination for War](../miscellany/the-growing-disinclination-for-war/)

### Next +2: cycle 1, queue positions 447-496

- `polish` 100 [Philosophy of Mind / IQ – Intelligence Quotient](../philosophy-of-mind/iq-intelligence-quotient/)
- `polish` 100 [Philosophy of Mind / Knowledge & Cognition Asymmetry](../philosophy-of-mind/knowledge-cognition-asymmetry/)
- `polish` 100 [Philosophy of Mind / Mother in My Brain](../philosophy-of-mind/mother-in-my-brain/)
- `polish` 100 [Philosophy of Mind / Neurotypical & Neurodivergent Minds](../philosophy-of-mind/neurotypical-neurodivergent-minds/)
- `polish` 100 [Philosophy of Mind / Subjectivity Constrained by the Objective](../philosophy-of-mind/subjectivity-constrained-by-the-objective/)
- `polish` 100 [Philosophy of Mind / The Chemical Basis of Happiness](../philosophy-of-mind/the-chemical-basis-of-happiness/)
- `polish` 100 [Philosophy of Mind / The Inertia of Comfort](../philosophy-of-mind/the-inertia-of-comfort/)
- `polish` 100 [Philosophy of Mind / The Schizophrenic Mind](../philosophy-of-mind/the-schizophrenic-mind/)
- `polish` 100 [Philosophy of Science / Bimodal Distributions](../philosophy-of-science/bimodal-distributions/)
- `polish` 100 [Philosophy of Science / Case #1 – Intelligence & Political Leanings](../philosophy-of-science/case-1-intelligence-political-leanings/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 182
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 419
- review: 23
