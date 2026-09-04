# Editorial audit — cycle 7, batch 100–149

Date: 2026-09-04

## Scope and preservation

Reviewed the 50 pages selected by `currentBatch.pages`, from Philosopher Club Membership through Moral Systems: Required Elements. Rebuilt from commit `d9cfa71b3`, not from the overlapping uncommitted generated output. Every page received a substantive clarification, correction, or worked example. There are 67 explicitly targeted section edits; all 200 prompt sections receive structural and preservation checks. This is an editorial audit, not an independent verification of every historical assertion in the archive.

The complete pre-existing changes are preserved in [the backup](/Users/philstilwell/Documents/byteseismic-audit-backup-20260904-XnZFhk/README.md): a binary-capable patch and an archive covering 641 changed files. The other 591 changed files remain byte-for-byte unchanged in the workspace.

## Main improvements

- Replaced thin philosopher-category instructions with five categories containing five examples each; supplied five-point comparison scales with explicit limitations.
- Distinguished confidence from action thresholds, causal confidence from causal contribution, and experience-shaped trust in logic from a premise-free proof of logic.
- Replaced inadequately supported personality-study summaries and misleading claims about shyness, choice, and exposure therapy. Added traceable research and National Institute of Mental Health guidance.
- Rebuilt the economics teaching sections with 30 definitions, 15 connected concepts, and ten explained mathematical relationships. Removed mismatched formula explanations and unsupported past-versus-present generalizations.
- Replaced speculative meta-ethics percentages with dated 2020 PhilPapers Survey figures and response conventions.
- Made the testability discussion about specified promises and fair comparison, without relying on unsupported blanket empirical claims.
- Added concrete examples for inquiry, agency, moral anti-realism, language, uncertainty, leadership, and ideological insulation. Preserved the curator's questions and recovered exchanges.
- Removed recurring empty editorial instructions and malformed learning-card text where encountered.

## Build safeguard

The isolated rebuild exposed an important cause of regression: the archive builder's manual-page injectors overwrite tailored context and learning notes even when the page itself is not regenerated. The 50 reviewed pages now carry a specific editorial-maintenance marker, and the builder skips those injectors for this batch. Unmarked pages retain existing behavior.

The renderer refuses to write when the authoritative tracker names a different batch. Its `--check` mode remains available after the tracker advances. It checks deterministic output, original questions, recovered exchanges, unchanged dialogue outside explicitly replaced composite responses, section counts, unique IDs, and local anchors. Article modification dates are synchronized in metadata and structured data.

## Verification

- Batch renderer: 50 pages and 200 prompt sections passed.
- Dialectical preservation: all 39 recovered pages and 17 high-risk regression cases passed.
- Visual inspection: philosopher categories, personality-study exposition, and economics formulas rendered legibly with functioning section navigation; temporary browser tab and local server closed.
- First isolated full build: 840 pages scanned, zero reported structural, link, grammar-scar, SEO, structured-data, sitemap, or robots issues. This build exposed the semantic overwrite behavior described above, which structural checks alone did not detect.
- Final safeguarded full build: completed successfully; its 840-page site audit again reported zero issues in every category. The renderer's `--check --built-root` regression check confirms that all 50 reviewed files survived the full build byte-for-byte.

## Follow-up

The philosophers-versus-philosophy prompt requests five documented histories of erroneous ideas delaying correction. The revised response explicitly distinguishes empirical error, moral repudiation, disputed metaphysics, appropriation, and institutional persistence; it does not pretend these establish five documented causal histories. A further primary-source historical expansion would be useful. Other inherited historical anecdotes have not all been independently revalidated in this editorial pass.

No unrelated generated changes belong in this commit. After final verification passed, the tracker advanced to cycle 7 index 150 (displayed position 151), beginning “What are Ethics?”. The reviewed batch and updated tracker are ready for commit.

## Pages reviewed and targeted improvements

