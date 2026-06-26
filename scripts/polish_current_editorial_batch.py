#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from pathlib import Path


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


def clean_html(original: str, page_title: str) -> str:
    updated = original
    for old, new in TEXT_REPLACEMENTS.items():
        updated = updated.replace(old, new)

    def rewrite_section(match: re.Match[str]) -> str:
        section_html = match.group("section")
        section_id = match.group("section_id")
        section_html, _ = replace_heading(section_html, page_title, section_id)
        section_html = PARAGRAPH_RE.sub(rewrite_paragraph, section_html)
        return section_html

    updated = SECTION_RE.sub(rewrite_section, updated)
    return updated


def clean_page(path: Path) -> bool:
    original = path.read_text()
    page_title_match = re.search(r"<h1>(?P<title>.*?)</h1>", original, re.DOTALL)
    page_title = strip_tags(page_title_match.group("title")) if page_title_match else path.parent.name
    updated = clean_html(original, page_title)
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
