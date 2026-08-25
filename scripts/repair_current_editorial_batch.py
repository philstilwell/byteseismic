#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag


ROOT = Path(__file__).resolve().parents[1]
TRACKER_PATH = ROOT / "quality" / "editorial-audit-tracker.json"

PLACEHOLDER_PATTERNS = [
    re.compile(r"is best approached as a live problem with pressure points", re.I),
    re.compile(r"The section is doing its job when the reader can", re.I),
    re.compile(r"The easiest way to test the concept is to run it through", re.I),
    re.compile(r"The central question is whether .* can bear the conclusion being attached to it", re.I),
    re.compile(r"The charitable version should be stated before the criticism lands", re.I),
    re.compile(r"A good reader should finish the section able to say", re.I),
    re.compile(r"becomes more intelligible when it is forced into a concrete case", re.I),
    re.compile(r"^A strong example does more than decorate .+\.$", re.I),
]

PLACEHOLDER_LIST_PATTERNS = [
    re.compile(r"This matters only if it changes how meaning, use, ambiguity, or reference is being handled\.", re.I),
    re.compile(r"The epistemic pressure is how evidence, uncertainty, and responsible confidence interact", re.I),
]

GENERIC_HEADING_PATTERNS = [
    re.compile(r"\breally means in practice\b", re.I),
    re.compile(r"\bclarifies, and where its limits show\b", re.I),
    re.compile(r"\bmatters in practice\b", re.I),
    re.compile(r"^Putting .+ under pressure\.?$", re.I),
    re.compile(r"require sharper edges before the distinction can guide judgment\.?$", re.I),
    re.compile(r"^A concrete case shows what .+ explains and where it strains\.?$", re.I),
    re.compile(r"^The real issue is what .+ changes once it becomes precise\.?$", re.I),
    re.compile(r"^The map of .+ becomes useful once the parts stop doing different work\.?$", re.I),
    re.compile(r"^.+ matters only if it survives the strongest pressure against it\.?$", re.I),
    re.compile(r"^Key terms in .+ become useful only when .+\.?$", re.I),
    re.compile(r"^The strongest version of the page says .+\.?$", re.I),
]

GENERATED_GENERIC_PATTERNS = [
    re.compile(r"^The answer should clarify the central claim, show what gives it force, and identify the comparison, objection, or example that keeps the discussion honest\.$", re.I),
    re.compile(r"^This section works best when .+ is treated as a concrete intellectual problem rather than as a settled label\.$", re.I),
    re.compile(r"^A useful test case is an everyday disagreement where both sides have some evidence but not enough to claim certainty\.", re.I),
    re.compile(r"^That requires clarifying the main claim, the tension or evidence that makes the claim worth discussing, and the point where an easy reading would start to overstate what follows\.$", re.I),
    re.compile(r"^The real work in this section is to make .+ intelligible without pretending the answer is simpler than it is\.$", re.I),
    re.compile(r"^The section is doing its job when the reader can .+$", re.I),
    re.compile(r"^The example earns its place only if it sharpens judgment\..+$", re.I),
]

SCAFFOLD_PARAGRAPH_PATTERNS = [
    re.compile(r"^The live issue is .+? This is where .+? starts to guide judgment instead of merely sounding important\.$", re.I),
    re.compile(r"^This middle step .+$", re.I),
    re.compile(r"^The dialogue form earns its place only if .+$", re.I),
    re.compile(r"^The answer should discipline the question without pretending .+$", re.I),
    re.compile(r"^Do not let the example sit there like a decorative vase\..+$", re.I),
    re.compile(r"^By this point the clearing work should already be done\..+$", re.I),
    re.compile(r"^The earlier sections should already have put .+$", re.I),
    re.compile(r"^The first move should give the reader something firm to hold\..+$", re.I),
    re.compile(r"^A fair pushback is .+$", re.I),
    re.compile(r"^A fair question is why this map is needed at all\..+$", re.I),
    re.compile(
        r"^A fair pushback is that real decisions often happen quickly\. The point is not to abolish speed; it is to notice which shortcut is harmless and which one quietly rigs the outcome before the reasoning even starts\.$",
        re.I,
    ),
    re.compile(
        r"^A fair pushback is that decent people often know what they mean morally long before they can theorize it neatly\. True enough\. The page still has to show what that first moral reaction gets right, what it blurs, and why the distinction matters once disagreement becomes serious\.$",
        re.I,
    ),
]

SCAFFOLD_LIST_PATTERNS = [
    re.compile(r"^State the clearest version of .+ before testing it\.$", re.I),
    re.compile(r"^Ask what evidence, example, or argument would genuinely change the reader's judgment\.$", re.I),
    re.compile(r"^Notice where a familiar phrase is doing more work than the reasoning beneath it\.$", re.I),
    re.compile(r"^Keep the neighboring concepts visible so the page does not collapse different questions together\.$", re.I),
    re.compile(r"^The exchange works only if its movement through .+$", re.I),
]

