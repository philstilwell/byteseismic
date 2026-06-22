# Byteseismic Editorial Audit Tracker

Generated: 2026-06-22
Batch size: 50 pages
Current cycle: 1
Current queue start: 447 of 528

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
| 447 | Philosophy of Mind | [IQ – Intelligence Quotient](../philosophy-of-mind/iq-intelligence-quotient/) | polish | 100 | 3 prompt sections are polish opportunities |
| 448 | Philosophy of Mind | [Knowledge & Cognition Asymmetry](../philosophy-of-mind/knowledge-cognition-asymmetry/) | polish | 100 | 3 prompt sections are polish opportunities |
| 449 | Philosophy of Mind | [Mother in My Brain](../philosophy-of-mind/mother-in-my-brain/) | polish | 100 | 3 prompt sections are polish opportunities |
| 450 | Philosophy of Mind | [Neurotypical & Neurodivergent Minds](../philosophy-of-mind/neurotypical-neurodivergent-minds/) | polish | 100 | 3 prompt sections are polish opportunities |
| 451 | Philosophy of Mind | [Subjectivity Constrained by the Objective](../philosophy-of-mind/subjectivity-constrained-by-the-objective/) | polish | 100 | 3 prompt sections are polish opportunities |
| 452 | Philosophy of Mind | [The Chemical Basis of Happiness](../philosophy-of-mind/the-chemical-basis-of-happiness/) | polish | 100 | 3 prompt sections are polish opportunities |
| 453 | Philosophy of Mind | [The Inertia of Comfort](../philosophy-of-mind/the-inertia-of-comfort/) | polish | 100 | 3 prompt sections are polish opportunities |
| 454 | Philosophy of Mind | [The Schizophrenic Mind](../philosophy-of-mind/the-schizophrenic-mind/) | polish | 100 | 3 prompt sections are polish opportunities |
| 455 | Philosophy of Science | [Bimodal Distributions](../philosophy-of-science/bimodal-distributions/) | polish | 100 | 3 prompt sections are polish opportunities |
| 456 | Philosophy of Science | [Case #1 – Intelligence & Political Leanings](../philosophy-of-science/case-1-intelligence-political-leanings/) | polish | 100 | 3 prompt sections are polish opportunities |
| 457 | Philosophy of Science | [Causal Chains](../philosophy-of-science/causal-chains/) | polish | 100 | 3 prompt sections are polish opportunities |
| 458 | Philosophy of Science | [Correlation Is Not Causation](../philosophy-of-science/correlation-is-not-causation/) | polish | 100 | 3 prompt sections are polish opportunities |
| 459 | Philosophy of Science | [Demarcation for Scientific Laws](../philosophy-of-science/demarcation-for-scientific-laws/) | polish | 100 | 3 prompt sections are polish opportunities |
| 460 | Philosophy of Science | [Life vs Non-Life](../philosophy-of-science/life-vs-non-life/) | polish | 100 | 3 prompt sections are polish opportunities |
| 461 | Philosophy of Science | [Overfitting in Scientific Models](../philosophy-of-science/overfitting-in-scientific-models/) | polish | 100 | 3 prompt sections are polish opportunities |
| 462 | Philosophy of Science | [Research Design Scenario #1](../philosophy-of-science/research-design-scenario-1/) | polish | 100 | 3 prompt sections are polish opportunities |
| 463 | Philosophy of Science | [Science and the Public](../philosophy-of-science/science-and-the-public/) | polish | 100 | 3 prompt sections are polish opportunities |
| 464 | Philosophy of Science | [Science vs Subjectivity](../philosophy-of-science/science-vs-subjectivity/) | polish | 100 | 3 prompt sections are polish opportunities |
| 465 | Philosophy of Science | [Scientific “Observations”](../philosophy-of-science/scientific-observations/) | polish | 100 | 3 prompt sections are polish opportunities |
| 466 | Philosophy of Science | [Technology Outpaces Theory](../philosophy-of-science/technology-outpaces-theory/) | polish | 100 | 3 prompt sections are polish opportunities |
| 467 | Philosophy of Science | [The Problem of Induction](../philosophy-of-science/the-problem-of-induction/) | polish | 100 | 3 prompt sections are polish opportunities |
| 468 | Philosophy of Science | [What is Deduction?](../philosophy-of-science/what-is-deduction/) | polish | 100 | 3 prompt sections are polish opportunities |
| 469 | Philosophy of Science | [What is Etiology?](../philosophy-of-science/what-is-etiology/) | polish | 100 | 3 prompt sections are polish opportunities |
| 470 | Political Philosophy | [AI & the US Political Divide](../political-philosophy/ai-the-us-political-divide/) | polish | 100 | 3 prompt sections are polish opportunities |
| 471 | Political Philosophy | [Electoral Systems](../political-philosophy/electoral-systems/) | polish | 100 | 3 prompt sections are polish opportunities |
| 472 | Political Philosophy | [Political Theory & Human Nature](../political-philosophy/political-theory-human-nature/) | polish | 100 | 3 prompt sections are polish opportunities |
| 473 | Political Philosophy | [Red, Blue, & Grey Tribes](../political-philosophy/red-blue-grey-tribes/) | polish | 100 | 3 prompt sections are polish opportunities |
| 474 | Rational Thought | [Attributions of Causation](../rational-thought/attributions-of-causation/) | polish | 100 | 3 prompt sections are polish opportunities |
| 475 | Rational Thought | [Case #1 – Seizures](../rational-thought/case-1-seizures/) | polish | 100 | 3 prompt sections are polish opportunities |
| 476 | Rational Thought | [Case #3 – Astrology](../rational-thought/case-3-astrology/) | polish | 100 | 3 prompt sections are polish opportunities |
| 477 | Rational Thought | [Case #5 – Grade Inflation](../rational-thought/case-5-grade-inflation/) | polish | 100 | 3 prompt sections are polish opportunities |
| 478 | Rational Thought | [Characteristics of Science Denial](../rational-thought/characteristics-of-science-denial/) | polish | 100 | 3 prompt sections are polish opportunities |
| 479 | Rational Thought | [Cognitive Threats to Rationality](../rational-thought/cognitive-threats-to-rationality/) | polish | 100 | 3 prompt sections are polish opportunities |
| 480 | Rational Thought | [Credencing](../rational-thought/credencing/) | polish | 100 | 3 prompt sections are polish opportunities |
| 481 | Rational Thought | [Detecting Bad Science](../rational-thought/detecting-bad-science/) | polish | 100 | 3 prompt sections are polish opportunities |
| 482 | Rational Thought | [False Equivalencies](../rational-thought/false-equivalencies/) | polish | 100 | 3 prompt sections are polish opportunities |
| 483 | Rational Thought | [Integrated Critical Thinking](../rational-thought/integrated-critical-thinking/) | polish | 100 | 3 prompt sections are polish opportunities |
| 484 | Rational Thought | [Leaving Room for Doubt](../rational-thought/leaving-room-for-doubt/) | polish | 100 | 3 prompt sections are polish opportunities |
| 485 | Rational Thought | [Life Choices](../rational-thought/life-choices/) | polish | 100 | 3 prompt sections are polish opportunities |
| 486 | Rational Thought | [Logic](../rational-thought/logic/) | polish | 100 | 3 prompt sections are polish opportunities |
| 487 | Rational Thought | [Rational Romance](../rational-thought/rational-romance/) | polish | 100 | 3 prompt sections are polish opportunities |
| 488 | Rational Thought | [Starting with Strong Basics](../rational-thought/starting-with-strong-basics/) | polish | 100 | 3 prompt sections are polish opportunities |
| 489 | Rational Thought | [The Illusion of Knowledge](../rational-thought/the-illusion-of-knowledge/) | polish | 100 | 3 prompt sections are polish opportunities |
| 490 | Rational Thought | [The Motive Fallacy](../rational-thought/the-motive-fallacy/) | polish | 100 | 3 prompt sections are polish opportunities |
| 491 | Rational Thought | [The Steppingstone Fallacy](../rational-thought/the-steppingstone-fallacy/) | polish | 100 | 3 prompt sections are polish opportunities |
| 492 | Economics | [Fiat Money](../economics/fiat-money/) | polish | 100 | 2 prompt sections are polish opportunities |
| 493 | Epistemology | [Case #3 – Core Rationality](../epistemology/case-3-core-rationality/) | polish | 100 | 2 prompt sections are polish opportunities |
| 494 | Epistemology | [Operational Epistemic Rigor](../epistemology/operational-epistemic-rigor/) | polish | 100 | 2 prompt sections are polish opportunities |
| 495 | Epistemology | [The Domain of “Proof”](../epistemology/the-domain-of-proof/) | polish | 100 | 2 prompt sections are polish opportunities |
| 496 | Epistemology | [The Web of Induction](../epistemology/the-web-of-induction/) | polish | 100 | 2 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 1, queue positions 497-528

- `polish` 100 [Epistemology / Types of Knowing](../epistemology/types-of-knowing/)
- `polish` 100 [Epistemology / Types of Reasoning](../epistemology/types-of-reasoning/)
- `polish` 100 [Epistemology / What is Epistemic Updating?](../epistemology/what-is-epistemic-updating/)
- `polish` 100 [Ethics / A History of Golden Rules](../ethics/a-history-of-golden-rules/)
- `polish` 100 [Ethics / Essay: Moral Anti-Realism](../ethics/essay-moral-anti-realism/)
- `polish` 100 [Ethics / Meta-Ethics Focus #1](../ethics/meta-ethics-focus-1/)
- `polish` 100 [Ethics / Meta-Ethics Focus #2](../ethics/meta-ethics-focus-2/)
- `polish` 100 [Ethics / Torturing Babies](../ethics/torturing-babies/)
- `polish` 100 [Humanistic Philosophies / Testing Prayer](../humanistic-philosophies/testing-prayer/)
- `polish` 100 [Introduction / Analogies to a Philosophical Life](../introduction/analogies-to-a-philosophical-life/)

### Next +2: cycle 2, queue positions 1-50

- `review` 84 [Humanistic Philosophies / Increasing Religious Humility](../humanistic-philosophies/increasing-religious-humility/)
- `review` 89 [Rational Thought / Where Framing Goes Awry](../rational-thought/where-framing-goes-awry/)
- `review` 91 [Epistemology / Inductive Invariance & Consistency](../epistemology/https-byteseismic-com-2024-04-10-inductive-invariance-conistency/)
- `review` 94 [Humanistic Philosophies / Faith or Evidence?](../humanistic-philosophies/faith-or-evidence/)
- `review` 100 [Ethics / Species-Dependent Mercy](../ethics/species-dependent-mercy/)
- `review` 52 [Humanistic Philosophies / Deism & Theism](../humanistic-philosophies/deism-theism/)
- `review` 59 [Rational Thought / The Primacy of Emotions](../rational-thought/the-primacy-of-emotions/)
- `review` 65 [Rational Thought / What is “Design Thinking”?](../rational-thought/what-is-design-thinking/)
- `review` 65 [Introduction / Are Philosophers Argumentative?](../introduction/are-philosophers-argumentative/)
- `review` 68 [Economics / Micro/Macro Economics](../economics/micro-macro-economics/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 82
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 396
- review: 46
