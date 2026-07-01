# Byteseismic Editorial Audit Tracker

Generated: 2026-07-01
Batch size: 50 pages
Current cycle: 2
Current queue start: 301 of 528

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
| 301 | Epistemology | [Evidence Workshop](../epistemology/evidence-workshop/) | polish | 100 | 4 prompt sections are polish opportunities |
| 302 | Epistemology | [Hypostatic Illogic](../epistemology/hypostatic-illogic/) | polish | 100 | 4 prompt sections are polish opportunities |
| 303 | Epistemology | [Induction: Cold Reading](../epistemology/induction-cold-reading/) | polish | 100 | 4 prompt sections are polish opportunities |
| 304 | Epistemology | [Mapping Belief to Evidence](../epistemology/mapping-belief-to-evidence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 305 | Epistemology | [Non-Scientific Ways of Knowing](../epistemology/non-scientific-ways-of-knowing/) | polish | 100 | 4 prompt sections are polish opportunities |
| 306 | Epistemology | [The Primacy of Induction](../epistemology/the-primacy-of-induction/) | polish | 100 | 4 prompt sections are polish opportunities |
| 307 | Epistemology | [Vicious & Virtuous Circularity](../epistemology/vicious-virtuous-circularity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 308 | Epistemology | [What are Syllogisms?](../epistemology/what-are-syllogisms/) | polish | 100 | 4 prompt sections are polish opportunities |
| 309 | Epistemology | [What is Bayes Theorem?](../epistemology/what-is-bayes-theorem/) | polish | 100 | 4 prompt sections are polish opportunities |
| 310 | Epistemology | [What is Faith?](../epistemology/what-is-faith/) | polish | 100 | 4 prompt sections are polish opportunities |
| 311 | Ethics | [Assuming Objective Evil](../ethics/assuming-objective-evil/) | polish | 100 | 4 prompt sections are polish opportunities |
| 312 | Ethics | [Divine Command Theory](../ethics/divine-command-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 313 | Ethics | [Ethical Edge Case #1](../ethics/ethical-edge-case-1/) | polish | 100 | 4 prompt sections are polish opportunities |
| 314 | Ethics | [No Morality = Chaos?](../ethics/no-morality-chaos/) | polish | 100 | 4 prompt sections are polish opportunities |
| 315 | Ethics | [Trolley Problems](../ethics/trolley-problems/) | polish | 100 | 4 prompt sections are polish opportunities |
| 316 | Ethics | [Value & Morality in Diversity?](../ethics/value-morality-in-diversity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 317 | Humanistic Philosophies | [Are Humans More Egoistic or Altruistic?](../humanistic-philosophies/are-humans-more-egoistic-or-altruistic/) | polish | 100 | 4 prompt sections are polish opportunities |
| 318 | Humanistic Philosophies | [Existentialism: Key Concepts](../humanistic-philosophies/existentialism-key-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 319 | Humanistic Philosophies | [New Manifestations of Theism](../humanistic-philosophies/new-manifestations-of-theism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 320 | Introduction | [Studying Philosophy: Resources](../introduction/studying-philosophy-resources/) | polish | 100 | 4 prompt sections are polish opportunities |
| 321 | Metaphysics | [A Taxonomy of Impossibilities](../metaphysics/a-taxonomy-of-impossibilities/) | polish | 100 | 4 prompt sections are polish opportunities |
| 322 | Metaphysics | [Are Quantum Physics “Spiritual”?](../metaphysics/are-quantum-physics-spiritual/) | polish | 100 | 4 prompt sections are polish opportunities |
| 323 | Metaphysics | [Could Mind be Fundamental?](../metaphysics/could-mind-be-fundamental/) | polish | 100 | 4 prompt sections are polish opportunities |
| 324 | Metaphysics | [Emergence](../metaphysics/emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 325 | Metaphysics | [Energy & Psychic Phenomena](../metaphysics/energy-psychic-phenomena/) | polish | 100 | 4 prompt sections are polish opportunities |
| 326 | Metaphysics | [Explanations](../metaphysics/explanations/) | polish | 100 | 4 prompt sections are polish opportunities |
| 327 | Metaphysics | [Matthew Pirkowski on Emergence](../metaphysics/matthew-pirkowski-on-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 328 | Metaphysics | [Metaphysics – Core Concepts](../metaphysics/metaphysics-core-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 329 | Metaphysics | [Ontological Domains](../metaphysics/ontological-domains/) | polish | 100 | 4 prompt sections are polish opportunities |
| 330 | Metaphysics | [Stuart Kauffman on Emergence](../metaphysics/stuart-kauffman-on-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 331 | Metaphysics | [The Principle of Sufficient Reason](../metaphysics/the-principle-of-sufficient-reason/) | polish | 100 | 4 prompt sections are polish opportunities |
| 332 | Miscellany | [Complexity Theory](../miscellany/complexity-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 333 | Miscellany | [Cross-Culture Emotional Dispositions](../miscellany/cross-culture-emotional-dispositions/) | polish | 100 | 4 prompt sections are polish opportunities |
| 334 | Miscellany | [David Krakauer on Complexity](../miscellany/david-krakauer-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 335 | Miscellany | [Domains of Aesthetics](../miscellany/domains-of-aesthetics/) | polish | 100 | 4 prompt sections are polish opportunities |
| 336 | Miscellany | [Flack & Mitchell on Complexity](../miscellany/flack-mitchell-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 337 | Miscellany | [Information Theory](../miscellany/information-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 338 | Miscellany | [Sara Walker on Life’s Emergence](../miscellany/sara-walker-on-lifes-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 339 | Miscellany | [The Fantastical & Historical Truth](../miscellany/the-fantastical-historical-truth/) | polish | 100 | 4 prompt sections are polish opportunities |
| 340 | Miscellany | [Zak Stein on Complexity](../miscellany/zak-stein-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 341 | Philosophical Inquiry | [Appreciating our Insignificance](../philosophical-inquiry/appreciating-our-insignificance/) | polish | 100 | 4 prompt sections are polish opportunities |
| 342 | Philosophical Inquiry | [Charitable Engagement](../philosophical-inquiry/charitable-engagement/) | polish | 100 | 4 prompt sections are polish opportunities |
| 343 | Philosophical Inquiry | [Dangers: Anti-Intellectualism](../philosophical-inquiry/dangers-anti-intellectualism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 344 | Philosophical Inquiry | [Dangers: Gaslighting](../philosophical-inquiry/dangers-gaslighting/) | polish | 100 | 4 prompt sections are polish opportunities |
| 345 | Philosophical Inquiry | [Dangers: Limits on Doubt](../philosophical-inquiry/dangers-limits-on-doubt/) | polish | 100 | 4 prompt sections are polish opportunities |
| 346 | Philosophical Inquiry | [Dangers: Removing the Impossible](../philosophical-inquiry/dangers-removing-the-impossible/) | polish | 100 | 4 prompt sections are polish opportunities |
| 347 | Philosophy of AI | [AI Censorship Case](../philosophy-of-ai/ai-censorship-case/) | polish | 100 | 4 prompt sections are polish opportunities |
| 348 | Philosophy of AI | [AI Meta-Post — Inner Monologues](../philosophy-of-ai/ai-meta-post-inner-monologues/) | polish | 100 | 4 prompt sections are polish opportunities |
| 349 | Philosophy of AI | [AI Meta-Post — Overreach](../philosophy-of-ai/ai-meta-post-overreach/) | polish | 100 | 4 prompt sections are polish opportunities |
| 350 | Philosophy of AI | [The Double Descent Phenomenon](../philosophy-of-ai/the-double-descent-phenomenon/) | polish | 100 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 2, queue positions 351-400

- `polish` 100 [Philosophy of Language / Abandoned Words](../philosophy-of-language/abandoned-words/)
- `polish` 100 [Philosophy of Language / Connotative Equivocation](../philosophy-of-language/connotative-equivocation/)
- `polish` 100 [Philosophy of Language / Language & the Brain](../philosophy-of-language/language-the-brain/)
- `polish` 100 [Philosophy of Language / Linguistic Scaffolding](../philosophy-of-language/linguistic-scaffolding/)
- `polish` 100 [Philosophy of Language / Needless Semantic Complexity](../philosophy-of-language/needless-semantic-complexity/)
- `polish` 100 [Philosophy of Language / Nomological Density of Grammar](../philosophy-of-language/nomological-density-of-grammar/)
- `polish` 100 [Philosophy of Language / The Power of Analogy](../philosophy-of-language/the-power-of-analogy/)
- `polish` 100 [Philosophy of Language / Thought = Language?](../philosophy-of-language/thought-language/)
- `polish` 100 [Philosophy of Mind / Are there Selfless Acts?](../philosophy-of-mind/are-there-selfless-acts/)
- `polish` 100 [Philosophy of Mind / Land Ownership](../philosophy-of-mind/land-ownership/)

### Next +2: cycle 2, queue positions 401-450

- `polish` 100 [Metaphysics / What is Metaphysics?](../metaphysics/what-is-metaphysics/)
- `polish` 100 [Miscellany / Assembly Theory](../miscellany/assembly-theory/)
- `polish` 100 [Miscellany / Cascading Factor Models](../miscellany/cascading-factor-models/)
- `polish` 100 [Miscellany / Dynamical Depth](../miscellany/dynamical-depth/)
- `polish` 100 [Miscellany / Profiling](../miscellany/profiling/)
- `polish` 100 [Miscellany / The Growing Disinclination for War](../miscellany/the-growing-disinclination-for-war/)
- `polish` 100 [Miscellany / The Historical Method](../miscellany/the-historical-method/)
- `polish` 100 [Miscellany / What is Axiology?](../miscellany/what-is-axiology/)
- `polish` 100 [Miscellany / Wisdom Dynamics](../miscellany/wisdom-dynamics/)
- `polish` 100 [Philosophical Inquiry / Authentic Humans](../philosophical-inquiry/authentic-humans/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 228
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 396
- review: 46