CUSTOM_SECTION_HEADINGS = {
    (
        "Regret Assessment",
        "What can I do to ensure I make decisions that minimize regrets later in life?",
    ): "Regret shrinks when present choices are screened for their future cost",
    (
        "Belief/Evidence Graphic",
        "Can individual A rationally say at the end of the period, ‘I knew it all along’ if they maintained their high degree of belief without mapping it to the relevant evidence as it fluctuated?",
    ): "A stable high belief can still be epistemically irresponsible",
    (
        "Christian Apologetics",
        "Imagine someone says, “The sparse evidence for your God requires that I assign a very low credence to your God’s existence.” How might each category of apologist respond?",
    ): "Sparse evidence forces each apologetic style to reveal its standard of justification",
    (
        "Christian Apologetics",
        "How might any of these apologetic approaches deal with the absurdity of an omnipresent and omnipotent God wanting a relationship with humans, but requiring that those humans read a holy book to come to know him?",
    ): "The relationship problem exposes the limits of revelation-by-text alone",
    (
        "Christian Apologetics",
        "For each apologetic category, provide a hypothetical dialogue between an apologist and a philosopher, with the philosopher revealing the weaknesses in the apologetics approach.",
    ): "A dialogue that exposes where apologetic styles fail under pressure",
    (
        "Selective Pressures on Ideologies",
        "Discuss historical 5 cases of demonstrably flawed ideologies, and the dynamics leading to their popularity.",
    ): "Flawed ideologies rise when social needs outrun truth-tracking",
    (
        "Selective Pressures on Ideologies",
        "In ChatGPT’s response, there appears to be a conflation between an ideology that is ethical and one that is true. Is there an actual necessary tie between what is ethical (by some ethical standard) and what is true?",
    ): "Ethical appeal and factual truth are not the same kind of claim",
    (
        "Fictional Meta-Ethics Debate",
        "I am still dissatisfied with what seems to be a reification of moral intuitions into something weightier than mere emotions. Can we not simply dispense with the muddy term moral and use the terms emotions or values when discussing human behavior? Continue the dialogue accordingly.",
    ): "Whether moral intuitions are more than emotions in disguise",
    (
        "Fictional Meta-Ethics Debate",
        "It is precisely the notion of normative force that I am objecting to. The use of the term normative appears to be simply another attempt to sneak in the assumption of an actual moral realm, and ignores the position of the moral anti-realist that there is no actual moral or normative realm in which moral or normative facts can reside. Continue the dialogue accordingly.",
    ): "Anti-realism presses hardest on the idea of normative force",
    (
        "Core Concepts: Philosophy of Language",
        "Provide a timeline of the philosophy of language. Include deeper explanations for any paradigm shifts.",
    ): "A timeline of philosophy of language through its major turns",
    (
        "Training Data Bias",
        "Based on the following post, explain the manner in which logical pushback can refine biased training data .",
    ): "Logical pushback can expose and refine biased training data",
    (
        "Training Data Bias",
        "Produce an essay on effective pushback against AI responses with apparent training data bias.",
    ): "How to push back effectively against biased AI responses",
    (
        "Moral Systems: Required Elements",
        "The following are proposed ways to refute the coherence of a moral system. Elaborate on each and provide any evaluative criteria of your own.",
    ): "How to test whether a moral system is internally coherent",
    (
        "Preponderance of Evidence?",
        "How might you respond to such a statement to demonstrate that belief is not binary and that there is no special threshold along the epistemic gradient that demands a binary flipping of our epistemic commitment from disbelief to belief?",
    ): "Belief should track gradients of evidence, not cross a magic threshold",
    (
        "Preponderance of Evidence?",
        "Create a dialogue featuring a gradient belief proponent and a binary belief proponent.",
    ): "A dialogue between gradient belief and binary belief",
    (
        "Preponderance of Evidence?",
        "Some of the terms in the section above appear appropriate when the degree of belief is fairly high. Provide guidelines to when more nuanced terms might be necessary to encourage the mapping of our degree of certainty to the degree of the evidence.",
    ): "When high-confidence language becomes more justified than cautious language",
    (
        "What is Language?",
        "Provide 10 philosophical insights on human language capabilities.",
    ): "Ten philosophical insights about what human language lets us do",
    (
        "Collapsing 2nd-Order Epistemological Concepts into 1st-Order Terms",
        "Suggest which 2nd-order concepts/terms in epistemology can be parsimoniously collapsed into phrases that are anchored by a 1st-order epistemological concepts/terms. Explain the collapse and provide your rationale.",
    ): "Which second-order epistemic terms can be reduced without loss",
    (
        "Conspiracies: Misunderstanding Human Nature",
        "To what degree does belief in supernatural entities, original sin, and the like, contribute to such cognitive distortions?",
    ): "Supernatural worldviews can train habits that conspiracies later exploit",
    (
        "Conspiracies: Misunderstanding Human Nature",
        "Provide the syllogistic formulations reflecting the correlation between increased mythical thinking and increased conspiratorial thinking.",
    ): "Syllogisms that expose the link between mythical and conspiratorial thinking",
    (
        "Functionalism & Subjectivity",
        "Provide further elaboration on the notion that, despite subjectivity feeling non-material to a subjective mind, the connectivity of the material substrate subsumes this subjective experiencing of qualia.",
    ): "Why subjective qualia can still depend on material organization",
    (
        "Subjective/Objective Free Will",
        "Can someone committed to the absence of objective free will also claim there is subjective free will?",
    ): "Subjective agency can survive even if objective free will does not",
    (
        "Subjective/Objective Free Will",
        "So, the determinist need not give up terms that reflect personal agency such as “choose” and “decide” if they are willing to make clear in relevant contexts that they are referring to subjective free will, right?",
    ): "Determinists can keep agency language if they state its level clearly",
    (
        "Subjective/Objective Free Will",
        "Given this conclusion, is there any field other than metaphysics in which a strong determinist stance from a determinist would be productive or required?",
    ): "Where strong determinism helps outside metaphysics",
    (
        "Wealth Creation",
        "Produce an entertaining, educational narrative to explain the dynamics of wealth creation.",
    ): "A narrative that makes wealth creation concrete",
    (
        "Accounting for X",
        "Christian apologists often claim that non-Christians cannot “account for” the existence of logic or the laws of nature. What do they mean by this, and how does Christianity provide the proper “accounting”?",
    ): "What apologists mean when they say only Christianity can 'account for' logic",
    (
        "Accounting for X",
        "Provide a list of candidate denotations of the term “account for” and indicate which are and are not coherent and of semantical substance.",
    ): "Which meanings of 'account for' are coherent and which are not",
    (
        "The Dangers of the Carrot & Stick",
        "How can the rational mind inoculate themselves against these unsubstantiated promises and threats?",
    ): "How a rational mind resists unsubstantiated promises and threats",
    (
        "Testing Ideologies",
        "Many religions suggest there are promises that their religion makes to its followers but then claim it is wrong for us to statistically test those claims. Does this warrant the suspicion that the claimed promises are not actually fulfilled? How might we encourage a rigorous test of those promises?",
    ): "If promises resist testing, suspicion becomes reasonable",
    (
        "The Dangers of Ideologies of Mystery",
        "How might I respond to someone who encourages me to believe something based on the beauty of its mystery instead of the evidence or argumentation supporting it?",
    ): "Mystery is not evidence, even when it feels profound",
    (
        "Economic Comparisons",
        "Provide me with a list of the average global incomes for each decade since 1850.",
    ): "What long-run global income comparisons can and cannot show",
    (
        "Economic Comparisons",
        "Have the average number of hours of labor necessary to buy common necessities increased or decreased over the years?",
    ): "How labor time for necessities has changed over time",
    (
        "Economic Stability",
        "Some economists suggest that high economic predictability is necessary for investment and entrepreneurship. Please elaborate on this notion, especially in respect to the conditions you provided above.",
    ): "Why investment and entrepreneurship depend on predictable conditions",
    (
        "Economic Stability",
        "Elaborate on the advantages unpredictability offers entrepreneurship and arbitrage.",
    ): "Where unpredictability creates openings for entrepreneurship and arbitrage",
    (
        "Economic Stability",
        "Discuss other sources of unpredictability such as corruption that factor into economic dynamics.",
    ): "Corruption and other hidden sources of instability",
    (
        "Minimum Wage",
        "Some might argue that increasing the minimum wage eats into the rights of workers to take any job that they’d like. Some jobs that might pay below the minimum wage may provide rewarding experiences to those willing to work for lower wages. Please weigh in on this argument.",
    ): "The freedom-to-contract argument for sub-minimum wages has real appeal and real limits",
    (
        "Minimum Wage",
        "The curator’s pushback: Gemini did address the argument as stated, and appears to focus on a minimum threshold of wages the government apparently should set beneath which no one should feel the work is rewarding enough to compensate for the lower wages. Is there an assumption here that a minimum wage is necessary?",
    ): "Whether minimum-wage arguments smuggle in a necessity assumption",
    (
        "Minimum Wage",
        "Isn’t the efficient use of migrant workers paid under-the-table at sub-minimum wage levels evidence that the minimum wage is over-regulation?",
    ): "Informal migrant labor does not by itself prove minimum wage is over-regulation",
    (
        "Minimum Wage",
        "Can you actually call a verbal contract in which both the employee and the employer agree and follow through on their commitments “exploitation”? Once you stop this “grey” economic practice, you only end up with the poor would-be migrants becoming poorer in their impoverished native countries, right?",
    ): "Consent alone does not settle whether grey-market labor is exploitative",
    (
        "Coherent Moral Systems",
        "Elaborate on the logical consistency required of such a moral system. Give real or imaginary examples if possible.",
    ): "Why coherent moral systems need logical consistency",
    (
        "Moral Hazards",
        "Provide an example of a moral hazard that is based only on information asymetry.",
    ): "A moral hazard driven only by information asymmetry",
}


