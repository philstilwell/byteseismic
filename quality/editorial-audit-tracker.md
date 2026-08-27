# Byteseismic Editorial Audit Tracker

Generated: 2026-08-27
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
| 135 | Ethics | [Value & Morality in Diversity?](../ethics/value-morality-in-diversity/) | polish | 90 | 4 prompt sections are polish opportunities |
| 294 | Humanistic Philosophies | [Are Humans More Egoistic or Altruistic?](../humanistic-philosophies/are-humans-more-egoistic-or-altruistic/) | polish | 100 | 4 prompt sections are polish opportunities |
| 3 | Humanistic Philosophies | [Existentialism: Key Concepts](../humanistic-philosophies/existentialism-key-concepts/) | review | 55 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 9 | Humanistic Philosophies | [New Manifestations of Theism](../humanistic-philosophies/new-manifestations-of-theism/) | review | 68 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 19 | Introduction | [Studying Philosophy: Resources](../introduction/studying-philosophy-resources/) | review | 73 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 142 | Metaphysics | [A Taxonomy of Impossibilities](../metaphysics/a-taxonomy-of-impossibilities/) | polish | 92 | 4 prompt sections are polish opportunities |
| 155 | Metaphysics | [Are Quantum Physics “Spiritual”?](../metaphysics/are-quantum-physics-spiritual/) | polish | 94 | 4 prompt sections are polish opportunities |
| 25 | Metaphysics | [Could Mind be Fundamental?](../metaphysics/could-mind-be-fundamental/) | review | 76 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 1 | Metaphysics | [Emergence](../metaphysics/emergence/) | review | 76 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 295 | Metaphysics | [Energy & Psychic Phenomena](../metaphysics/energy-psychic-phenomena/) | polish | 100 | 4 prompt sections are polish opportunities |
| 156 | Metaphysics | [Explanations](../metaphysics/explanations/) | polish | 94 | 4 prompt sections are polish opportunities |
| 23 | Metaphysics | [Matthew Pirkowski on Emergence](../metaphysics/matthew-pirkowski-on-emergence/) | review | 75 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 17 | Metaphysics | [Metaphysics – Core Concepts](../metaphysics/metaphysics-core-concepts/) | review | 72 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 10 | Metaphysics | [Ontological Domains](../metaphysics/ontological-domains/) | review | 68 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 137 | Metaphysics | [Stuart Kauffman on Emergence](../metaphysics/stuart-kauffman-on-emergence/) | polish | 91 | 4 prompt sections are polish opportunities |
| 28 | Metaphysics | [The Principle of Sufficient Reason](../metaphysics/the-principle-of-sufficient-reason/) | review | 76 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 7 | Miscellany | [Complexity Theory](../miscellany/complexity-theory/) | review | 62 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 26 | Miscellany | [Cross-Culture Emotional Dispositions](../miscellany/cross-culture-emotional-dispositions/) | review | 76 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 30 | Miscellany | [David Krakauer on Complexity](../miscellany/david-krakauer-on-complexity/) | review | 78 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 4 | Miscellany | [Domains of Aesthetics](../miscellany/domains-of-aesthetics/) | review | 60 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 8 | Miscellany | [Flack & Mitchell on Complexity](../miscellany/flack-mitchell-on-complexity/) | review | 62 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 36 | Miscellany | [Information Theory](../miscellany/information-theory/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 14 | Miscellany | [Sara Walker on Life’s Emergence](../miscellany/sara-walker-on-lifes-emergence/) | review | 70 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 16 | Miscellany | [The Fantastical & Historical Truth](../miscellany/the-fantastical-historical-truth/) | review | 72 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 15 | Miscellany | [Zak Stein on Complexity](../miscellany/zak-stein-on-complexity/) | review | 70 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 296 | Philosophical Inquiry | [Appreciating our Insignificance](../philosophical-inquiry/appreciating-our-insignificance/) | polish | 100 | 4 prompt sections are polish opportunities |
| 27 | Philosophical Inquiry | [Charitable Engagement](../philosophical-inquiry/charitable-engagement/) | review | 76 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 138 | Philosophical Inquiry | [Dangers: Anti-Intellectualism](../philosophical-inquiry/dangers-anti-intellectualism/) | polish | 91 | 4 prompt sections are polish opportunities |
| 157 | Philosophical Inquiry | [Dangers: Gaslighting](../philosophical-inquiry/dangers-gaslighting/) | polish | 94 | 4 prompt sections are polish opportunities |
| 38 | Philosophical Inquiry | [Dangers: Limits on Doubt](../philosophical-inquiry/dangers-limits-on-doubt/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 297 | Philosophical Inquiry | [Dangers: Removing the Impossible](../philosophical-inquiry/dangers-removing-the-impossible/) | polish | 100 | 4 prompt sections are polish opportunities |
| 2 | Philosophy of AI | [AI Censorship Case](../philosophy-of-ai/ai-censorship-case/) | review | 76 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 31 | Philosophy of AI | [AI Meta-Post — Inner Monologues](../philosophy-of-ai/ai-meta-post-inner-monologues/) | review | 78 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 144 | Philosophy of AI | [AI Meta-Post — Overreach](../philosophy-of-ai/ai-meta-post-overreach/) | polish | 92 | 4 prompt sections are polish opportunities |
| 298 | Philosophy of AI | [The Double Descent Phenomenon](../philosophy-of-ai/the-double-descent-phenomenon/) | polish | 100 | 4 prompt sections are polish opportunities |
| 6 | Philosophy of Language | [Abandoned Words](../philosophy-of-language/abandoned-words/) | review | 60 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 186 | Philosophy of Language | [Connotative Equivocation](../philosophy-of-language/connotative-equivocation/) | polish | 98 | 4 prompt sections are polish opportunities |
| 24 | Philosophy of Language | [Language & the Brain](../philosophy-of-language/language-the-brain/) | review | 76 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 12 | Philosophy of Language | [Linguistic Scaffolding](../philosophy-of-language/linguistic-scaffolding/) | review | 68 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 11 | Philosophy of Language | [Needless Semantic Complexity](../philosophy-of-language/needless-semantic-complexity/) | review | 68 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 299 | Philosophy of Language | [Nomological Density of Grammar](../philosophy-of-language/nomological-density-of-grammar/) | polish | 100 | 4 prompt sections are polish opportunities |
| 158 | Philosophy of Language | [The Power of Analogy](../philosophy-of-language/the-power-of-analogy/) | polish | 94 | 4 prompt sections are polish opportunities |
| 130 | Philosophy of Language | [Thought = Language?](../philosophy-of-language/thought-language/) | polish | 89 | 4 prompt sections are polish opportunities |
| 18 | Philosophy of Mind | [Are there Selfless Acts?](../philosophy-of-mind/are-there-selfless-acts/) | review | 73 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 176 | Philosophy of Mind | [Land Ownership](../philosophy-of-mind/land-ownership/) | polish | 97 | 4 prompt sections are polish opportunities |
| 29 | Philosophy of Mind | [Philosophy of Mind — Core Concepts](../philosophy-of-mind/philosophy-of-mind-core-concepts/) | review | 77 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 13 | Philosophy of Mind | [Preferences = Pleasures?](../philosophy-of-mind/preferences-pleasures/) | review | 70 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 5 | Philosophy of Science | [Confounding Variables](../philosophy-of-science/confounding-variables/) | review | 60 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 22 | Philosophy of Science | [Hard vs Soft Sciences](../philosophy-of-science/hard-vs-soft-sciences/) | review | 74 | 3 prompt sections need review; 3 prompt sections need gap fill |
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

- `review` 76 [Metaphysics / Emergence](../metaphysics/emergence/)
- `review` 76 [Philosophy of AI / AI Censorship Case](../philosophy-of-ai/ai-censorship-case/)
- `review` 55 [Humanistic Philosophies / Existentialism: Key Concepts](../humanistic-philosophies/existentialism-key-concepts/)
- `review` 60 [Miscellany / Domains of Aesthetics](../miscellany/domains-of-aesthetics/)
- `review` 60 [Philosophy of Science / Confounding Variables](../philosophy-of-science/confounding-variables/)
- `review` 60 [Philosophy of Language / Abandoned Words](../philosophy-of-language/abandoned-words/)
- `review` 62 [Miscellany / Complexity Theory](../miscellany/complexity-theory/)
- `review` 62 [Miscellany / Flack & Mitchell on Complexity](../miscellany/flack-mitchell-on-complexity/)
- `review` 68 [Humanistic Philosophies / New Manifestations of Theism](../humanistic-philosophies/new-manifestations-of-theism/)
- `review` 68 [Metaphysics / Ontological Domains](../metaphysics/ontological-domains/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 96
- Estimated batches per cycle: 7

- gap-fill: 82
- polish: 225
- review: 39
