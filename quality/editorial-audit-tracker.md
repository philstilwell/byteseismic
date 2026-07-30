# Byteseismic Editorial Audit Tracker

Generated: 2026-07-30
Batch size: 50 pages
Current cycle: 5
Current queue start: 1 of 346

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
| 1 | Metaphysics | [Emergence](../metaphysics/emergence/) | review | 76 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 2 | Philosophy of AI | [AI Censorship Case](../philosophy-of-ai/ai-censorship-case/) | review | 84 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 3 | Miscellany | [Domains of Aesthetics](../miscellany/domains-of-aesthetics/) | review | 60 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 4 | Miscellany | [Complexity Theory](../miscellany/complexity-theory/) | review | 62 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 5 | Humanistic Philosophies | [Existentialism: Key Concepts](../humanistic-philosophies/existentialism-key-concepts/) | review | 63 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 6 | Humanistic Philosophies | [New Manifestations of Theism](../humanistic-philosophies/new-manifestations-of-theism/) | review | 68 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 7 | Metaphysics | [Ontological Domains](../metaphysics/ontological-domains/) | review | 68 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 8 | Philosophy of Language | [Needless Semantic Complexity](../philosophy-of-language/needless-semantic-complexity/) | review | 68 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 9 | Philosophy of Science | [Confounding Variables](../philosophy-of-science/confounding-variables/) | review | 68 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 10 | Philosophy of Language | [Abandoned Words](../philosophy-of-language/abandoned-words/) | review | 68 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 11 | Miscellany | [Sara Walker on Life’s Emergence](../miscellany/sara-walker-on-lifes-emergence/) | review | 70 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 12 | Miscellany | [Flack & Mitchell on Complexity](../miscellany/flack-mitchell-on-complexity/) | review | 70 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 13 | Miscellany | [Zak Stein on Complexity](../miscellany/zak-stein-on-complexity/) | review | 70 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 14 | Miscellany | [The Fantastical & Historical Truth](../miscellany/the-fantastical-historical-truth/) | review | 72 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 15 | Metaphysics | [Metaphysics – Core Concepts](../metaphysics/metaphysics-core-concepts/) | review | 72 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 16 | Philosophy of Mind | [Are there Selfless Acts?](../philosophy-of-mind/are-there-selfless-acts/) | review | 73 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 17 | Philosophy of Mind | [What is Consciousness?](../philosophy-of-mind/what-is-consciousness/) | review | 73 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 18 | Metaphysics | [Jeremy Sherman on Emergence](../metaphysics/jeremy-sherman-on-emergence/) | review | 73 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 19 | Philosophy of Science | [Hard vs Soft Sciences](../philosophy-of-science/hard-vs-soft-sciences/) | review | 74 | 3 prompt sections need review; 3 prompt sections need gap fill |
| 20 | Metaphysics | [Matthew Pirkowski on Emergence](../metaphysics/matthew-pirkowski-on-emergence/) | review | 75 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 21 | Philosophy of Mind | [Preferences = Pleasures?](../philosophy-of-mind/preferences-pleasures/) | review | 76 | 4 prompt sections need review; 4 prompt sections need gap fill |
| 22 | Metaphysics | [Could Mind be Fundamental?](../metaphysics/could-mind-be-fundamental/) | review | 76 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 23 | Miscellany | [Cross-Culture Emotional Dispositions](../miscellany/cross-culture-emotional-dispositions/) | review | 76 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 24 | Philosophical Inquiry | [Charitable Engagement](../philosophical-inquiry/charitable-engagement/) | review | 76 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 25 | Philosophy of Language | [Language & the Brain](../philosophy-of-language/language-the-brain/) | review | 76 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 26 | Metaphysics | [The Principle of Sufficient Reason](../metaphysics/the-principle-of-sufficient-reason/) | review | 76 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 27 | Philosophy of Language | [Linguistic Scaffolding](../philosophy-of-language/linguistic-scaffolding/) | review | 76 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 28 | Philosophy of Mind | [Philosophy of Mind — Core Concepts](../philosophy-of-mind/philosophy-of-mind-core-concepts/) | review | 77 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 29 | Introduction | [Studying Philosophy: Resources](../introduction/studying-philosophy-resources/) | review | 78 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 30 | Miscellany | [David Krakauer on Complexity](../miscellany/david-krakauer-on-complexity/) | review | 78 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 31 | Philosophy of AI | [AI Meta-Post — Inner Monologues](../philosophy-of-ai/ai-meta-post-inner-monologues/) | review | 78 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 32 | Humanistic Philosophies | [What is Existentialism?](../humanistic-philosophies/what-is-existentialism/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 33 | Philosophy of Mind | [Elitzur on Consciousness](../philosophy-of-mind/elitzur-on-consciousness/) | review | 78 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 34 | Epistemology | [Rationality Discussion](../epistemology/rationality-discussion/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 35 | Introduction | [Miscellaneous Philosophers](../introduction/miscellaneous-philosophers/) | review | 79 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 36 | Miscellany | [Information Theory](../miscellany/information-theory/) | review | 80 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 37 | Epistemology | [“Adequate” Evidence](../epistemology/adequate-evidence/) | review | 81 | 2 prompt sections need review; 2 prompt sections need gap fill |
| 38 | Philosophical Inquiry | [Dangers: Limits on Doubt](../philosophical-inquiry/dangers-limits-on-doubt/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 39 | Rational Thought | [1 at 99.5% or 5 at 95%?](../rational-thought/1-at-99-5-or-5-at-95/) | review | 84 | 1 prompt sections need review; 1 prompt sections need gap fill |
| 40 | Philosophers | [Daniel Dennett](../philosophers/daniel-dennett/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 41 | Philosophers | [David Hume](../philosophers/david-hume/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 42 | Philosophers | [Plato](../philosophers/plato-2/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 43 | Philosophers | [René Descartes](../philosophers/rene-descartes/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 44 | Philosophers | [Socrates](../philosophers/socrates/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 45 | Philosophers | [Søren Kierkegaard](../philosophers/soren-kierkegaard/) | gap-fill | 90 | 4 prompt sections need gap fill |
| 46 | Philosophers | [Bertrand Russell](../philosophers/bertrand-russell/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 47 | Philosophers | [Charles Sanders Peirce](../philosophers/charles-sanders-peirce/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 48 | Philosophers | [Jacques Derrida](../philosophers/jacques-derrida/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 49 | Philosophers | [John Locke](../philosophers/john-locke/) | gap-fill | 93 | 4 prompt sections need gap fill |
| 50 | Philosophers | [Thomas Aquinas](../philosophers/thomas-aquinas/) | gap-fill | 93 | 4 prompt sections need gap fill |

## Upcoming Batch Preview

### Next +1: cycle 5, queue positions 51-100

- `gap-fill` 95 [Philosophers / Immanuel Kant](../philosophers/immanuel-kant/)
- `gap-fill` 95 [Philosophers / Martin Heidegger](../philosophers/martin-heidegger/)
- `gap-fill` 95 [Philosophers / Thomas Hobbes](../philosophers/thomas-hobbes/)
- `gap-fill` 95 [Philosophers / Willard Van Orman Quine](../philosophers/willard-van-orman-quine/)
- `gap-fill` 97 [Philosophers / Baruch Spinoza](../philosophers/baruch-spinoza/)
- `gap-fill` 97 [Philosophers / Edmund Husserl](../philosophers/edmund-husserl/)
- `gap-fill` 97 [Philosophers / Epicurus](../philosophers/epicurus/)
- `gap-fill` 97 [Philosophers / Gottfried Wilhelm Leibniz](../philosophers/gottfried-wilhelm-leibniz/)
- `gap-fill` 98 [Philosophers / Empiricists](../philosophers/empiricists/)
- `gap-fill` 98 [Philosophers / Phenomenologists](../philosophers/phenomenologists/)

### Next +2: cycle 5, queue positions 101-150

- `gap-fill` 100 [Philosophers / Nagarjuna](../philosophers/nagarjuna/)
- `gap-fill` 100 [Philosophers / Niccolo Machiavelli](../philosophers/niccolo-machiavelli/)
- `gap-fill` 100 [Philosophers / Parmenides](../philosophers/parmenides/)
- `gap-fill` 100 [Philosophers / Plato](../philosophers/plato/)
- `gap-fill` 100 [Philosophers / Plotinus](../philosophers/plotinus/)
- `gap-fill` 100 [Philosophers / Pragmatists](../philosophers/pragmatists/)
- `gap-fill` 100 [Philosophers / Rationalists](../philosophers/rationalists/)
- `gap-fill` 100 [Philosophers / Saul Kripke](../philosophers/saul-kripke/)
- `gap-fill` 100 [Philosophers / Scholastics](../philosophers/scholastics/)
- `gap-fill` 100 [Philosophers / Seneca](../philosophers/seneca/)

## Summary

- Tracked pages: 346
- Pages remaining in current cycle: 346
- Estimated batches per cycle: 7

- gap-fill: 82
- polish: 225
- review: 39