def load_batch_paths() -> list[Path]:
    tracker = json.loads(TRACKER_PATH.read_text())
    return [ROOT / page["pagePath"].strip("/") / "index.html" for page in tracker["currentBatch"]["pages"]]


def strip_prompt_number(text: str) -> str:
    text = " ".join(text.split())
    return re.sub(r"^Prompt\s+\d+:\s*", "", text, flags=re.I)


def section_prompt(section: Tag) -> str:
    prompt_node = section.find("p", class_="article-section__prompt", recursive=False)
    prompt = strip_prompt_number(prompt_node.get_text(" ", strip=True) if prompt_node else "")
    return re.sub(r"\s+([,.;:?])", r"\1", prompt)


def normalize_heading(text: str, page_title: str, prompt: str) -> str:
    text = " ".join(text.split())
    custom = CUSTOM_SECTION_HEADINGS.get((page_title, prompt))
    if custom:
        return custom
    if heading_needs_rewrite(text, prompt):
        return derive_heading_from_prompt(prompt, page_title)
    return text


def heading_needs_rewrite(text: str, prompt: str) -> bool:
    if any(pattern.search(text) for pattern in GENERIC_HEADING_PATTERNS):
        return True
    if text and text[0].islower():
        return True
    if text.startswith(("And ", "Me ", "Up ")):
        return True
    cleaned_prompt = " ".join(prompt.split()).strip().rstrip(".")
    if cleaned_prompt:
        prompt_base = cleaned_prompt.rstrip("?")
        heading_base = text.strip().rstrip("?")
        if heading_base == prompt_base and len(text) > 72:
            return True
        if prompt_base.startswith(heading_base) and len(prompt_base) - len(heading_base) >= 6:
            return True
        prompt_words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", prompt_base.lower())
        heading_words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", heading_base.lower())
        if len(heading_words) >= 4:
            for start in (1, 2, 3):
                candidate = prompt_words[start : start + len(heading_words)]
                if heading_words == candidate:
                    return True
    return False


def trim_heading_length(text: str, limit: int = 96) -> str:
    if len(text) <= limit:
        return text
    clipped = text[:limit].rsplit(" ", 1)[0].strip()
    return clipped.rstrip(" ,;:") or text[:limit].strip()


def sentence_case(text: str) -> str:
    if not text:
        return text
    return text[0].upper() + text[1:]


