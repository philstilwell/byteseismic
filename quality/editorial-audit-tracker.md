# Byteseismic Editorial Audit Tracker

Generated: 2026-06-21
Batch size: 50 pages
Current cycle: 1
Current queue start: 397 of 528

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
| 397 | Metaphysics | [Objectively & Subjectively “Real”](../metaphysics/objectively-subjectively-real/) | polish | 100 | 3 prompt sections are polish opportunities |
| 398 | Metaphysics | [Terrence Deacon on Emergence](../metaphysics/terrence-deacon-on-emergence/) | polish | 100 | 3 prompt sections are polish opportunities |
| 399 | Metaphysics | [The Beginning of Time](../metaphysics/the-beginning-of-time/) | polish | 100 | 3 prompt sections are polish opportunities |
| 400 | Metaphysics | [The Status of Evil](../metaphysics/the-status-of-evil/) | polish | 100 | 3 prompt sections are polish opportunities |
| 401 | Metaphysics | [What is Metaphysics?](../metaphysics/what-is-metaphysics/) | polish | 100 | 3 prompt sections are polish opportunities |
| 402 | Miscellany | [Assembly Theory](../miscellany/assembly-theory/) | polish | 100 | 3 prompt sections are polish opportunities |
| 403 | Miscellany | [Cascading Factor Models](../miscellany/cascading-factor-models/) | polish | 100 | 3 prompt sections are polish opportunities |
| 404 | Miscellany | [Dynamical Depth](../miscellany/dynamical-depth/) | polish | 100 | 3 prompt sections are polish opportunities |
| 405 | Miscellany | [Profiling](../miscellany/profiling/) | polish | 100 | 3 prompt sections are polish opportunities |
| 406 | Miscellany | [The Growing Disinclination for War](../miscellany/the-growing-disinclination-for-war/) | polish | 100 | 3 prompt sections are polish opportunities |
| 407 | Miscellany | [The Historical Method](../miscellany/the-historical-method/) | polish | 100 | 3 prompt sections are polish opportunities |
| 408 | Miscellany | [What is Axiology?](../miscellany/what-is-axiology/) | polish | 100 | 3 prompt sections are polish opportunities |
| 409 | Miscellany | [Wisdom Dynamics](../miscellany/wisdom-dynamics/) | polish | 100 | 3 prompt sections are polish opportunities |
| 410 | Philosophical Inquiry | [Authentic Humans](../philosophical-inquiry/authentic-humans/) | polish | 100 | 3 prompt sections are polish opportunities |
| 411 | Philosophical Inquiry | [Dangers: Awe as an Indicator](../philosophical-inquiry/dangers-awe-as-an-indicator/) | polish | 100 | 3 prompt sections are polish opportunities |
| 412 | Philosophical Inquiry | [Dangers: Dissipating Promises](../philosophical-inquiry/dangers-dissipating-promises/) | polish | 100 | 3 prompt sections are polish opportunities |
| 413 | Philosophical Inquiry | [Dangers: Egocentrism](../philosophical-inquiry/dangers-egocentrism/) | polish | 100 | 3 prompt sections are polish opportunities |
| 414 | Philosophical Inquiry | [Dangers: Explanatory Depth Illusions](../philosophical-inquiry/dangers-explanatory-depth-illusions/) | polish | 100 | 3 prompt sections are polish opportunities |
| 415 | Philosophical Inquiry | [Dangers: Promissory Treasures](../philosophical-inquiry/dangers-promissory-treasures/) | polish | 100 | 3 prompt sections are polish opportunities |
| 416 | Philosophical Inquiry | [Dangers: Siloed Ideologies](../philosophical-inquiry/dangers-siloed-ideologies/) | polish | 100 | 3 prompt sections are polish opportunities |
| 417 | Philosophical Inquiry | [Dangers: Vested Interests](../philosophical-inquiry/dangers-vested-interests/) | polish | 100 | 3 prompt sections are polish opportunities |
| 418 | Philosophical Inquiry | [Dangers: “Transcendent Meaning”](../philosophical-inquiry/dangers-transcendent-meaning/) | polish | 100 | 3 prompt sections are polish opportunities |
| 419 | Philosophical Inquiry | [Logic wherever Structure](../philosophical-inquiry/logic-wherever-structure/) | polish | 100 | 3 prompt sections are polish opportunities |
| 420 | Philosophical Inquiry | [Our View of Humanity](../philosophical-inquiry/our-view-of-humanity/) | polish | 100 | 3 prompt sections are polish opportunities |
| 421 | Philosophical Inquiry | [Philosophical Growth](../philosophical-inquiry/philosophical-growth/) | polish | 100 | 3 prompt sections are polish opportunities |
| 422 | Philosophy of AI | [AI Bias](../philosophy-of-ai/ai-bias/) | polish | 100 | 3 prompt sections are polish opportunities |
| 423 | Philosophy of AI | [AI Fact-Checking](../philosophy-of-ai/ai-fact-checking/) | polish | 100 | 3 prompt sections are polish opportunities |
| 424 | Philosophy of AI | [AI in Public Discourse](../philosophy-of-ai/ai-in-public-discourse/) | polish | 100 | 3 prompt sections are polish opportunities |
| 425 | Philosophy of AI | [AI in the Markets](../philosophy-of-ai/ai-in-the-markets/) | polish | 100 | 3 prompt sections are polish opportunities |
| 426 | Philosophy of AI | [AI Knowledge](../philosophy-of-ai/ai-knowledge/) | polish | 100 | 3 prompt sections are polish opportunities |
| 427 | Philosophy of AI | [AI Meta-Post — Pushback](../philosophy-of-ai/ai-meta-post-pushback/) | polish | 100 | 3 prompt sections are polish opportunities |
| 428 | Philosophy of AI | [AI Overconfidence](../philosophy-of-ai/ai-overconfidence/) | polish | 100 | 3 prompt sections are polish opportunities |
| 429 | Philosophy of AI | [AI Response to Pushback](../philosophy-of-ai/ai-response-to-pushback/) | polish | 100 | 3 prompt sections are polish opportunities |
| 430 | Philosophy of AI | [AIs in Politics](../philosophy-of-ai/ais-in-politics/) | polish | 100 | 3 prompt sections are polish opportunities |
| 431 | Philosophy of AI | [Chain-of-Thought Prompts](../philosophy-of-ai/chain-of-thought-prompts/) | polish | 100 | 3 prompt sections are polish opportunities |
| 432 | Philosophy of AI | [Confidentiality of LLM Weights](../philosophy-of-ai/confidentiality-of-llm-weights/) | polish | 100 | 3 prompt sections are polish opportunities |
| 433 | Philosophy of AI | [Precision Prompting](../philosophy-of-ai/precision-prompting/) | polish | 100 | 3 prompt sections are polish opportunities |
| 434 | Philosophy of AI | [Public Discourse & AI](../philosophy-of-ai/public-discourse-ai/) | polish | 100 | 3 prompt sections are polish opportunities |
| 435 | Philosophy of AI | [Quality Training Data](../philosophy-of-ai/quality-training-data/) | polish | 100 | 3 prompt sections are polish opportunities |
| 436 | Philosophy of AI | [Synthetic AI Data](../philosophy-of-ai/synthetic-ai-data/) | polish | 100 | 3 prompt sections are polish opportunities |
| 437 | Philosophy of AI | [The Credibility of AI](../philosophy-of-ai/the-credibility-of-ai/) | polish | 100 | 3 prompt sections are polish opportunities |
| 438 | Philosophy of AI | [What is the Philosophy of AI?](../philosophy-of-ai/what-is-the-philosophy-of-ai/) | polish | 100 | 3 prompt sections are polish opportunities |
| 439 | Philosophy of Language | [Binarizing Gradient Concepts](../philosophy-of-language/binarizing-gradient-concepts/) | polish | 100 | 3 prompt sections are polish opportunities |
| 440 | Philosophy of Language | [Can Words Constitute Violence?](../philosophy-of-language/can-words-constitute-violence/) | polish | 100 | 3 prompt sections are polish opportunities |
| 441 | Philosophy of Language | [Chomsky & AI](../philosophy-of-language/chomsky-ai/) | polish | 100 | 3 prompt sections are polish opportunities |
| 442 | Philosophy of Language | [Functional/Aesthetic Languages](../philosophy-of-language/functional-aesthetic-languages/) | polish | 100 | 3 prompt sections are polish opportunities |
| 443 | Philosophy of Language | [Living By Metaphor](../philosophy-of-language/living-by-metaphor/) | polish | 100 | 3 prompt sections are polish opportunities |
| 444 | Philosophy of Language | [Vague Tags of Identification](../philosophy-of-language/vague-tags-of-identification/) | polish | 100 | 3 prompt sections are polish opportunities |
| 445 | Philosophy of Language | [“Normative”](../philosophy-of-language/normative/) | polish | 100 | 3 prompt sections are polish opportunities |
| 446 | Philosophy of Mind | [IQ & Evolution](../philosophy-of-mind/iq-evolution/) | polish | 100 | 3 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 1, queue positions 447-496

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

### Next +2: cycle 1, queue positions 497-528

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

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 132
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 396
- review: 46