- [Philosopher Club Membership](/Users/philstilwell/Documents/BYTESEISMIC/philosophers/philosopher-club-membership/index.html): Five overlapping ways of doing philosophy; Retrospective labels are useful, but imagined reactions remain speculative; Practical philosophy changes how a difficult decision is made.
- [Philosophers or Philosophy?](/Users/philstilwell/Documents/BYTESEISMIC/philosophers/philosophers-or-philosophy/index.html): Use thinkers as entry points and arguments as the test; Distinguish demonstrated errors from disputed philosophical inheritances.
- [Philosophical Gradients](/Users/philstilwell/Documents/BYTESEISMIC/philosophers/philosophical-gradients/index.html): Build separate axes before placing philosophers; Five-point teaching scales, with explicit limits.
- [Dangers: Untestable Ideologies](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/dangers-untestable-ideologies/index.html): Keep the promised outcome fixed when testing the claim.
- [Observable Regularities](/Users/philstilwell/Documents/BYTESEISMIC/philosophy-of-science/observable-regularity/index.html): Observed patterns support provisional expectations, not guarantees.
- [Abduction: Utility and Issues](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/abduction-utility-and-issues/index.html): Reserve room for unconsidered explanations without inventing precision.
- [Intrinsic Human Value](/Users/philstilwell/Documents/BYTESEISMIC/ethics/intrinsic-human-value/index.html): Sentience supplies a morally relevant fact only with an evaluative premise; Separate moral standing from criteria for a particular decision.
- [What is Etymology?](/Users/philstilwell/Documents/BYTESEISMIC/philosophy-of-language/what-is-etymology/index.html): Use word origins to investigate meaning, not dictate it.
- [Avoiding Single-Cause Dogmatism](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/avoiding-single-cause-dogmatism/index.html): Separate confidence in a cause from the size of its contribution.
- [Collapsing Epistemological Terms](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/collapsing-epistemological-terms/index.html): Unpack knowledge without losing truth or reliability.
- [⌁ Finite Agency, Moral Demand, and Happiness](/Users/philstilwell/Documents/BYTESEISMIC/ethics/finite-agency-moral-demand-and-happiness/index.html): Give finite care a practical stopping rule.
- [Perverse Incentives](/Users/philstilwell/Documents/BYTESEISMIC/rational-thought/perverse-incentives/index.html): Test the easiest way to satisfy the metric while defeating the goal.
- [Doxastic Voluntarism](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/doxastic-voluntarism/index.html): Direct choice of belief differs from control over inquiry.
- [The Burden of Proof](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/the-burden-of-proof/index.html): Some evidence is not yet enough support for the claim.
- [Can Humans Change?](/Users/philstilwell/Documents/BYTESEISMIC/humanistic-philosophies/can-humans-change/index.html): Change is possible without unlimited self-reinvention; What longitudinal evidence does—and does not—show; Choose a concrete behavior rather than reject your whole personality; Autonomy and professional support are not opposites; One person's success does not establish a brute-force method.
- [Do Humans have an Essence?](/Users/philstilwell/Documents/BYTESEISMIC/humanistic-philosophies/do-humans-have-an-essence/index.html): A fixed purpose is different from a stable disposition; Dispositions constrain choices without supplying a predetermined purpose; Shyness is not simply a choice or a verdict on your identity.
- [Epistemological Case Studies](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/epistemological-case-studies/index.html): A sixty-minute class that tests one reasoning habit at a time.
- [Moral Black Boxes](/Users/philstilwell/Documents/BYTESEISMIC/ethics/moral-black-boxes/index.html): The problem is one-way evaluation, not mystery alone.
- [Economics – Core Concepts](/Users/philstilwell/Documents/BYTESEISMIC/economics/economics-core-concepts/index.html): Read an equation as a set of assumptions before using it; Connect scarcity, incentives, and consequences; How economic questions connect households, firms, and institutions; Tools change, but model judgment remains essential; Thirty terms for understanding choices under constraints.
- [Complexity Theory](/Users/philstilwell/Documents/BYTESEISMIC/miscellany/complexity-theory/index.html): Complexity explains interaction, not permission to abandon testing.
- [Personal Truth?](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/personal-truth/index.html): Preserve first-person testimony without multiplying contradictory truths.
- [Regret Assessment](/Users/philstilwell/Documents/BYTESEISMIC/rational-thought/regret-assessment/index.html): Compare a regrettable action with a regrettable omission.
- [Belief/Evidence Graphic](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/belief-evidence-graphic/index.html): An action threshold need not be a sudden change in confidence; High stakes justify caution in action, not belief in the opposite; Calibration is the remedy, not the danger.
- [Pascal’s Wager](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/pascals-wager/index.html): Rival payoff claims prevent a unique decision without further premises.
- [The Inductive Paradox](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/the-inductive-paradox/index.html): Apply comparable standards, not mechanically identical conclusions.
- [Christian Apologetics](/Users/philstilwell/Documents/BYTESEISMIC/humanistic-philosophies/christian-apologetics/index.html): Separate apologetic methods before assessing their claims.
- [Common Sense Blunders](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/common-sense-blunders/index.html): Turn an obvious-seeming answer into a testable guess.
- [Packaged vs Eclectic Ideologies](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/packaged-vs-eclectic-ideologies/index.html): Check selected beliefs for incompatible commitments.
- [Selective Pressures on Ideologies](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/selective-pressures-on-ideologies/index.html): Transmission success and truth require different evidence.
- [The Danger of “Resulting”](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/the-danger-of-resulting/index.html): Resulting mistakes a fortunate outcome for a sound decision.
- [Is Logic Acquired Inductively?](/Users/philstilwell/Documents/BYTESEISMIC/philosophy-of-science/is-logic-acquired-inductively/index.html): Experience-shaped confidence is not a premise-free proof of logic.
- [Case #6 – Insatiable Loops](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/case-6-insatiable-loops/index.html): Ask what would distinguish a discovered cave from an excavated one.
- [Fictional Meta-Ethics Debate](/Users/philstilwell/Documents/BYTESEISMIC/ethics/fictional-meta-ethics-debate/index.html): Locate the extra premise behind a claim of binding authority.
- [Decision-Making](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/decision-making/index.html): Stop investigating when the next check is unlikely to change the choice.
- [Dangers: Strong Leaders](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/dangers-strong-leaders/index.html): Judge how a leader responds to correction.
- [Dangers: Co-opted Wonders](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/dangers-co-opted-wonders/index.html): Grant the wonder, then ask for the missing inference.
- [Dangers: Half-Searches](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/dangers-half-searches/index.html): Plan for an unwelcome answer before looking for reassurance.
- [Ethics — Core Concepts](/Users/philstilwell/Documents/BYTESEISMIC/ethics/ethics-core-concepts/index.html): Separate the moral verdict from the theory of its status.
- [Gradient Concepts and Binary Terms](/Users/philstilwell/Documents/BYTESEISMIC/philosophy-of-language/gradient-concepts-and-binary-terms/index.html): A useful cutoff need not be a natural boundary.
- [Epistemology — Core Concepts](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/epistemology-core-concepts/index.html): Follow one report through evidence, confidence, and revision.
- [Do I need a “worldview”?](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/do-i-need-a-worldview/index.html): Make a revisable method explicit without pretending it is assumption-free.
- [Philosophy of Language — Core Concepts](/Users/philstilwell/Documents/BYTESEISMIC/philosophy-of-language/core-concepts-philosophy-of-language/index.html): Use one utterance to distinguish meaning, context, and implication.
- [Training Data Bias](/Users/philstilwell/Documents/BYTESEISMIC/rational-thought/training-data-bias/index.html): Test a model's revised answer rather than reward its agreement.
- [Coherent Moral Systems](/Users/philstilwell/Documents/BYTESEISMIC/ethics/coherent-moral-systems/index.html): Consistency needs a rule for conflicts, not just admirable principles.
- [Counterfactual Reasoning](/Users/philstilwell/Documents/BYTESEISMIC/epistemology/counterfactual-reasoning/index.html): Change one cause while allowing its consequences to change.
- [Dangers: Narrative](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/dangers-narrative/index.html): Retell the same events without the story's assigned heroes.
- [Dangers: Ontological Buffet](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/dangers-ontological-buffet/index.html): An added entity needs more than the ability to rescue a story.
- [Dangers: Unnuanced Conclusions](/Users/philstilwell/Documents/BYTESEISMIC/philosophical-inquiry/dangers-unnuanced-conclusions/index.html): Ask what would justify a stronger or weaker conclusion.
- [Meta-Ethics](/Users/philstilwell/Documents/BYTESEISMIC/ethics/meta-ethics/index.html): A survey maps respondents, not the truth of a moral theory.
- [Moral Systems: Required Elements](/Users/philstilwell/Documents/BYTESEISMIC/ethics/moral-systems-required-elements/index.html): Use a hard case to locate a system's missing rule.