def derive_heading_from_prompt(prompt: str, page_title: str) -> str:
    cleaned = " ".join(prompt.split()).strip().rstrip(".")
    if not cleaned:
        return page_title

    prompt_lower = cleaned.lower()
    exact_overrides = {
        "would an insufficient food supply justify the killing of the shipwrecked 100 by the 300 natives under any political or ethical theory?": "When scarcity is invoked to justify killing",
        "make the insufficient food supply an objective fact. is there any ethical culpability incurred by anyone who would not cull the population through killing, leading to the agonizing starvation of everyone?": "If everyone starves otherwise, what becomes culpable?",
        "provide your own assessment of the plausibility of these arguments, then assess their potential weaknesses": "An assessment of the view's plausibility and weaknesses",
        "write an essay on this scenario from the perspective of a compassionate moral non-realist": "A compassionate moral non-realist on survival and shared loss",
        "do we have examples of cohesive societies in which there is no single moral system but in which there is a deeply cultivated respect and compassion for humanity?": "Pluralistic societies can sustain compassion without one moral system",
        "japan is one country in which there is no strong religious foundation, but there is a strong notion of respect and community. comment on the social cohesion found in japan.": "Japan as a case of social cohesion without strong religious foundations",
        "can it be coherently argued that the person treating others well in the absence of a moral system has a character superior to the moralist even by the moralist’s own standard?": "Can kindness without a moral system outrank moralism itself?",
        "does the complexity of the trolley problem strongly suggest there is no objective moral standard readily accessible to humans and that “ moral intuitions ” are actually emotional dispositions?": "Do trolley problems expose moral intuition as emotional disposition?",
        "can ai agents now or in the future contribute to meaningful insights into trolley problem “ solutions “? why or why not?": "Can AI clarify trolley-problem decisions?",
        "can you produce an example of a computational ethics calculus related to the trolley problem?": "A computational ethics calculus for the trolley problem",
        "discuss the following scenario based on major political and ethical theories.": "How major moral and political theories sort the same survival crisis",
        "how would one argue that maintaining a diversity of competing species is morally right while maintaining only a few thriving species would be morally wrong? present the arguments in syllogistic form.": "The case for preserving biodiversity as a moral good",
        "how might one argue that maintaining a diversity of competing species is immoral while maintaining only a few thriving species would be morally right? present the arguments in syllogistic form.": "The case against treating biodiversity as a moral good",
        "is there an argument to be made that what humans deem moral arguments distill to merely emotional preferences once scrutinized?": "Do moral arguments collapse into emotional preference?",
        "what are the best online sources of philosophical training for those new to philosophy?": "The best online starting points for learning philosophy",
        "provide a 6-month schedule for well-rounded self-study training in philosophy": "A 6-month plan for well-rounded self-study in philosophy",
        "why might some people become bored or frustrated with philosophy, and how might i keep my philosophy studies exciting?": "How to keep philosophy engaging when boredom sets in",
        "describe the emotional disposition that is most healthy and productive when discussing philosophy with others": "The best emotional stance for discussing philosophy with others",
        "i am asking specifically about the shape of the statistical curve of human egoism/altruism as determined by common markers such as crime rates and charity giving.": "What the data might show about egoism and altruism",
        "what would be an optimal way to assess whether humans fall into polarized categories of “good” and “bad” or whether they generally tend to possess a balance of both egoism and altruism? what metrics and proxies might we use?": "How to measure whether people cluster as good, bad, or mixed",
        "would the many anecdotes (and presumably statistics) of people making dramatic changes to their lives from bad to good and vice-versa speak to this in any way?": "Do dramatic moral reversals weaken fixed human-type theories?",
        "for each of the 16 concepts above, create 3 scenarios depicting the concept in action.": "Existentialist concepts shown in lived scenarios",
        "many of the concepts above appear diametrically opposed to the many more hopeful (if unsubstantiated) promises found in religion. comment on why existentialism remains popular nonetheless.": "Why existentialism still attracts readers despite its harder outlook",
        "write an essay on the relevance of existentialism in today’s technology-laden world.": "The relevance of existentialism in a technology-laden world",
        "what effects has the decrease in participation in regular religious meetings had on notions of god and spirituality?": "How declining religious attendance reshapes ideas of God",
        "create a hypothetical debate between two experts on emergence who have contrasting opinions on the concept": "A debate between rival views of emergence",
        "provide a list of the most respected names in the field of emergence.": "Major figures in emergence research",
        "what are causes for the proliferation of the unsubstantiated notion that there is a psychic energy humans can access?": "Why the idea of psychic energy keeps spreading",
        "it appears that the principle of sufficient reason is intrinsically susceptible to irreconcilable subjective assessments on what reasons are sufficient. or can an objective foundation be found?": "Can the Principle of Sufficient Reason escape subjective standards?",
        "discuss the ontological implications of positing a realm in which psychic energy operates": "The ontological cost of positing a realm of psychic energy",
        "what relationships exist among the different notions of impossibility?": "How the different kinds of impossibility relate to one another",
        "how can different notions of impossibility become entangled and lead to confusion? give examples.": "How different kinds of impossibility get tangled together",
        "what is emergence?": "What emergence claims and why people argue about it",
        "list key domains in metaphysics and their defining questions.": "Key domains in metaphysics and the questions that define them",
        "a timeline of the development of metaphysics. include both the relevant thinkers and the concepts introduced.": "A timeline of metaphysics through its major thinkers and concepts",
        "create a hypothetical debate between two expert on emergence who have contrasting opinions on the concept": "A debate between rival views of emergence",
        "do a deep dive into the primary arguments made in the transcript, augmented by other relevant sources. create syllogisms of the arguments if possible, clearly restate any analogies, and make any causal chains explicit": "The transcript's main arguments, clarified and tested",
        "do a deep dive into the primary arguments made in the transcript, augmented by other relevant sources. create syllogisms of the arguments if possible, restate clearly any analogies, and make any causal chains explicit": "The transcript's main arguments, clarified and tested",
        "introduce 2 instances in which this principle is invoked, and discuss the strengths and weaknesses of the arguments.": "Two uses of the Principle of Sufficient Reason under scrutiny",
        "provide a list of key research questions relevant to resolving issues surrounding the principle of sufficient reason.": "Key research questions about the Principle of Sufficient Reason",
        "provide a list of promising research projects in information theory.": "Promising directions in information theory research",
        "provide the rigorous rationale behind giving the resurrection of jesus a “low to moderate” credence, but the flying dutchman a “very low” credence": "Why some fantastical historical claims outrank others in credibility",
        "list and elaborate on the hypothetical missing elements that would make the flying dutchman as plausible as the resurrection of jesus.": "What would make the Flying Dutchman as plausible as the resurrection?",
        "are there studies that suggest the control or suppression of emotions in early childhood results in 1) less access to intense emotions or 2) more control over intense emotions in adulthood?": "What childhood emotion-suppression studies actually suggest",
        "there seems to be some disagreement among the ai contributors on the last question. try to resolve the apparent disputes.": "How to sort out the dispute over emotional suppression",
        "how do japanese parents help their children regulate their emotions in a way that become beneficial in adulthood?": "How Japanese parenting trains emotional regulation",
        "introduce some key concepts relevant to the core concerns of complexity theory.": "Core concepts that anchor complexity theory",
        "what are the main domains of aesthetics?": "The main domains of aesthetics",
        "let’s focus on how information theory is used in exploring social networks. write a short, informative essay on this.": "How information theory helps explain social networks",
        "what are the benefits of charitable engagement with antagonistic individuals?": "Why charitable engagement helps with antagonistic people",
        "many ideologies recruit through promises of cosmic significance. how can we stay grounded and content in the reality of our relative unimportance?": "How to stay grounded without fantasies of cosmic importance",
        "while schooling is no guarantee one will find truth, there is a clear correlation between gaining knowledge and proximity to truth. please comment on this.": "Why schooling and truth-tracking correlate without guaranteeing truth",
        "if one does not have access to a formal education, what foundation and balance of self-education will most likely lead to truth acquisition?": "What self-education best substitutes for formal schooling",
        "is doubt intrinsically unstable and temporary, or is it instead a normal epistemic disposition taken in response to the current degree of the relevant evidence?": "Doubt as a normal response to incomplete evidence",
        "how might the inner monologue of humans and ais be intrinsically and irreconcilably different, and why might this be a good thing or bad thing for the advancement of ai?": "How human and AI inner monologues may differ in kind",
        "chatgpt suggests that humans “should” be in the driver’s seat when moral assessments are required. however, given the moral disagreements among humans, wouldn’t an impassive mind be better suited for the application of moral calculus?": "Should humans stay in charge of moral judgment?",
        "to what degree are your instructions to provide comprehensive and balanced responses explicitly coded, and to what degree are more implicit, higher-abstraction filters used?": "How much of AI balance is explicit instruction versus higher-level filtering?",
        "what are your general limits when discussing topics such as the tiananmen square protests or the armenian genocide?": "How AI limits appear in politically and historically sensitive topics",
        "is there a legitimate analogy that could be made between the poorly understood mathematical dynamics that have led to unexpected power in artificial intelligence and similar mathematical dynamics that may undergird the efficiency of the human brain?": "Can AI double descent illuminate the efficiency of the brain?",
        "to what degree do contradictory meanings contribute to the disuse of a word such as we see with the word sanction?": "How contradictory meanings can push a word toward disuse",
        "when a generational divide develops within a culture, is there a noticeable introduction of replacement terms by the younger generation?": "How generational turnover replaces aging words",
        "which areas of the brain are causally responsible for the various aspects of language acquisition, comprehension, and production?": "Which brain systems support language acquisition, comprehension, and speech",
        "to what degree is scaffolding central to all forms of human learning? give examples.": "How central scaffolding is to human learning",
        "how can scientists and educators encourage a reduction in the linguistic complexity behind simple realities?": "How to reduce needless complexity in scientific language",
        "list the advantages of a charitable disposition when engaging antagonistic individuals.": "How charity strengthens difficult relationships",
        "what are the best evidences for this correlation between education level and proximity to truth?": "Why education and truth-tracking still correlate imperfectly",
        "what are the best evidences for the correlation between education and proximity to truth?": "What best supports the education and truth-tracking link",
        "respond to gemini’s response shown below, addressing the issues raise": "A direct reply to the strongest egoist pushback",
        "create an essay on the risks of banning ai feedback that includes the works of these philosophers": "The risks of banning AI engagement with named philosophers",
        "assess the content on language and thought for factual accuracy, logical coherence, and testability.": "How strong is the case that language and thought are deeply linked?",
        "list and describe new areas of interest in the philosophy of mind.": "New areas of interest in philosophy of mind",
        "list and provide explanations of key concepts in the philosophy of mind.": "Key concepts in philosophy of mind, clearly explained",
        "a timeline of the philosophy of mind. include both the relevant thinkers and the concepts introduced.": "A timeline of philosophy of mind through its major thinkers and concepts",
        "what are ways to identify hidden confounding factors that may jeopardize a study?": "How to identify hidden confounding factors",
        "what are confounding variables in the context of a scientific experiment? (the terms “confounding variables” and “confounding factors” are essentially synonymous.)": "What confounding variables are and why they distort experiments",
        "elaborate on the way these categories build up from hard sciences to soft sciences.": "How the sciences scale from hard to soft",
        "comment on the degrees of freedom in each category that changes the degree of complexity and move away from quantitative certainty to more statistical modeling.": "Degrees of freedom and why softer sciences rely more on statistics",
        "introduce 12 essential terms scientists employ related to the notions of multi-variable, degrees of freedom, and boundedness. provide clear definitions and examples.": "Twelve core terms for multivariable science, degrees of freedom, and boundedness",
        "elaborate on the history of the reproducibility crisis, and provide an extensive explanation of its causes and effects.": "The reproducibility crisis: history, causes, and effects",
        "why is anti-intellectualism dangerous?": "Why anti-intellectualism damages truth-seeking cultures",
        "what risks arise when people treat doubt as a defect rather than a normal response to evidence?": "What goes wrong when doubt is treated as a flaw",
        "what are the main risks of removing impossible explanations too early?": "Why removing the impossible too early can mislead inquiry",
        "comment on the degrees of freedom in each category that changes the degree of complexity and move away from quantitative certainty to more statistical modeling.": "Why more degrees of freedom push science toward statistics",
        "elaborate on the history of the reproducibility crisis, and provide an extensive explanation of its causes and effects.": "The reproducibility crisis: how it grew and why it matters",
        "elaborate on the history of poor access to scientific research, and provide an extensive explanation of its causes and effects.": "Poor access to research: history, causes, and effects",
        "explain how the ability of an agent to interact with a perceived object would strengthen the ontological status of the object in the agent’s mind beyond what mere observation would.": "Why interaction can strengthen an object's felt reality",
        "explain how the ability of an agent to interact with a perceived object would strengthen the ontological status of the object in the agent’s mind beyond what mere observation would.": "Why interaction makes an object feel more real than observation alone",
        "provide two pedagogical narratives. the first will explain how an actual experiment would overturn the false intuition that heavier objects fall faster than light objects. the second will explain how a deductive analysis would overturn the false intuition.": "Two narratives that overturn a false intuition",
        "provide an example of an experimental design in which orthogonality (causal independence) can be robustly established.": "A clean experimental case of orthogonality",
        "present 3 actual scientific experiments in which two variables were considered orthogonal, but later shown to be causally dependent.": "When orthogonality later turned out to be false",
        "explain how “confidence intervals” work.": "How confidence intervals work",
        "list and define 30 key terms in the philosophy of science.": "Thirty key terms in philosophy of science",
        "list and provide explanations of key concepts in the philosophy of science.": "Core concepts in philosophy of science, explained",
        "provide a timeline of the philosophy of science. include deeper explanations for any paradigm shifts.": "A timeline of philosophy of science and its main turns",
        "list and describe new areas of interest in the philosophy of science.": "New areas of interest in philosophy of science",
        "provide historical cases in which laws that were once thought to be constant turned out to be wrong or riddled with exceptions.": "When supposed laws failed under closer scrutiny",
        "provide me with 3 examples outside of biology in which line of evidence converge to support a theory.": "Three non-biological cases of evidential convergence",
        "provide the mathematics behind the notion that converging independent lines of evidence strengthen a theory.": "Why independent evidence compounds mathematically",
        "provide 5 actual cases in which a proxy was revealed to be improper.": "Five cases where a proxy misled inquiry",
        "provide me with 5 examples of counter-intuitive or surprising legitimate proxies.": "Five surprising proxies that genuinely work",
        "comment on the intrinsic dangers contained in a position based on subjective perceptions rather than objective statistics.": "What goes wrong when subjective perception outruns public evidence",
        "provide three accounts from history in which the fudging of truth by policy-makers may have prevented a tragedy.": "Cases where strategic distortion may have prevented harm",
        "provide robust guidelines that would wisely direct policy-makers in similar situations.": "Guidelines for officials tempted to bend the truth",
        "provide an analogy on an interpersonal level that might make this dilemma more salient.": "An everyday analogy for truth versus panic management",
        "consider the following list of metrics of well-being. survey the list of societies that are failing on those metrics, and explain the institutional or cultural sources of those failures.": "Where societies fail the well-being metrics and why",
        "so, the degree of the legitimacy of tacit consent is based on the degree of freedom to emigrate, right?": "How far freedom to emigrate strengthens tacit consent",
        "if the notion of the social contract is to have any real ethical obligation, it will need to be able to coherently distinguish which systems they are ethically obligated to in the following scenarios, right?": "Hard cases for social-contract obligation",
        "could this argument be revised in any way to reach the valid conclusion “miraculous event x happened”?": "Can the miracle argument be repaired at all?",
        "in your revised argument, you introduce inductively acquired evidence. therefore, the conclusion cannot be certain but merely assigned a sub-absolute degree of confidence, right?": "Why any serious miracle argument ends in probability, not certainty",
        "are there times in which a less accommodating and a more stern public rebuttal would be more productive in terms of the number of minds changed?": "When a sterner rebuttal can be more effective",
        "what are logical fallacies , and why should we train ourselves to identify them?": "What logical fallacies are and why they matter",
        "provide 5 examples from history in which a faulty risk assessment lead to injury or loss, including lost opportunities.": "Five historical cases of badly misread risk",
        "what different daily habits do those successfully acquring deep knowledge and those pursuing a breadth of knowledge have?": "Daily habits that favor depth versus breadth",
        "write up a consultation report for a company with an ai project proposal to disrupt the esl market by providing effective ai tools directly to students.": "A consultation brief for an AI-first ESL venture",
        "based on this report, provide scores for the effects of the ubi experiment.": "Scoring the UBI experiment's main effects",
        "provide a description of the study’s method, scope, and limitations.": "The UBI study's method, scope, and limits",
        "provide recommendations for methods, scope, and variables in future ubi studies.": "How future UBI studies should improve",
        "a fundamental notion in bayes theorem is the notion that even widely disparate priors of two epistemic agents will eventually converge if identical evidence is encountered. elaborate on this notion.": "Why shared evidence can slowly pull priors together",
        "what is bayes theorem?": "What Bayes Theorem says and why it matters",
        "provide practical examples of the power of bayes theorem. instantiate the variables with clear terms in each example.": "What Bayes Theorem looks like in worked examples",
        "in conclusion, for the scenario introduced, we have no justification for taking on full ontological certainty on notions such as the external world or even logic, but can simply provisionally test each notion with deep uncertainty. the iterative testing of the notions will allow up to continuously update the priors we had placed provisionally on those notions, with greater approximation to the likely reality with each iteration. right?": "Why provisional testing beats premature ontological certainty",
        "if there is a god, what are some ways we might expect spiritual effects to be evident and measurable in our material world?": "What measurable traces a real god might leave",
        "imagine a statistical analysis of potentially disparate crime rates between a population of individuals devoted to a particular god and a population of secular-minded individuals. what might be the legitimate and illegitimate responses among those defending the god in question if the secular-minded group is shown to have lower crime rates?": "How believers might answer a bad moral-performance comparison",
        "provide accounts from history in which the pressure to take a dogmatic position led to negative consequences.": "Historical damage caused by pressure for dogmatic certainty",
        "has there been an uptick in public or academic interest in epistemology since the advent of the information age?": "Has the information age renewed interest in epistemology?",
        "create a lengthy dialogue between the author of the essay and someone who holds that one must either believe or disbelieve a given proposition.": "A dialogue between binary belief and graded belief",
        "wouldn’t the proper epistemic response be to increase or decrease our degree of certainty to map to the level of confirming or disconfirming evidence we encounter?": "Why certainty should move with the evidence",
        "what might cause individuals to irrationally conclude they cannot relinquish their current ideology unless they replace it with a new ideology?": "Why people fear abandoning an ideology without a replacement",
        "what major disagreements exist among philosophers on the proposed types of knowledge?": "Where philosophers disagree about a priori knowledge",
        "if a priori knowledge is not actually grounded through empirical experience, what else could ground this class of knowledge?": "What could ground a priori knowledge besides experience?",
        "it appears that many of those most dogmatic on particular human rights cannot articulate the logical grounding of those rights. how might we encourage a deeper contemplation of the foundation of morality and human rights?": "How to push human-rights talk toward deeper grounding",
        "survey some of the more common gods proposed throughout history, and highlight some of the more interesting ways they reflect human dispositions and behaviors.": "How gods mirror the people who imagine them",
        "comment on how the complexion and body type in depictions of jesus reflect the culture in which he is venerated.": "Why Jesus is repeatedly redrawn in the worshiper's image",
        "some would argue that the greatest harm of religion is its conscious promotion of a degree of belief that exceeds the degree of the relevant evidence which has led to a regrettable delay in humanity’s maturity. weigh in on this.": "Does religion normalize confidence beyond the evidence?",
        "members of religions often tell the unbelieving that their disbelief or doubt is a reflection of their wickedness or rebellion against the god in question. comment on the power of this tactic.": "Why moralizing disbelief is such a potent religious tactic",
        "what is stoicism?": "What Stoicism is really training",
        "give a brief introduction to the most influential stoic philosophers.": "The most influential Stoic philosophers at a glance",
        "provide 20 notable quotes from stoic philosophers.": "Twenty notable Stoic quotations worth revisiting",
        "list markers of philosophical maturity as they are manifested in domains such as the following.": "Markers of philosophical maturity across domains",
        "provide a list of quantifiable measures of philosophical maturity.": "What, if anything, can quantify philosophical maturity",
        "create a table that rates each factor contributing to a stable state and its degree of importance.": "How the main stabilizing factors compare",
        "what is the ontological status of the social contract and, given that status, what grounds it? does it entail any actual obligation or is our commitment to the social contract wholly voluntary?": "What kind of thing the social contract is, and why it binds",
        "is there a robust definition of scientism?": "What scientism claims, if it claims anything coherent",
        "some say those promoting scientism claim science can or will explain everything. is this true or is it a straw-man?": "Does scientism really say science can explain everything?",
        "if there are other sources of knowledge outside of science, what is the non-scientific way to validate the veracity of those sources?": "How non-scientific knowledge claims would have to be validated",
        "provide a list of 10 facts that have not been established through scientific methods.": "Ten claims not established by scientific method",
        "you appear to invoke “faith” as a method to verify religious knowledge. how does faith validate the veracity of a god-claim?": "Can faith validate a God-claim at all?",
        "the chatgpt quote above suggests the introduction of a spiritual realm to explain mental activities provides a “holistic” view. however, if there is no actual spiritual realm, this “holistic” view is a distortion and an illusion, right?": "Why a 'holistic' spiritual gloss can still distort explanation",
        "let me offer a syllogism to reflect my previous argument in a more rigorous manner. assuming p2 is correct, including spiritual concepts to provide a “holistic” approach is logically inappropriate, correct?": "Why a 'holistic' label does not rescue a bad explanation",
        "the quote from chatgpt above was offered in response to my p2 premise, “the spiritual realm has not been established to exist.” i did not limit the ways of knowing. non-empirical ways of knowing could establish a spiritual realm also, but the premise is that it has not been established, inclusive of any way of knowing. correct? therefore the chatgpt response referring to other way of knowing is irrelevant, correct?": "Why unestablished spiritual claims remain irrelevant here",
        "on top of the remoteness of the evidence necessary to feed an accurate inductive analysis, much of the dissent among historians seems to be emergent of the varying ascribed intentions of historical figures. please weigh in on this notion.": "Why remote evidence makes claims about historical motives fragile",
        "provide 5 historical events for which historians may have overstated their knowledge of the intentions of the actors.": "Five events where historians likely overstated what actors intended",
        "it seems the human appetite for narrative allows historians to attribute excessive causal power to individuals ( the great man theory ) rather than to other more likely mundane causes. comment on this tendency.": "Narrative hunger can exaggerate the role of individuals in history",
        "provide 5 cases in which historians have attributed the cause of an event to a “great man” when the causation very likely lies elsewhere.": "Five 'great man' explanations that likely miss the deeper causes",
        "to what degree have 1) reflection on the track records of attempted political systems and 2) a far more global culture reduced violent revolutions?": "How historical memory and global culture can reduce violent revolutions",
        "you did not mention the factor of vested interests. youth today experience far less suffering, but many more pleasures than youth in the past. they are far more content. can you comment on this factor and the reason you found it too insignificant to mention?": "How comfort and vested interests can soften revolutionary appetite",
        "gemini responded to my mention of a upward trend in comforts for youth with “ not all young people experience the same level of comfort. ” is this not irrelevant since exceptions to the average do not affect the average?": "Do exceptions weaken the broader trend toward greater youth comfort?",
        "assess the following argument for coherence": "What the miracle argument does and does not establish",
        "how might you respond to someone making this argument to make them aware of its circularity?": "How to expose the miracle argument's circularity",
        "provide me with a table with two lists, the first a list of risks that humans tend to overestimate, and the second a list of risks that humans tend to underestimate.": "Risks people overestimate versus underestimate",
        "there are times when what seems to factual disagreements turn out to be only semantic misunderstandings. elaborate on this and give examples.": "When a factual dispute is really a semantic one",
        "some semantic misunderstandings seem to be very common in public discourse. provide an annotated list of 10 of these.": "Ten semantic confusions that repeatedly derail public debate",
        "provide an pedagogical dialogue which begins with semantic confusion but ends in an clear understanding of the terms.": "A dialogue that turns semantic confusion into clarity",
        "provide a short essay on the importance of stipulating denotations for terms relevant to a subsequent discussion.": "Why early term-definition prevents wasted argument",
        "despite the aforementioned concerns, are there times in which top-down pricing might be the best course of action?": "When price controls may still be justified",
        "can the public legitimately limit the salaries of individuals who receive their wealth through non-government contracts or negotiations?": "Can the public cap privately negotiated salaries?",
        "provide, if possible, a robust coherent philosophical grounding for public salary caps for private employment contracts.": "What could philosophically justify salary caps",
        "there is often detrimental social pressure to choose a dogmatic pole on issues. comment on the social dangers this engenders, and suggest strategies to make it disreputable to pressure others into dogmatic positions.": "How social pressure pushes people into fake certainty",
        "present 3 cases in which a logical assessment revealed fatal flaws in arguments that had been largely accepted by the public.": "Three public arguments undone by logical scrutiny",
        "name a few recent issues in epistemology that philosophers are currently grappling with.": "Recent questions epistemologists are actively debating",
        "present a few recent trends or new concepts in decision theory or game theory.": "Recent moves in decision theory and game theory",
        "we have already discussed the notion that “knowledge” is simply a degree of confidence that is subjectively determined. one person might consider a 95% level of confidence to be the threshold above which they consider something “knowledge,” and another person may consider an 80% level of confidence a sufficient threshold at which the credence is considered “knowledge.” yet, some epistemologists treat knowledge as something that can be more objective, such as in the notion that “knowledge” is “justified, true belief.” is this attempt to elevate the notion of “knowledge” to a more objective status justified when considering the conventional usage of “knowledge” that has much subjective variance in its definition and application? it appears some epistemologists are attempting to wrest the term “knowledge” away from its conventional usage and coerce the term into a stipulated definition. is this correct?": "Can philosophers legitimately tighten the meaning of knowledge?",
        "let’s take a closer look at the notion that “knowledge” is “justified, true belief”. this definition appears circular. based on this definition, in order for someone to say they “know” something, the person must have assessed the knowledge as objectively true. however, this ability to objectively perceive something as true is not available to the subjectivity-bound person hoping to claim to “know” something. once we take away the ability to use the term “know” in its most useful context in which we can subjectively claim we “know” it will rain tomorrow without needing access to the objective truth of the claim, then we have, indeed, wrest away the term from its conventional usage, and are providing a stipulation that has no relevance in daily life, right?": "Why justified true belief feels too strict for ordinary knowing",
        "i suggest we abandon the highly problematic and tired project of finding a rigorous and coherent non-conventional definition of “knowledge”, and to instead focus on defining rational belief? do you not think this would be a more successful focus, especially since the “epistemic turn” away from binary notions of belief and knowledge and towards more nuanced expressions of belief, such as credences and degrees of confidence?": "Why rational belief may be a better target than knowledge",
        "provide a full and rigorous definition of a religion.": "What a rigorous definition of religion must include",
        "provide a comprehensive list of religions’ goods and ills.": "Religion's recurring goods and recurring harms",
    }
    normalized_exact_overrides = {key.rstrip("?."): value for key, value in exact_overrides.items()}
    prompt_key = prompt_lower.rstrip("?.")
    if prompt_key in normalized_exact_overrides:
        return normalized_exact_overrides[prompt_key]

    if re.match(r"^(what|why|how|can|could|should|would|is|are|does|do|will|to what degree)\b", prompt_lower):
        return trim_heading_length(sentence_case(cleaned) + "?") if not cleaned.endswith("?") else trim_heading_length(sentence_case(cleaned))
    if re.match(r"^(list|introduce)\b", prompt_lower):
        rewritten = re.sub(r"^(list|introduce)\s+", "", cleaned, flags=re.I).rstrip(".")
        return trim_heading_length(sentence_case(rewritten))
    if prompt_lower.startswith("assess "):
        rewritten = re.sub(r"^assess\s+", "", cleaned, flags=re.I).rstrip(".")
        return trim_heading_length(sentence_case(rewritten))
    if prompt_lower.startswith("create a hypothetical debate"):
        rewritten = re.sub(r"^create\s+", "", cleaned, flags=re.I).rstrip(".")
        return trim_heading_length(sentence_case(rewritten))

    substitutions = [
        (r"^provide (?:an|a|the)\s+", ""),
        (r"^provide\s+", ""),
        (r"^create (?:an|a|the)\s+", ""),
        (r"^create\s+", ""),
        (r"^write an essay on\s+", ""),
        (r"^write\s+", ""),
        (r"^discuss\s+", ""),
        (r"^comment on and give examples of\s+", ""),
        (r"^comment on\s+", ""),
        (r"^explain how\s+", ""),
        (r"^expand on\s+", ""),
        (r"^elaborate on\s+", ""),
        (r"^introduce\s+", ""),
        (r"^present\s+", ""),
        (r"^make\s+", ""),
        (r"^respond to\s+", "A response to "),
        (r"^let’s focus on\s+", ""),
        (r"^let's focus on\s+", ""),
    ]
    rewritten = cleaned
    for pattern, replacement in substitutions:
        newer = re.sub(pattern, replacement, rewritten, flags=re.I)
        if newer != rewritten:
            rewritten = newer
            break

    rewritten = rewritten.strip().rstrip(".")
    if rewritten:
        rewritten = sentence_case(rewritten)

    return trim_heading_length(rewritten or page_title)


