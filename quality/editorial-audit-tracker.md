# Byteseismic Editorial Audit Tracker

Generated: 2026-09-06
Batch size: 50 pages
Current cycle: 7
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
| 251 | Epistemology | [Evidence Workshop](../epistemology/evidence-workshop/) | polish | 100 | 4 prompt sections are polish opportunities |
| 252 | Epistemology | [Hypostatic Illogic](../epistemology/hypostatic-illogic/) | polish | 100 | 4 prompt sections are polish opportunities |
| 253 | Epistemology | [Induction: Cold Reading](../epistemology/induction-cold-reading/) | polish | 100 | 4 prompt sections are polish opportunities |
| 254 | Epistemology | [Mapping Belief to Evidence](../epistemology/mapping-belief-to-evidence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 255 | Epistemology | [Non-Scientific Ways of Knowing](../epistemology/non-scientific-ways-of-knowing/) | polish | 100 | 4 prompt sections are polish opportunities |
| 256 | Epistemology | [The Primacy of Induction](../epistemology/the-primacy-of-induction/) | polish | 100 | 4 prompt sections are polish opportunities |
| 257 | Epistemology | [Vicious & Virtuous Circularity](../epistemology/vicious-virtuous-circularity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 258 | Epistemology | [What are Syllogisms?](../epistemology/what-are-syllogisms/) | polish | 100 | 4 prompt sections are polish opportunities |
| 259 | Epistemology | [What is Bayes Theorem?](../epistemology/what-is-bayes-theorem/) | polish | 100 | 4 prompt sections are polish opportunities |
| 260 | Epistemology | [What is Faith?](../epistemology/what-is-faith/) | polish | 100 | 4 prompt sections are polish opportunities |
| 261 | Ethics | [Assuming Objective Evil](../ethics/assuming-objective-evil/) | polish | 100 | 4 prompt sections are polish opportunities |
| 262 | Ethics | [Divine Command Theory](../ethics/divine-command-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 263 | Ethics | [Ethical Edge Case #1](../ethics/ethical-edge-case-1/) | polish | 100 | 4 prompt sections are polish opportunities |
| 264 | Ethics | [No Morality = Chaos?](../ethics/no-morality-chaos/) | polish | 100 | 4 prompt sections are polish opportunities |
| 265 | Ethics | [Trolley Problems](../ethics/trolley-problems/) | polish | 100 | 4 prompt sections are polish opportunities |
| 266 | Ethics | [Value & Morality in Diversity?](../ethics/value-morality-in-diversity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 267 | Humanistic Philosophies | [Are Humans More Egoistic or Altruistic?](../humanistic-philosophies/are-humans-more-egoistic-or-altruistic/) | polish | 100 | 4 prompt sections are polish opportunities |
| 268 | Humanistic Philosophies | [Existentialism: Key Concepts](../humanistic-philosophies/existentialism-key-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 269 | Humanistic Philosophies | [New Manifestations of Theism](../humanistic-philosophies/new-manifestations-of-theism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 270 | Introduction | [Studying Philosophy: Resources](../introduction/studying-philosophy-resources/) | polish | 100 | 4 prompt sections are polish opportunities |
| 271 | Metaphysics | [A Taxonomy of Impossibilities](../metaphysics/a-taxonomy-of-impossibilities/) | polish | 100 | 4 prompt sections are polish opportunities |
| 272 | Metaphysics | [Are Quantum Physics “Spiritual”?](../metaphysics/are-quantum-physics-spiritual/) | polish | 100 | 4 prompt sections are polish opportunities |
| 273 | Metaphysics | [Could Mind be Fundamental?](../metaphysics/could-mind-be-fundamental/) | polish | 100 | 4 prompt sections are polish opportunities |
| 274 | Metaphysics | [Emergence](../metaphysics/emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 275 | Metaphysics | [Energy & Psychic Phenomena](../metaphysics/energy-psychic-phenomena/) | polish | 100 | 4 prompt sections are polish opportunities |
| 276 | Metaphysics | [Explanations](../metaphysics/explanations/) | polish | 100 | 4 prompt sections are polish opportunities |
| 277 | Metaphysics | [Matthew Pirkowski on Emergence](../metaphysics/matthew-pirkowski-on-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 278 | Metaphysics | [Metaphysics – Core Concepts](../metaphysics/metaphysics-core-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 279 | Metaphysics | [Ontological Domains](../metaphysics/ontological-domains/) | polish | 100 | 4 prompt sections are polish opportunities |
| 280 | Metaphysics | [Stuart Kauffman on Emergence](../metaphysics/stuart-kauffman-on-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 281 | Metaphysics | [The Principle of Sufficient Reason](../metaphysics/the-principle-of-sufficient-reason/) | polish | 100 | 4 prompt sections are polish opportunities |
| 282 | Miscellany | [Cross-Culture Emotional Dispositions](../miscellany/cross-culture-emotional-dispositions/) | polish | 100 | 4 prompt sections are polish opportunities |
| 283 | Miscellany | [David Krakauer on Complexity](../miscellany/david-krakauer-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 284 | Miscellany | [Flack & Mitchell on Complexity](../miscellany/flack-mitchell-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 285 | Miscellany | [Information Theory](../miscellany/information-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 286 | Miscellany | [Sara Walker on Life’s Emergence](../miscellany/sara-walker-on-lifes-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 287 | Miscellany | [The Fantastical & Historical Truth](../miscellany/the-fantastical-historical-truth/) | polish | 100 | 4 prompt sections are polish opportunities |
| 288 | Miscellany | [Zak Stein on Complexity](../miscellany/zak-stein-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 289 | Philosophical Inquiry | [Appreciating our Insignificance](../philosophical-inquiry/appreciating-our-insignificance/) | polish | 100 | 4 prompt sections are polish opportunities |
| 290 | Philosophical Inquiry | [Charitable Engagement](../philosophical-inquiry/charitable-engagement/) | polish | 100 | 4 prompt sections are polish opportunities |
| 291 | Philosophical Inquiry | [Dangers: Anti-Intellectualism](../philosophical-inquiry/dangers-anti-intellectualism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 292 | Philosophical Inquiry | [Dangers: Gaslighting](../philosophical-inquiry/dangers-gaslighting/) | polish | 100 | 4 prompt sections are polish opportunities |
| 293 | Philosophical Inquiry | [Dangers: Limits on Doubt](../philosophical-inquiry/dangers-limits-on-doubt/) | polish | 100 | 4 prompt sections are polish opportunities |
| 294 | Philosophical Inquiry | [Dangers: Removing the Impossible](../philosophical-inquiry/dangers-removing-the-impossible/) | polish | 100 | 4 prompt sections are polish opportunities |
| 295 | Philosophy of AI | [AI Censorship Case](../philosophy-of-ai/ai-censorship-case/) | polish | 100 | 4 prompt sections are polish opportunities |
| 296 | Philosophy of AI | [AI Meta-Post — Inner Monologues](../philosophy-of-ai/ai-meta-post-inner-monologues/) | polish | 100 | 4 prompt sections are polish opportunities |
| 297 | Philosophy of AI | [AI Meta-Post — Overreach](../philosophy-of-ai/ai-meta-post-overreach/) | polish | 100 | 4 prompt sections are polish opportunities |
| 298 | Philosophy of AI | [The Double Descent Phenomenon](../philosophy-of-ai/the-double-descent-phenomenon/) | polish | 100 | 4 prompt sections are polish opportunities |
| 299 | Philosophy of Language | [Abandoned Words](../philosophy-of-language/abandoned-words/) | polish | 100 | 4 prompt sections are polish opportunities |
| 300 | Philosophy of Language | [Connotative Equivocation](../philosophy-of-language/connotative-equivocation/) | polish | 100 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 7, queue positions 301-346

- `polish` 100 [Philosophy of Language / Language & the Brain](../philosophy-of-language/language-the-brain/)
- `polish` 100 [Philosophy of Language / Linguistic Scaffolding](../philosophy-of-language/linguistic-scaffolding/)
- `polish` 100 [Philosophy of Language / Needless Semantic Complexity](../philosophy-of-language/needless-semantic-complexity/)
- `polish` 100 [Philosophy of Language / Nomological Density of Grammar](../philosophy-of-language/nomological-density-of-grammar/)
- `polish` 100 [Philosophy of Language / The Power of Analogy](../philosophy-of-language/the-power-of-analogy/)
- `polish` 100 [Philosophy of Language / Thought = Language?](../philosophy-of-language/thought-language/)
- `polish` 100 [Philosophy of Mind / Are there Selfless Acts?](../philosophy-of-mind/are-there-selfless-acts/)
- `polish` 100 [Philosophy of Mind / Land Ownership](../philosophy-of-mind/land-ownership/)
- `polish` 100 [Philosophy of Mind / Philosophy of Mind — Core Concepts](../philosophy-of-mind/philosophy-of-mind-core-concepts/)
- `polish` 100 [Philosophy of Mind / Preferences = Pleasures?](../philosophy-of-mind/preferences-pleasures/)

### Next +2: cycle 8, queue positions 1-50

- `review` 54 [Philosophers / Empiricists](../philosophers/empiricists/)
- `review` 60 [Philosophy of Mind / What is Consciousness?](../philosophy-of-mind/what-is-consciousness/)
- `review` 60 [Philosophers / Analytic Philosophers](../philosophers/analytic-philosophers/)
- `review` 60 [Philosophy of Science / The Use of Proxies](../philosophy-of-science/the-use-of-proxies/)
- `review` 60 [Philosophy of Science / Methodological Naturalism](../philosophy-of-science/methodological-naturalism/)
- `review` 62 [Philosophers / David Hume](../philosophers/david-hume/)
- `review` 62 [Philosophers / Baruch Spinoza](../philosophers/baruch-spinoza/)
- `review` 62 [Philosophers / Immanuel Kant](../philosophers/immanuel-kant/)
- `review` 64 [Political Philosophy / Critical Race Theory](../political-philosophy/critical-race-theory/)
- `review` 65 [Philosophers / Ancient Philosophers](../philosophers/ancient-philosophers/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 96
- Estimated batches per cycle: 7

- gap-fill: 63
- polish: 243
- review: 40
