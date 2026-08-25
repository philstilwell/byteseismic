# Byteseismic Editorial Audit Tracker

Generated: 2026-08-25
Batch size: 50 pages
Current cycle: 6
Current queue start: 251 of 346

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
| 251 | Ethics | [Value & Morality in Diversity?](../ethics/value-morality-in-diversity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 252 | Humanistic Philosophies | [Are Humans More Egoistic or Altruistic?](../humanistic-philosophies/are-humans-more-egoistic-or-altruistic/) | polish | 100 | 4 prompt sections are polish opportunities |
| 253 | Humanistic Philosophies | [Existentialism: Key Concepts](../humanistic-philosophies/existentialism-key-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 254 | Humanistic Philosophies | [New Manifestations of Theism](../humanistic-philosophies/new-manifestations-of-theism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 255 | Introduction | [Studying Philosophy: Resources](../introduction/studying-philosophy-resources/) | polish | 100 | 4 prompt sections are polish opportunities |
| 256 | Metaphysics | [A Taxonomy of Impossibilities](../metaphysics/a-taxonomy-of-impossibilities/) | polish | 100 | 4 prompt sections are polish opportunities |
| 257 | Metaphysics | [Are Quantum Physics “Spiritual”?](../metaphysics/are-quantum-physics-spiritual/) | polish | 100 | 4 prompt sections are polish opportunities |
| 258 | Metaphysics | [Could Mind be Fundamental?](../metaphysics/could-mind-be-fundamental/) | polish | 100 | 4 prompt sections are polish opportunities |
| 259 | Metaphysics | [Emergence](../metaphysics/emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 260 | Metaphysics | [Energy & Psychic Phenomena](../metaphysics/energy-psychic-phenomena/) | polish | 100 | 4 prompt sections are polish opportunities |
| 261 | Metaphysics | [Explanations](../metaphysics/explanations/) | polish | 100 | 4 prompt sections are polish opportunities |
| 262 | Metaphysics | [Matthew Pirkowski on Emergence](../metaphysics/matthew-pirkowski-on-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 263 | Metaphysics | [Metaphysics – Core Concepts](../metaphysics/metaphysics-core-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 264 | Metaphysics | [Ontological Domains](../metaphysics/ontological-domains/) | polish | 100 | 4 prompt sections are polish opportunities |
| 265 | Metaphysics | [Stuart Kauffman on Emergence](../metaphysics/stuart-kauffman-on-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 266 | Metaphysics | [The Principle of Sufficient Reason](../metaphysics/the-principle-of-sufficient-reason/) | polish | 100 | 4 prompt sections are polish opportunities |
| 267 | Miscellany | [Complexity Theory](../miscellany/complexity-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 268 | Miscellany | [Cross-Culture Emotional Dispositions](../miscellany/cross-culture-emotional-dispositions/) | polish | 100 | 4 prompt sections are polish opportunities |
| 269 | Miscellany | [David Krakauer on Complexity](../miscellany/david-krakauer-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 270 | Miscellany | [Domains of Aesthetics](../miscellany/domains-of-aesthetics/) | polish | 100 | 4 prompt sections are polish opportunities |
| 271 | Miscellany | [Flack & Mitchell on Complexity](../miscellany/flack-mitchell-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 272 | Miscellany | [Information Theory](../miscellany/information-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 273 | Miscellany | [Sara Walker on Life’s Emergence](../miscellany/sara-walker-on-lifes-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 274 | Miscellany | [The Fantastical & Historical Truth](../miscellany/the-fantastical-historical-truth/) | polish | 100 | 4 prompt sections are polish opportunities |
| 275 | Miscellany | [Zak Stein on Complexity](../miscellany/zak-stein-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 276 | Philosophical Inquiry | [Appreciating our Insignificance](../philosophical-inquiry/appreciating-our-insignificance/) | polish | 100 | 4 prompt sections are polish opportunities |
| 277 | Philosophical Inquiry | [Charitable Engagement](../philosophical-inquiry/charitable-engagement/) | polish | 100 | 4 prompt sections are polish opportunities |
| 278 | Philosophical Inquiry | [Dangers: Anti-Intellectualism](../philosophical-inquiry/dangers-anti-intellectualism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 279 | Philosophical Inquiry | [Dangers: Gaslighting](../philosophical-inquiry/dangers-gaslighting/) | polish | 100 | 4 prompt sections are polish opportunities |
| 280 | Philosophical Inquiry | [Dangers: Limits on Doubt](../philosophical-inquiry/dangers-limits-on-doubt/) | polish | 100 | 4 prompt sections are polish opportunities |
| 281 | Philosophical Inquiry | [Dangers: Removing the Impossible](../philosophical-inquiry/dangers-removing-the-impossible/) | polish | 100 | 4 prompt sections are polish opportunities |
| 282 | Philosophy of AI | [AI Censorship Case](../philosophy-of-ai/ai-censorship-case/) | polish | 100 | 4 prompt sections are polish opportunities |
| 283 | Philosophy of AI | [AI Meta-Post — Inner Monologues](../philosophy-of-ai/ai-meta-post-inner-monologues/) | polish | 100 | 4 prompt sections are polish opportunities |
| 284 | Philosophy of AI | [AI Meta-Post — Overreach](../philosophy-of-ai/ai-meta-post-overreach/) | polish | 100 | 4 prompt sections are polish opportunities |
| 285 | Philosophy of AI | [The Double Descent Phenomenon](../philosophy-of-ai/the-double-descent-phenomenon/) | polish | 100 | 4 prompt sections are polish opportunities |
| 286 | Philosophy of Language | [Abandoned Words](../philosophy-of-language/abandoned-words/) | polish | 100 | 4 prompt sections are polish opportunities |
| 287 | Philosophy of Language | [Connotative Equivocation](../philosophy-of-language/connotative-equivocation/) | polish | 100 | 4 prompt sections are polish opportunities |
| 288 | Philosophy of Language | [Language & the Brain](../philosophy-of-language/language-the-brain/) | polish | 100 | 4 prompt sections are polish opportunities |
| 289 | Philosophy of Language | [Linguistic Scaffolding](../philosophy-of-language/linguistic-scaffolding/) | polish | 100 | 4 prompt sections are polish opportunities |
| 290 | Philosophy of Language | [Needless Semantic Complexity](../philosophy-of-language/needless-semantic-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 291 | Philosophy of Language | [Nomological Density of Grammar](../philosophy-of-language/nomological-density-of-grammar/) | polish | 100 | 4 prompt sections are polish opportunities |
| 292 | Philosophy of Language | [The Power of Analogy](../philosophy-of-language/the-power-of-analogy/) | polish | 100 | 4 prompt sections are polish opportunities |
| 293 | Philosophy of Language | [Thought = Language?](../philosophy-of-language/thought-language/) | polish | 100 | 4 prompt sections are polish opportunities |
| 294 | Philosophy of Mind | [Are there Selfless Acts?](../philosophy-of-mind/are-there-selfless-acts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 295 | Philosophy of Mind | [Land Ownership](../philosophy-of-mind/land-ownership/) | polish | 100 | 4 prompt sections are polish opportunities |
| 296 | Philosophy of Mind | [Philosophy of Mind — Core Concepts](../philosophy-of-mind/philosophy-of-mind-core-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 297 | Philosophy of Mind | [Preferences = Pleasures?](../philosophy-of-mind/preferences-pleasures/) | polish | 100 | 4 prompt sections are polish opportunities |
| 298 | Philosophy of Science | [Confounding Variables](../philosophy-of-science/confounding-variables/) | polish | 100 | 4 prompt sections are polish opportunities |
| 299 | Philosophy of Science | [Hard vs Soft Sciences](../philosophy-of-science/hard-vs-soft-sciences/) | polish | 100 | 4 prompt sections are polish opportunities |
| 300 | Philosophy of Science | [History as Forensic Science](../philosophy-of-science/history-as-forensic-science/) | polish | 100 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 6, queue positions 301-346

- `polish` 100 [Philosophy of Science / Improving Science](../philosophy-of-science/improving-science/)
- `polish` 100 [Philosophy of Science / Inductive Density](../philosophy-of-science/inductive-density/)
- `polish` 100 [Philosophy of Science / Methodological Naturalism](../philosophy-of-science/methodological-naturalism/)
- `polish` 100 [Philosophy of Science / Orthogonality](../philosophy-of-science/orthogonality/)
- `polish` 100 [Philosophy of Science / P-Value Issues](../philosophy-of-science/p-value-issues/)
- `polish` 100 [Philosophy of Science / Philosophy of Science — Core Concepts](../philosophy-of-science/philosophy-of-science-core-concepts/)
- `polish` 100 [Philosophy of Science / The Notion of Laws](../philosophy-of-science/the-notion-of-laws/)
- `polish` 100 [Philosophy of Science / The Power of Convergence](../philosophy-of-science/the-power-of-convergence/)
- `polish` 100 [Philosophy of Science / The Use of Proxies](../philosophy-of-science/the-use-of-proxies/)
- `polish` 100 [Political Philosophy / Critical Race Theory](../political-philosophy/critical-race-theory/)

### Next +2: cycle 7, queue positions 1-50

- `review` 100 [Ethics / Assisted Suicide](../ethics/assisted-suicide/)
- `review` 58 [Metaphysics / Dualism vs Materialism](../metaphysics/dualismvsmaterialism/)
- `review` 64 [Philosophy of Mind / Manufacturer or Method?](../philosophy-of-mind/manufacturer-or-method/)
- `review` 68 [Philosophy of Language / Semantics: Convention vs Stipulation](../philosophy-of-language/semantics-convention-vs-stipulation/)
- `review` 68 [Humanistic Philosophies / Personal & Cosmic Meaning](../humanistic-philosophies/personal-cosmic-meaning/)
- `review` 68 [Philosophy of Language / Linguistic Abstraction](../philosophy-of-language/linguistic-abstraction/)
- `review` 68 [Philosophy of Language / The Linearity of Language](../philosophy-of-language/the-linearity-of-language/)
- `review` 68 [Introduction / Careers in Philosophy](../introduction/careers-in-philosophy/)
- `review` 71 [Philosophy of Mind / Assessing Mind with Mind](../philosophy-of-mind/assessing-mind-with-mind/)
- `review` 72 [Humanistic Philosophies / The Legitimacy of Divine Revelation](../humanistic-philosophies/the-legitimacy-of-divine-revelation/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 96
- Estimated batches per cycle: 7

- gap-fill: 82
- polish: 231
- review: 33