def is_placeholder_paragraph(text: str) -> bool:
    return any(pattern.search(text) for pattern in PLACEHOLDER_PATTERNS)


def topic_from_heading(heading: str, page_title: str) -> str:
    cleaned = re.sub(r"\s+", " ", heading).strip().rstrip(".")
    cleaned = re.sub(r"^What\s+", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+actually clarifies$", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+becomes clearer once.*$", "", cleaned, flags=re.I)
    return cleaned or page_title


def lower_topic(topic: str) -> str:
    if not topic:
        return "the issue"
    return topic[0].lower() + topic[1:]


def generate_intro_paragraphs(page_title: str, heading: str, prompt: str) -> list[str]:
    prompt_lower = prompt.lower()
    topic = topic_from_heading(heading, page_title)
    topic_lower = lower_topic(topic)

    if "present five cases" in prompt_lower or "present five" in prompt_lower:
        return [
            f"This issue becomes easiest to see when the same linguistic move is tracked across several concrete disputes rather than described in the abstract.",
            "A strong answer should show what remains constant from case to case, how the framing shifts sympathy or blame, and why the altered wording does argumentative work before explicit evidence even arrives.",
        ]
    if "design a short course" in prompt_lower or prompt_lower.startswith("design "):
        return [
            f"A useful course on {topic_lower} should train recognition before moralizing about better behavior.",
            "Students need repeated practice comparing rival phrasings, identifying the hidden verdict inside the wording, and rewriting live cases in language that is fairer without becoming bland.",
        ]
    if "provide a list of resources" in prompt_lower or "resources" in prompt_lower:
        return [
            "A good reading path here should not stay in one lane, because the problem mixes formal structure, probabilistic updating, and ordinary human limits.",
            "The strongest resource list therefore combines conceptual introductions, technical tools, and cognitive-bias material so the reader can understand both the model and the reasons real people mishandle it.",
        ]
    if prompt_lower.startswith("provide a clear demarcation"):
        return [
            f"The key task here is not to multiply labels but to keep the boundary around {topic_lower} sharp enough that one category cannot quietly do the work of the other.",
            "A useful answer has to state what belongs on each side of the line, what kinds of evidence count for each, and where the two are commonly but misleadingly blurred together.",
        ]
    if prompt_lower.startswith("describe "):
        return [
            f"{topic} should be treated as a package of gains, losses, and shifted incentives rather than as a moral reflex or political chant.",
            "A useful answer needs to identify who benefits, who bears the costs, which mechanisms plausibly produce each effect, and what evidence would show whether the tradeoffs are local, temporary, or durable.",
        ]
    if "weigh in on" in prompt_lower or prompt_lower.startswith("weigh in"):
        return [
            "The pressure in this argument comes from a real tension, not from a cartoon disagreement between freedom and regulation.",
            "A careful response should grant the attraction of the autonomy claim, then test where unequal bargaining power, exploitation risk, and broader wage effects limit how far that claim can responsibly be pushed.",
        ]
    if prompt_lower.startswith("comment on") or "please comment on" in prompt_lower:
        return [
            f"This prompt is not only asking for a reaction to {topic_lower}; it is asking what judgment becomes distorted when the framing is left unexamined.",
            "A strong answer should identify the recurring pattern, show why it is rhetorically tempting, and clarify what habits of thought keep the case from being decided by tone alone.",
        ]
    if prompt_lower.startswith("elaborate on"):
        return [
            f"The page needs to do more than name {topic_lower}; it needs to make the view's logic and limits visible.",
            "A strong explanation should say what the position claims, what pressure gave rise to it, and where its strongest objection or internal instability is likely to appear.",
        ]
    if prompt_lower.startswith("how should") or prompt_lower.startswith("how might"):
        return [
            f"The practical value of this section depends on turning {topic_lower} into a usable habit of judgment rather than leaving it as a slogan.",
            "The best answer should show what to notice, what to resist, and what a disciplined response looks like once the pressure moves from theory into an actual conversation or decision.",
        ]
    if prompt_lower.startswith("what ") or prompt_lower.startswith("why ") or prompt_lower.startswith("can ") or prompt_lower.startswith("will "):
        return [
            f"The real work in this section is to make {topic_lower} intelligible without pretending the answer is simpler than it is.",
            "That requires clarifying the main claim, the tension or evidence that makes the claim worth discussing, and the point where an easy reading would start to overstate what follows.",
        ]
    return [
        f"This section works best when {topic_lower} is treated as a concrete intellectual problem rather than as a settled label.",
        "The answer should clarify the central claim, show what gives it force, and identify the comparison, objection, or example that keeps the discussion honest.",
    ]


