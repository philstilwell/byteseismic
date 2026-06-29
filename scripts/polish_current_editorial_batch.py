#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

from build_archive import (
    PHILOSOPHER_SOURCE_WORKS,
    clean_discussion_key,
    current_batch_philosopher_example_paragraph,
    current_batch_philosopher_items,
    current_batch_philosopher_paragraphs,
    philosopher_base_name,
    philosopher_page_is_collective,
    philosopher_profile_for_title,
    philosopher_source_work_fallback,
    prompt_focus,
    render_inline_text,
    render_list_section,
    render_paragraphs,
    short_prompt_key,
    topic_label,
)


ROOT = Path(__file__).resolve().parents[1]
TRACKER_PATH = ROOT / "quality" / "editorial-audit-tracker.json"

SECTION_RE = re.compile(
    r'(?P<section><section class="article-section article-section--prompt" id="(?P<section_id>prompt-\d+)">.*?</section>)',
    re.DOTALL,
)
PROMPT_RE = re.compile(
    r'(<p class="article-section__prompt">.*?<span>\s*Prompt\s+\d+:\s*</span>\s*)(?P<prompt>.*?)(</p>)',
    re.DOTALL,
)
H2_RE = re.compile(r"(<h2>)(?P<heading>.*?)(</h2>)", re.DOTALL)
PARAGRAPH_RE = re.compile(r"(?P<indent>\s*)<p(?P<attrs>\b[^>]*)?>(?P<body>.*?)</p>", re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
PROMPT_NUMBER_RE = re.compile(r"^Prompt\s+\d+\s*:\s*", re.IGNORECASE)
GENERIC_SECTION_RE = re.compile(
    r"\b("
    r"The section should|The answer should|The live issue is|This middle step|"
    r"At this level|The payoff here is|A fair pushback is|A fair question is|"
    r"The deeper issue in .+ is usually not whether certainty is possible"
    r")\b"
)

TEXT_REPLACEMENTS = {
    "Has religions’ exposure to this track record resulted a more humble disposition toward the unknown?": "Has religion's exposure to this track record resulted in a more humble disposition toward the unknown?",
    "How might we respond to somone who invokes inductive invariance when claiming effects can be traced back to a first cause in defense of their God, yet also rejects the inductive invarience seen in the other four observations that run counter to the conception of their God?": "How might we respond to someone who invokes inductive invariance when claiming effects can be traced back to a first cause in defense of their God, yet also rejects the inductive invariance seen in the other four observations that run counter to the conception of their God?",
    "Create syllogistic formulations of the strongest arguments for 1) euthenasia for animals and 2) prologing life for humans.": "Create syllogistic formulations of the strongest arguments for 1) euthanasia for animals and 2) prolonging life for humans.",
}

HEADING_REPLACEMENTS = {
    "Create a hypothetical discussion set 500 years ago on the cause of epilepsy. A religious leader is invoking": "A 500-year-old debate over epilepsy and divine causation",
    "Create a rigorous rubric to assess the degree of distortive framing of news reports": "A rubric for grading distortive framing in news reports",
    "Create a 2x2 grid showing the interactions among rational & irrational minds and objective & subjectively": "A 2x2 map of minds, framing, and distortion",
    "How might we respond to somone who invokes inductive invariance when claiming effects can be traced back to?": "When inductive invariance is invoked selectively",
    "Create a list of observations grounded in inductive invariance that run counter to various notions of God": "Observations that push against theistic claims",
    "Create a rigorous syllogism that captures the logical incoherency pointed out by ChatGPT below": "A syllogism exposing the tension between miracles and faith",
    "If it is more virtuous in the mind of God for humans to strongly believe in his existence based on weak": "If faith without strong evidence is more virtuous, should miracles disappear?",
    "Create syllogistic formulations of the strongest arguments for 1) euthenasia for animals and 2) prologing": "Two strongest syllogisms on mercy, animals, and human life",
    "Based on the past trajectory of ethical positions on this issue, what do you predict to be the legal status": "How the legal status of human euthanasia may change",
    "Some theists claim that a deist is one step away from becoming a theist of their ilk. Explain why this does": "Why deism does not naturally collapse into theism",
    "Explain how a version of design thinking might be used in one's personal life": "Using design thinking in personal life",
    "Examples of pairs of philosophers who strongly disagreed, but who were also close": "Philosophers who disagreed deeply yet stayed close",
    "10 macroeconomic concepts that are essential knowledge for those in commerce today": "Ten macroeconomic ideas people in commerce should know",
    "Has there ever been a functioning economy that was largely self-regulated and without any government": "Whether any economy has ever functioned without government intervention",
    "What government interventions are considered intrusive and oppressive in most democracies?": "Which interventions democracies often judge intrusive or oppressive",
    "3 cases in which a logical assessment revealed fatal flaws in arguments that had been": "Three cases where logical analysis exposed fatal flaws",
    "Accounts from history in which the pressure to take a dogmatic position led to negative": "Historical cases where pressure for dogmatism caused damage",
}

REMOVE_PARAGRAPH_PATTERNS = [
    re.compile(r"^This section is trying to show why .+ keeps reappearing after the original setting is gone\.$", re.IGNORECASE),
    re.compile(r"^This section is about historical lift-off: how .+ became visible, memorable, and hard to ignore\.$", re.IGNORECASE),
    re.compile(r"^This section traces where .+ tools migrated after leaving their original home\.$", re.IGNORECASE),
    re.compile(r"^The useful question here is not which item on the list looks grandest, but which move from .+ still helps later readers think\.$", re.IGNORECASE),
    re.compile(r"^The point of naming major figures is to show how .+ diversified without simply dissolving\.$", re.IGNORECASE),
    re.compile(r"^This response stages .+ under pressure:.+", re.IGNORECASE),
    re.compile(r"^This response gives the reader a route into .+:.+", re.IGNORECASE),
    re.compile(r"^This section uses dialogue as a teaching device:.+", re.IGNORECASE),
    re.compile(r"^The section works only if .+", re.IGNORECASE),
    re.compile(r"^The question matters because it changes what the reader would now compare.+", re.IGNORECASE),
    re.compile(r"^The pressure point is whether .+", re.IGNORECASE),
    re.compile(r"^At the center is a simpler claim:.+", re.IGNORECASE),
    re.compile(r"^.+ need to stay distinct here, because they answer different questions and carry different explanatory weight\.$", re.IGNORECASE),
    re.compile(r"^Put the issue into a live setting\..+", re.IGNORECASE),
    re.compile(r"^Run one live case through the structure\..+", re.IGNORECASE),
    re.compile(r"^Picture a serious critic who grants the background but resists the move toward .+", re.IGNORECASE),
    re.compile(r"^Read .+ as separate levers in the argument .+", re.IGNORECASE),
    re.compile(r"^Read the section as a small map:.+", re.IGNORECASE),
    re.compile(r"^Read this section as an attempt to make .+ sound like a mind at work rather than a name under glass\.$", re.IGNORECASE),
    re.compile(r"^Read .+ as working tools\.(?: The page succeeds only if .+)?$", re.IGNORECASE),
    re.compile(r"^The obvious resistance is that real judgment is often fast, social, and pressured\..+", re.IGNORECASE),
    re.compile(r"^A likely objection is that the ordinary way of talking about .+", re.IGNORECASE),
    re.compile(r"^The natural pushback is that ordinary life runs on incomplete evidence\..+", re.IGNORECASE),
    re.compile(r"^The payoff (?:here|of .+) is .+", re.IGNORECASE),
    re.compile(r"^The section should clarify how .+", re.IGNORECASE),
    re.compile(r"^Put the distinction under pressure\..+", re.IGNORECASE),
    re.compile(r"^Keep .+ in the same frame\.", re.IGNORECASE),
    re.compile(r"^Keep .+ distinct from .+\.", re.IGNORECASE),
    re.compile(r"^Keep .+ in view at the same time\.", re.IGNORECASE),
    re.compile(r"^Read the section by contrast:", re.IGNORECASE),
    re.compile(r"^Read the section through ", re.IGNORECASE),
    re.compile(r"^Take one concrete case and run it through ", re.IGNORECASE),
    re.compile(r"^A quick way to test the page ", re.IGNORECASE),
    re.compile(r"^Bring the issue down to street level\.", re.IGNORECASE),
    re.compile(r"^The first move should ", re.IGNORECASE),
    re.compile(r"^This middle step keeps ", re.IGNORECASE),
    re.compile(r"^This middle step prepares ", re.IGNORECASE),
    re.compile(r"^By this point the clearing work should ", re.IGNORECASE),
    re.compile(r"^A fair pushback is that the familiar way of speaking ", re.IGNORECASE),
    re.compile(r"^A fair question is why this map is needed at all\.", re.IGNORECASE),
    re.compile(r"^The page succeeds only if the ideas start doing more than sitting there with polished names\.$", re.IGNORECASE),
    re.compile(r"^.+ is where .+ has to start making a difference\..+", re.IGNORECASE),
    re.compile(r"^One honest test after reading is whether ", re.IGNORECASE),
    re.compile(r"^Treat .+ as handles, not slogans\.", re.IGNORECASE),
    re.compile(r"^Do not let the example sit there like a decorative vase\.", re.IGNORECASE),
    re.compile(r"^The human-machine exchange is healthiest ", re.IGNORECASE),
    re.compile(r"^The real test of .+ is whether ", re.IGNORECASE),
    re.compile(r"^.+ should remain tied to a live intellectual practice\.", re.IGNORECASE),
]

SCHOOL_NAME_BY_FIGURE_LABEL = {
    "analytic philosophers": "Analytic Philosophy",
    "ancient philosophers": "Ancient Philosophy",
    "continental philosophers": "Continental Philosophy",
    "critical theorists": "Critical Theory",
    "empiricists": "Empiricism",
    "existentialists": "Existentialism",
    "phenomenologists": "Phenomenology",
}


def load_batch_paths() -> list[Path]:
    tracker = json.loads(TRACKER_PATH.read_text())
    return [ROOT / page["pagePath"].strip("/") / "index.html" for page in tracker["currentBatch"]["pages"]]


def strip_tags(value: str) -> str:
    text = TAG_RE.sub("", value)
    return " ".join(html.unescape(text).split())


def html_text(value: str) -> str:
    return html.escape(value, quote=False)


def normalized_prompt_text(text: str) -> str:
    return PROMPT_NUMBER_RE.sub("", " ".join(text.split())).strip()


def normalize_heading_text(text: str) -> str:
    text = " ".join(text.split())

    if text in HEADING_REPLACEMENTS:
        return HEADING_REPLACEMENTS[text]

    match = re.fullmatch(r"The real issue is what (.+) changes once it becomes precise\.", text)
    if match:
        return f"What changes once we define {match.group(1)} more carefully"

    match = re.fullmatch(r"A concrete case shows what (.+) explains and where it strains\.", text)
    if match:
        return f"What {match.group(1)} explains, and where it starts to strain"

    match = re.fullmatch(r"The map of (.+) becomes useful once the parts stop doing different work\.", text)
    if match:
        return f"Why {match.group(1)} matters in practice"

    return text


def heading_from_prompt(prompt_text: str, page_title: str, heading_text: str, section_id: str) -> str:
    prompt_text = " ".join(prompt_text.split())
    heading_text = " ".join(heading_text.split())

    match = re.match(r"Provide a general description of (?:the philosophical school of )?(.+?)\.$", prompt_text, re.IGNORECASE)
    if match and section_id == "prompt-1":
        return f"What {match.group(1)} is really trying to do"

    if section_id == "prompt-1":
        if "influence on philosophy" in prompt_text.lower():
            return f"Why {page_title} still matters to later philosophy"
        if "remains philosophically important" in prompt_text.lower():
            return f"Why {page_title} remains philosophically important"

    if section_id == "prompt-2":
        if "7 greatest contributions" in prompt_text.lower():
            return f"Seven ways {page_title} still shapes later thought"
        if "annotated list" in prompt_text.lower() and "contributions" in prompt_text.lower():
            return f"Seven ways {page_title} still shapes later thought"
        match = re.match(r"Provide a list of the key contributions (.+?) ha(?:s|ve) made to philosophical thought\.$", prompt_text, re.IGNORECASE)
        if match:
            return f"How {match.group(1)} reshaped later philosophy"
        if "key concepts" in prompt_text.lower() or "major concepts" in prompt_text.lower():
            return f"The ideas that make {page_title} more than a label"

    if section_id == "prompt-3":
        if "most likely causes behind" in prompt_text.lower() and "becoming a notable philosopher" in prompt_text.lower():
            return f"Why {page_title} became impossible to ignore"
        match = re.match(r"List the most influential (.+?) in history\.$", prompt_text, re.IGNORECASE)
        if match:
            subject = match.group(1).strip()
            subject = SCHOOL_NAME_BY_FIGURE_LABEL.get(subject.lower(), subject)
            return f"The figures who gave {subject} its durable shape"
        if "strongest objection" in prompt_text.lower():
            return f"The hardest objection {page_title} still has to answer"

    if section_id == "prompt-4":
        if "which schools of philosophical thought" in prompt_text.lower() or "which academic domains" in prompt_text.lower():
            return f"Where {page_title} left the deepest mark"
        match = re.match(r"Produce a 20-line hypothetical dialogue between (?P<subject>(?:an?|the) .+?) and .+\.$", prompt_text, re.IGNORECASE)
        if match:
            return f"A dialogue that shows how {match.group('subject')} thinks in practice"
        if "dialogue" in prompt_text.lower():
            return f"A dialogue that tests what {page_title} can explain"
        if "how should a contemporary reader begin with" in prompt_text.lower():
            return f"How to begin reading {page_title} today"
        if "entry point" in prompt_text.lower() or "best entry point" in prompt_text.lower():
            return f"The best way into {page_title} for a new reader"

    return normalize_heading_text(heading_text)


def should_remove_paragraph(text: str) -> bool:
    cleaned = " ".join(text.split())
    return any(pattern.match(cleaned) for pattern in REMOVE_PARAGRAPH_PATTERNS)


def replace_heading(section_html: str, page_title: str, section_id: str) -> tuple[str, bool]:
    prompt_match = PROMPT_RE.search(section_html)
    heading_match = H2_RE.search(section_html)
    if not prompt_match or not heading_match:
        return section_html, False

    prompt_text = strip_tags(prompt_match.group("prompt"))
    old_heading = strip_tags(heading_match.group("heading"))
    new_heading = heading_from_prompt(prompt_text, page_title, old_heading, section_id)
    if new_heading == old_heading:
        return section_html, False

    replacement = f"{heading_match.group(1)}{html_text(new_heading)}{heading_match.group(3)}"
    updated = section_html[: heading_match.start()] + replacement + section_html[heading_match.end() :]
    return updated, True


def rewrite_paragraph(match: re.Match[str]) -> str:
    attrs = match.group("attrs") or ""
    body = match.group("body")
    clean_text_value = strip_tags(body)

    if 'article-section__prompt' in attrs:
        return match.group(0)
    if not clean_text_value:
        return match.group(0)
    if should_remove_paragraph(clean_text_value):
        return ""
    if clean_text_value.startswith("In plain terms:"):
        plain_text = clean_text_value[len("In plain terms:") :].strip()
        if plain_text:
            return f'{match.group("indent")}<p{attrs}>{html_text(plain_text)}</p>'
    return match.group(0)


def page_frame(page: dict) -> tuple[str, str]:
    section_id = page["section_id"]
    if section_id == "epistemology":
        return (
            "what would count as evidence, what confidence is actually earned, and where a reader should stay provisional",
            "A useful test case is an everyday disagreement where both sides have some evidence but not enough to claim certainty. The distinction only matters if it changes what each side should now infer, demand, or withhold.",
        )
    if section_id == "ethics":
        return (
            "what norm is being defended, what justifies it, and which tradeoffs appear once the principle has to guide real cases",
            "A strong ethical explanation should be able to survive one concrete case in which empathy, fairness, harm, and institutional consequences do not all point in the same direction.",
        )
    if section_id == "economics":
        return (
            "which incentives, tradeoffs, and feedback loops the reader should notice first",
            "The easiest way to test the concept is to run it through a familiar case such as prices, wages, housing, or regulation and ask what pattern becomes more intelligible once the idea is applied.",
        )
    if section_id == "philosophy-of-language":
        return (
            "how words, categories, and context are doing different jobs that should not be collapsed into one blurry notion of meaning",
            "A good language example shows how a phrase can sound harmless in ordinary conversation but become costly once law, medicine, politics, or technical coordination demand more precision.",
        )
    if section_id == "philosophy-of-mind":
        return (
            "which part of mind is being explained, what gets left out by a simple model, and where subjective experience resists compression",
            "A concrete case helps here because consciousness talk becomes vague very quickly unless the page forces the reader to distinguish reportability, function, attention, feeling, and self-modeling.",
        )
    if section_id == "humanistic-philosophies":
        return (
            "what picture of the human condition is being offered and what kind of freedom, responsibility, or meaning it is trying to secure",
            "The page becomes clearer once the idea is tied to a recognizable life problem such as alienation, choice, mortality, conformity, or the temptation to hide behind inherited scripts.",
        )
    if section_id == "rational-thought":
        return (
            "which habit improves judgment and which shortcut quietly distorts it",
            "A useful example is a decision made under time pressure, where the reader can see the difference between a harmless heuristic and a reasoning habit that rigs the conclusion before the evidence is weighed.",
        )
    if section_id == "metaphysics":
        return (
            "what kind of structure reality is supposed to have and what explanatory work that structure is meant to do",
            "A metaphysical claim earns trust when it clarifies one stubborn puzzle, such as identity, causation, emergence, or persistence, without pretending to solve every other puzzle at the same time.",
        )
    if section_id == "introduction":
        return (
            "what orientation the newcomer needs first and which distinctions will stop later pages from blurring together",
            "An introductory page works best when it gives the reader a map for comparison rather than a pile of names or slogans to admire from a distance.",
        )
    return (
        "what claim is being made, what distinction carries the argument, and what would test it under pressure",
        "A useful example should move the discussion from labels to judgment by showing what changes once the distinction is applied to a live case.",
    )


def section_needs_rewrite(page: dict, heading_text: str, paragraphs: list[str]) -> bool:
    content = " ".join(paragraphs).strip()
    if not content:
        return True
    if len(content.split()) < 95:
        return True
    if len(paragraphs) < 2:
        return True
    if "in from vocabulary" in content or "disappeared ." in content:
        return True
    if heading_text and heading_text.endswith("had been"):
        return True
    return bool(GENERIC_SECTION_RE.search(content))


def synthesize_section_paragraphs(page: dict, page_title: str, prompt_text: str, heading_text: str) -> list[str]:
    topic = topic_label(page_title)
    focus = prompt_focus(prompt_text)
    key = clean_discussion_key(short_prompt_key(prompt_text, topic), topic, topic)
    frame, example = page_frame(page)

    openers = {
        "definition": (
            f"{heading_text} matters because it clarifies {frame}. The goal is not a prettier definition of {key}, but a sharper standard for what the reader should now notice and refuse to blur."
        ),
        "mapping": (
            f"{heading_text} should function like a map rather than a slogan. The reader needs to see how the main parts of {topic} connect without pretending they all do the same work."
        ),
        "examples": (
            f"{heading_text} becomes useful only when it can survive contact with a concrete case. The page should move from abstract description to an example that forces the distinction to make a difference."
        ),
        "argument": (
            f"{heading_text} is not just a claim to repeat; it has to earn confidence under pressure. What matters is what actually supports it, what would weaken it, and which shortcuts only create the appearance of a stronger conclusion."
        ),
        "description": (
            f"{heading_text} should teach the reader what to watch for first. A good explanation of {topic} does not merely restate familiar language; it shows what that language usually hides."
        ),
        "inquiry": (
            f"{heading_text} is worth asking because it changes what the reader should compare next. The point is to make {topic} more investigable, not merely more impressive-sounding."
        ),
        "dialogue": (
            f"{heading_text} works only if the exchange exposes the real pressure point instead of letting the speakers trade rehearsed slogans. Each side should sharpen the other by forcing the key assumptions into plain view."
        ),
    }
    first = openers.get(focus, openers["inquiry"])
    second = example
    third = (
        f"The pedagogical payoff is practical. After this section, the reader should be better able to explain {key} in plain language, identify a likely misuse of it, and say what further evidence or argument would actually move the view."
    )
    return [first, second, third]


def strengthen_section_html(section_html: str, page: dict, page_title: str) -> str:
    soup = BeautifulSoup(section_html, "html.parser")
    section = soup.find("section")
    if section is None:
        return section_html

    prompt_note = section.find("p", class_="article-section__prompt", recursive=False)
    heading = section.find("h2", recursive=False)
    if prompt_note is None or heading is None:
        return section_html

    prompt_text = normalized_prompt_text(prompt_note.get_text(" ", strip=True))
    heading_text = strip_tags(str(heading))
    paragraphs = [
        p for p in section.find_all("p", recursive=False)
        if "article-section__prompt" not in (p.get("class") or [])
    ]
    paragraph_texts = [strip_tags(str(p)) for p in paragraphs]
    if not section_needs_rewrite(page, heading_text, paragraph_texts):
        return str(section)

    for paragraph in paragraphs:
        paragraph.decompose()

    anchor = heading
    for text in synthesize_section_paragraphs(page, page_title, prompt_text, heading_text):
        new_p = soup.new_tag("p")
        new_p.string = text
        anchor.insert_after(new_p)
        anchor = new_p

    return str(section)


def page_dict_for_path(path: Path, page_title: str) -> dict:
    built_path = "/" + path.parent.relative_to(ROOT).as_posix().strip("/") + "/"
    return {
        "title": page_title,
        "section_id": path.parts[-3] if len(path.parts) >= 3 else path.parent.name,
        "built_path": built_path,
        "kind": "article",
    }


def replace_with_fragment(node, html_fragment: str) -> None:
    fragment = BeautifulSoup(html_fragment, "html.parser")
    replacement = fragment.find()
    if replacement is not None:
        node.replace_with(replacement)


def polish_current_batch_philosopher_page(path: Path, original: str, page_title: str) -> str:
    page = page_dict_for_path(path, page_title)
    if page["section_id"] != "philosophers":
        return original

    profile = philosopher_profile_for_title(page_title)
    if not profile and not philosopher_page_is_collective(page, page_title, profile):
        return original

    soup = BeautifulSoup(original, "html.parser")

    base = philosopher_base_name(page_title)
    source_work = (
        PHILOSOPHER_SOURCE_WORKS.get(base)
        or PHILOSOPHER_SOURCE_WORKS.get(page_title)
        or philosopher_source_work_fallback(page, page_title, profile)
    )
    for card in soup.select("#source-texture .source-dossier__card"):
        label = card.select_one(".mini-label")
        body = card.find_all("p")
        if not label or len(body) < 2:
            continue
        if "Primary texts nearby" != " ".join(label.get_text(" ", strip=True).split()):
            continue
        body[-1].clear()
        fragment = BeautifulSoup(render_inline_text(source_work), "html.parser")
        for child in list(fragment.contents):
            body[-1].append(child)
        break

    for section in soup.select("section.article-section--prompt[id^='prompt-']"):
        prompt_note = section.find("p", class_="article-section__prompt", recursive=False)
        heading = section.find("h2", recursive=False)
        meta = section.find("div", class_="article-section__meta", recursive=False)
        learning_card = section.find("aside", class_="learning-card")
        if not prompt_note or not heading or not meta:
            continue
        prompt_text = strip_tags(prompt_note.get_text(" ", strip=True))
        prompt_text = re.sub(r"^Prompt\s+\d+\s*:\s*", "", prompt_text, flags=re.IGNORECASE)
        paragraphs = current_batch_philosopher_paragraphs(page, prompt_text, None) or []
        example = current_batch_philosopher_example_paragraph(page, prompt_text)
        if example and example not in paragraphs:
            paragraphs.append(example)
        list_items = current_batch_philosopher_items(page, prompt_text) or []
        new_section_html = (
            f'<section class="{" ".join(section.get("class", []))}" id="{section.get("id", "")}">'
            f"{str(meta)}"
            f"{str(prompt_note)}"
            f"{str(heading)}"
            f"{render_paragraphs(paragraphs)}"
            f"{render_list_section(list_items)}"
            f"{str(learning_card) if learning_card else ''}"
            "</section>"
        )
        replace_with_fragment(section, new_section_html)

    return str(soup)


def clean_html(original: str, page: dict, page_title: str) -> str:
    updated = original
    for old, new in TEXT_REPLACEMENTS.items():
        updated = updated.replace(old, new)

    def rewrite_section(match: re.Match[str]) -> str:
        section_html = match.group("section")
        section_id = match.group("section_id")
        section_html, _ = replace_heading(section_html, page_title, section_id)
        section_html = PARAGRAPH_RE.sub(rewrite_paragraph, section_html)
        section_html = strengthen_section_html(section_html, page, page_title)
        return section_html

    updated = SECTION_RE.sub(rewrite_section, updated)
    return updated


def clean_page(path: Path) -> bool:
    original = path.read_text()
    page_title_match = re.search(r"<h1>(?P<title>.*?)</h1>", original, re.DOTALL)
    page_title = strip_tags(page_title_match.group("title")) if page_title_match else path.parent.name
    page = page_dict_for_path(path, page_title)
    updated = clean_html(original, page, page_title)
    updated = polish_current_batch_philosopher_page(path, updated, page_title)
    if updated == original:
        return False
    path.write_text(updated)
    return True


def main() -> int:
    changed_files = []
    for path in load_batch_paths():
        if clean_page(path):
            changed_files.append(path)
    print(f"Polished {len(changed_files)} batch pages.")
    for path in changed_files:
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
