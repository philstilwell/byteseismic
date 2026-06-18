# Byteseismic Editorial Audit Tracker

Generated: 2026-06-18
Batch size: 50 pages
Current cycle: 1
Current queue start: 247 of 528

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
| 247 | Rational Thought | [What is Rational Thought?](../rational-thought/what-is-rational-thought/) | polish | 100 | 5 prompt sections are polish opportunities |
| 248 | Economics | [A Living Wage](../economics/a-living-wage/) | polish | 100 | 4 prompt sections are polish opportunities |
| 249 | Economics | [AI & the Future of Work](../economics/ai-the-future-of-work/) | polish | 100 | 4 prompt sections are polish opportunities |
| 250 | Economics | [Business Risks](../economics/business-risks/) | polish | 100 | 4 prompt sections are polish opportunities |
| 251 | Economics | [Economic Complexity](../economics/economic-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 252 | Economics | [Economic Entitlements](../economics/economic-entitlements/) | polish | 100 | 4 prompt sections are polish opportunities |
| 253 | Economics | [Economic Optimism](../economics/economic-optimism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 254 | Economics | [Innovation Attractors](../economics/innovation-attractors/) | polish | 100 | 4 prompt sections are polish opportunities |
| 255 | Economics | [Justified Optimism](../economics/justified-optimism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 256 | Economics | [The Poverty Line](../economics/the-poverty-line/) | polish | 100 | 4 prompt sections are polish opportunities |
| 257 | Economics | [What Makes Economics “Dismal”?](../economics/what-makes-economics-dismal/) | polish | 100 | 4 prompt sections are polish opportunities |
| 258 | Epistemology | [Absolute Certainty](../epistemology/absolute-certainty/) | polish | 100 | 4 prompt sections are polish opportunities |
| 259 | Epistemology | [Case #5 – Vanishing Probabilities](../epistemology/case-5-vanishing-probabilities/) | polish | 100 | 4 prompt sections are polish opportunities |
| 260 | Epistemology | [Cromwell’s Rule](../epistemology/cromwells-rule/) | polish | 100 | 4 prompt sections are polish opportunities |
| 261 | Epistemology | [Establishing Cognitive Reliability (#1)](../epistemology/establishing-cognitive-reliability-1/) | polish | 100 | 4 prompt sections are polish opportunities |
| 262 | Epistemology | [Evidence Workshop](../epistemology/evidence-workshop/) | polish | 100 | 4 prompt sections are polish opportunities |
| 263 | Epistemology | [Hypostatic Illogic](../epistemology/hypostatic-illogic/) | polish | 100 | 4 prompt sections are polish opportunities |
| 264 | Epistemology | [Induction: Cold Reading](../epistemology/induction-cold-reading/) | polish | 100 | 4 prompt sections are polish opportunities |
| 265 | Epistemology | [Mapping Belief to Evidence](../epistemology/mapping-belief-to-evidence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 266 | Epistemology | [Non-Scientific Ways of Knowing](../epistemology/non-scientific-ways-of-knowing/) | polish | 100 | 4 prompt sections are polish opportunities |
| 267 | Epistemology | [The Primacy of Induction](../epistemology/the-primacy-of-induction/) | polish | 100 | 4 prompt sections are polish opportunities |
| 268 | Epistemology | [Vicious & Virtuous Circularity](../epistemology/vicious-virtuous-circularity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 269 | Epistemology | [What are Syllogisms?](../epistemology/what-are-syllogisms/) | polish | 100 | 4 prompt sections are polish opportunities |
| 270 | Epistemology | [What is Bayes Theorem?](../epistemology/what-is-bayes-theorem/) | polish | 100 | 4 prompt sections are polish opportunities |
| 271 | Epistemology | [What is Faith?](../epistemology/what-is-faith/) | polish | 100 | 4 prompt sections are polish opportunities |
| 272 | Ethics | [Assuming Objective Evil](../ethics/assuming-objective-evil/) | polish | 100 | 4 prompt sections are polish opportunities |
| 273 | Ethics | [Divine Command Theory](../ethics/divine-command-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 274 | Ethics | [Ethical Edge Case #1](../ethics/ethical-edge-case-1/) | polish | 100 | 4 prompt sections are polish opportunities |
| 275 | Ethics | [No Morality = Chaos?](../ethics/no-morality-chaos/) | polish | 100 | 4 prompt sections are polish opportunities |
| 276 | Ethics | [Trolley Problems](../ethics/trolley-problems/) | polish | 100 | 4 prompt sections are polish opportunities |
| 277 | Ethics | [Value & Morality in Diversity?](../ethics/value-morality-in-diversity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 278 | Humanistic Philosophies | [Are Humans More Egoistic or Altruistic?](../humanistic-philosophies/are-humans-more-egoistic-or-altruistic/) | polish | 100 | 4 prompt sections are polish opportunities |
| 279 | Humanistic Philosophies | [Existentialism: Key Concepts](../humanistic-philosophies/existentialism-key-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 280 | Humanistic Philosophies | [New Manifestations of Theism](../humanistic-philosophies/new-manifestations-of-theism/) | polish | 100 | 4 prompt sections are polish opportunities |
| 281 | Introduction | [Studying Philosophy: Resources](../introduction/studying-philosophy-resources/) | polish | 100 | 4 prompt sections are polish opportunities |
| 282 | Metaphysics | [A Taxonomy of Impossibilities](../metaphysics/a-taxonomy-of-impossibilities/) | polish | 100 | 4 prompt sections are polish opportunities |
| 283 | Metaphysics | [Are Quantum Physics “Spiritual”?](../metaphysics/are-quantum-physics-spiritual/) | polish | 100 | 4 prompt sections are polish opportunities |
| 284 | Metaphysics | [Could Mind be Fundamental?](../metaphysics/could-mind-be-fundamental/) | polish | 100 | 4 prompt sections are polish opportunities |
| 285 | Metaphysics | [Emergence](../metaphysics/emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 286 | Metaphysics | [Energy & Psychic Phenomena](../metaphysics/energy-psychic-phenomena/) | polish | 100 | 4 prompt sections are polish opportunities |
| 287 | Metaphysics | [Explanations](../metaphysics/explanations/) | polish | 100 | 4 prompt sections are polish opportunities |
| 288 | Metaphysics | [Matthew Pirkowski on Emergence](../metaphysics/matthew-pirkowski-on-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 289 | Metaphysics | [Metaphysics – Core Concepts](../metaphysics/metaphysics-core-concepts/) | polish | 100 | 4 prompt sections are polish opportunities |
| 290 | Metaphysics | [Ontological Domains](../metaphysics/ontological-domains/) | polish | 100 | 4 prompt sections are polish opportunities |
| 291 | Metaphysics | [Stuart Kauffman on Emergence](../metaphysics/stuart-kauffman-on-emergence/) | polish | 100 | 4 prompt sections are polish opportunities |
| 292 | Metaphysics | [The Principle of Sufficient Reason](../metaphysics/the-principle-of-sufficient-reason/) | polish | 100 | 4 prompt sections are polish opportunities |
| 293 | Miscellany | [Complexity Theory](../miscellany/complexity-theory/) | polish | 100 | 4 prompt sections are polish opportunities |
| 294 | Miscellany | [Cross-Culture Emotional Dispositions](../miscellany/cross-culture-emotional-dispositions/) | polish | 100 | 4 prompt sections are polish opportunities |
| 295 | Miscellany | [David Krakauer on Complexity](../miscellany/david-krakauer-on-complexity/) | polish | 100 | 4 prompt sections are polish opportunities |
| 296 | Miscellany | [Domains of Aesthetics](../miscellany/domains-of-aesthetics/) | polish | 100 | 4 prompt sections are polish opportunities |

## Upcoming Batch Preview

### Next +1: cycle 1, queue positions 297-346

- `polish` 100 [Miscellany / Flack & Mitchell on Complexity](../miscellany/flack-mitchell-on-complexity/)
- `polish` 100 [Miscellany / Information Theory](../miscellany/information-theory/)
- `polish` 100 [Miscellany / Sara Walker on Life’s Emergence](../miscellany/sara-walker-on-lifes-emergence/)
- `polish` 100 [Miscellany / The Fantastical & Historical Truth](../miscellany/the-fantastical-historical-truth/)
- `polish` 100 [Miscellany / Zak Stein on Complexity](../miscellany/zak-stein-on-complexity/)
- `polish` 100 [Philosophical Inquiry / Appreciating our Insignificance](../philosophical-inquiry/appreciating-our-insignificance/)
- `polish` 100 [Philosophical Inquiry / Charitable Engagement](../philosophical-inquiry/charitable-engagement/)
- `polish` 100 [Philosophical Inquiry / Dangers: Anti-Intellectualism](../philosophical-inquiry/dangers-anti-intellectualism/)
- `polish` 100 [Philosophical Inquiry / Dangers: Gaslighting](../philosophical-inquiry/dangers-gaslighting/)
- `polish` 100 [Philosophical Inquiry / Dangers: Limits on Doubt](../philosophical-inquiry/dangers-limits-on-doubt/)

### Next +2: cycle 1, queue positions 347-396

- `polish` 100 [Rational Thought / Empathy Overload](../rational-thought/empathy-overload/)
- `polish` 100 [Rational Thought / Factual Disagreements vs Semantic Misunderstandings](../rational-thought/factual-disagreements-vs-semantic-misunderstandings/)
- `polish` 100 [Rational Thought / Fine-Tuned Rationality](../rational-thought/fine-tuned-rationality/)
- `polish` 100 [Rational Thought / Monetary Goals](../rational-thought/monetary-goals/)
- `polish` 100 [Rational Thought / The Power of Statistics](../rational-thought/the-power-of-statistics/)
- `polish` 100 [Rational Thought / The Primacy of Emotions](../rational-thought/the-primacy-of-emotions/)
- `polish` 100 [Rational Thought / Tu Quoque or “You too!”](../rational-thought/tu-quoque-or-you-too/)
- `polish` 100 [Rational Thought / What is “Design Thinking”?](../rational-thought/what-is-design-thinking/)
- `polish` 100 [Rational Thought / Where Framing Goes Awry](../rational-thought/where-framing-goes-awry/)
- `polish` 100 [Economics / Behavioral Economics](../economics/behavioral-economics/)

## Summary

- Tracked pages: 528
- Pages remaining in current cycle: 282
- Estimated batches per cycle: 11

- gap-fill: 86
- polish: 419
- review: 23