def replace_placeholder_intro(soup: BeautifulSoup, section: Tag, page_title: str) -> bool:
    heading = section.find("h2", recursive=False)
    if heading is None:
        return False

    after_heading: list[Tag] = []
    for sibling in heading.find_next_siblings():
        if not isinstance(sibling, Tag):
            continue
        if sibling.name != "p":
            break
        after_heading.append(sibling)

    if not after_heading:
        return False

    placeholder_nodes = []
    for node in after_heading:
        text = " ".join(node.get_text(" ", strip=True).split())
        if is_placeholder_paragraph(text):
            placeholder_nodes.append(node)
        else:
            break

    if not placeholder_nodes:
        return False

    prompt = section_prompt(section)
    replacements = generate_intro_paragraphs(page_title, heading.get_text(" ", strip=True), prompt)
    first = placeholder_nodes[0]
    for paragraph in reversed(replacements):
        new_tag = soup.new_tag("p")
        new_tag.string = paragraph
        first.insert_before(new_tag)
    for node in placeholder_nodes:
        node.decompose()
    return True


def remove_placeholder_list_items(section: Tag) -> bool:
    changed = False
    for item in section.find_all("li"):
        text = " ".join(item.get_text(" ", strip=True).split())
        if any(pattern.search(text) for pattern in PLACEHOLDER_LIST_PATTERNS + SCAFFOLD_LIST_PATTERNS):
            item.decompose()
            changed = True

    for list_tag in section.find_all(["ol", "ul"]):
        if not list_tag.find_all("li"):
            list_tag.decompose()
            changed = True
    return changed


