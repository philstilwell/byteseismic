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
]

PLACEHOLDER_LIST_PATTERNS = [
    re.compile(r"This matters only if it changes how meaning, use, ambiguity, or reference is being handled\.", re.I),
    re.compile(r"The epistemic pressure is how evidence, uncertainty, and responsible confidence interact", re.I),
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
]

SCAFFOLD_LIST_PATTERNS = [
    re.compile(r"^State the clearest version of .+ before testing it\.$", re.I),
    re.compile(r"^Ask what evidence, example, or argument would genuinely change the reader's judgment\.$", re.I),
    re.compile(r"^Notice where a familiar phrase is doing more work than the reasoning beneath it\.$", re.I),
    re.compile(r"^Keep the neighboring concepts visible so the page does not collapse different questions together\.$", re.I),
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
    return text


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