def remove_generated_generic_paragraphs(section: Tag) -> bool:
    heading = section.find("h2", recursive=False)
    if heading is None:
        return False

    changed = False
    for sibling in list(heading.find_next_siblings()):
        if not isinstance(sibling, Tag):
            continue
        if sibling.name != "p":
            break
        text = " ".join(sibling.get_text(" ", strip=True).split())
        if any(pattern.search(text) for pattern in GENERATED_GENERIC_PATTERNS + SCAFFOLD_PARAGRAPH_PATTERNS):
            sibling.decompose()
            changed = True
    return changed


def fix_dialogue_speaker_quotes(soup: BeautifulSoup) -> bool:
    changed = False
    for speaker in soup.select("span.dialogue-turn__speaker"):
        label = speaker.get_text("", strip=True)
        if "“" not in label or "”" in label:
            continue

        current = speaker.next_sibling
        absorbed = ""
        while current is not None:
            if isinstance(current, NavigableString):
                text = str(current)
                if "”" in text:
                    before, after = text.split("”", 1)
                    absorbed += before
                    speaker.string = label + absorbed + "”"
                    current.replace_with(after)
                    changed = True
                    break
                absorbed += text
                next_sibling = current.next_sibling
                current.extract()
                current = next_sibling
                continue
            break
    return changed


def repair_page(path: Path) -> bool:
    original = path.read_text()
    soup = BeautifulSoup(original, "html.parser")
    page_title = soup.find("h1").get_text(" ", strip=True) if soup.find("h1") else path.parent.name

    changed = fix_dialogue_speaker_quotes(soup)

    for section in soup.select("section.article-section--prompt"):
        heading = section.find("h2", recursive=False)
        prompt = section_prompt(section)
        if heading is not None:
            normalized = normalize_heading(heading.get_text(" ", strip=True), page_title, prompt)
            if normalized != heading.get_text(" ", strip=True):
                heading.string = normalized
                changed = True
        if replace_placeholder_intro(soup, section, page_title):
            changed = True
        if remove_generated_generic_paragraphs(section):
            changed = True
        if remove_placeholder_list_items(section):
            changed = True

    for list_tag in soup.find_all(["ol", "ul"]):
        if not list_tag.find_all("li"):
            list_tag.decompose()
            changed = True

    if not changed:
        return False

    path.write_text(str(soup))
    return True


def main() -> int:
    changed = []
    for path in load_batch_paths():
        if repair_page(path):
            changed.append(path.relative_to(ROOT))
    print(f"Repaired {len(changed)} batch pages.")
    for path in changed:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
