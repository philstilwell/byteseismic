#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

from current_batch_editorial_profiles import CURRENT_BATCH_SPECIAL_PAGE_PROFILES

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
    render_dialogue_card,
    render_list_section,
    render_paragraphs,
    short_prompt_key,
    synthetic_prompt_dialogue_turns,
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
    "Create a hypothetical debate between two expert on emergence who have contrasting opinions on the concept.": "Create a hypothetical debate between two experts on emergence who have contrasting opinions on the concept.",
    "central test case and the central test case": "central test case and the neighboring case",
    "In the page's own terms, A good route is": "In the page's own terms, a good route is",
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
    "Game Theory names the central pressure.": "What Game Theory studies, and why strategy matters",
    "Bayes Theorem names the central pressure.": "What Bayes Theorem clarifies about updating belief",
    "Putting The issue under pressure": "Where the real issue has to be tested",
    "Putting Reason for Initial Omission under pressure": "Why the initial omission matters",
    "Putting Differentiating Actual Evil from Mere Emotional Responses under pressure": "Why actual evil must be separated from emotional reaction",
    "What Instantiate the variables with clear terms in each example clarifies, and where its limits show": "What Bayes Theorem looks like in worked examples",
    "What Facilitates Dialogue Between Different Worldviews clarifies, and where its limits show": "How faith can shape dialogue across worldviews",
    "What Generated educational graphics simply based on text or audio content really means in practice": "What text-to-graphic tools change for teaching",
    "What Step method of teasing out actual causation from a correlation really means in practice": "A step-by-step way to test whether correlation is causal",
    "What Research questions and hypotheses and provide helpful examples clarifies, and where its limits show": "How research questions and hypotheses guide a study",
    "What Critique of the Author’s Thesis in the “Deeper Thinking Podcast” really means in practice": "How the main critique of the podcast thesis should be tested",
    "What Correlation Between Childhood Trauma/Deprivation and Neurodiversity really means in practice": "How trauma correlations can be confused with neurodiversity itself",
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
    re.compile(r"^A reasonable objection is that economic life is too messy for neat answers here\..+", re.IGNORECASE),
    re.compile(r"^The payoff (?:here|of .+) is .+", re.IGNORECASE),
    re.compile(r"^The section should clarify how .+", re.IGNORECASE),
    re.compile(r"^Put the distinction under pressure\..+", re.IGNORECASE),
    re.compile(r"^Keep .+ in the same frame\.", re.IGNORECASE),
    re.compile(
        r"^Keep .+ in the same frame\. That is what shows what the page is claiming, where it gets tested, and what would have to change if the claim is right\.$",
        re.IGNORECASE,
    ),
    re.compile(r"^Keep .+ distinct from .+\.", re.IGNORECASE),
    re.compile(
        r"^Keep .+ distinct from .+\. They are not interchangeable bits of vocabulary; they point the reader toward different judgments, objections, or next steps\.$",
        re.IGNORECASE,
    ),
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

REMOVE_LIST_ITEM_PATTERNS = [
    re.compile(r"^Leave the reader with a sharper question about .+\.$", re.IGNORECASE),
    re.compile(r"^Notice what changes if .+$", re.IGNORECASE),
    re.compile(r"^Ask which incentive changes, who pays, and what tradeoff becomes easier to ignore when the framing gets too abstract\.$", re.IGNORECASE),
    re.compile(r"^Track the movement in the exchange: .+$", re.IGNORECASE),
    re.compile(r"^Watch how the section calibrates confidence .+$", re.IGNORECASE),
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

COLLECTIVE_SOURCE_DOSSIERS = {
    "Empiricists": {
        "source_intro": "This dossier keeps Empiricism tied to the early modern fight over where knowledge begins, how far experience can carry explanation, and why later thinkers keep returning to that pressure.",
        "source_cards": {
            "Original framing": "An editorial orientation page designed to make Empiricism teachable as a living method rather than a parade of names.",
            "Preserved texture": "The page preserves empiricism as a habit of testing claims against experience, then asking how much structure the mind contributes in the process.",
            "Historical setting": "Early modern philosophy, especially the British empiricist struggle over sensation, reflection, causation, and the limits of innate ideas.",
            "Primary texts nearby": "Locke's An Essay Concerning Human Understanding, Berkeley's Three Dialogues, and Hume's Treatise and Enquiry.",
            "Ideas in view": "Experience, ideas, causation, induction, the self, and the challenge to rationalist confidence.",
            "Influence trail": "Modern epistemology, philosophy of science, psychology of belief, pragmatism, and later naturalist critiques of a priori certainty.",
        },
    },
    "Phenomenologists": {
        "source_intro": "This dossier keeps Phenomenology anchored in the attempt to describe experience before theory, reduction, or scientific abstraction flatten what first appears.",
        "source_cards": {
            "Original framing": "An editorial orientation page designed to make Phenomenology teachable as a disciplined method of description rather than a vague mood.",
            "Preserved texture": "The page preserves phenomenology as a return to lived experience, intentionality, embodiment, and the structures that make a world show up for consciousness at all.",
            "Historical setting": "Late nineteenth- and twentieth-century European philosophy, where experience, intentionality, and embodiment become central after the limits of psychologism and abstract system-building.",
            "Primary texts nearby": "Husserl's Ideas, Heidegger's Being and Time, Merleau-Ponty's Phenomenology of Perception, and Beauvoir's phenomenological ethics.",
            "Ideas in view": "Intentionality, lived experience, epoché, embodiment, worldhood, and the difference between description and explanation.",
            "Influence trail": "Existentialism, hermeneutics, cognitive science, psychiatry, theology, literary theory, and debates about first-person method.",
        },
    },
    "Analytic Philosophers": {
        "source_intro": "This dossier keeps Analytic philosophy tied to its strongest aspiration: clearer arguments, sharper distinctions, and fewer conceptual fog machines masquerading as depth.",
        "source_cards": {
            "Original framing": "An editorial orientation page designed to make Analytic philosophy teachable as a style of inquiry rather than a geography label.",
            "Preserved texture": "The page preserves analytic philosophy as a commitment to argumentative clarity, explicit premises, and patient conceptual repair under objection.",
            "Historical setting": "Twentieth-century philosophy shaped by logic, language, science, and the wish to replace grand system-building with tighter analysis.",
            "Primary texts nearby": "Frege's essays, Russell's classic papers, Wittgenstein's Tractatus and Investigations, and later work by Quine, Kripke, Lewis, and Parfit.",
            "Ideas in view": "Logical analysis, language, reference, mind, knowledge, modality, and the standards arguments must meet to count as clear.",
            "Influence trail": "Philosophy of language, mind, logic, epistemology, decision theory, ethics, formal semantics, and ties to cognitive science.",
        },
    },
    "Ancient Philosophers": {
        "source_intro": "This dossier keeps ancient philosophy visible as more than origin story: it is where ethics, metaphysics, rhetoric, politics, and inquiry were first forced into durable argumentative form.",
        "source_cards": {
            "Original framing": "An editorial orientation page designed to make ancient philosophy teachable as a field of live disputes rather than a marble hall of founders.",
            "Preserved texture": "The page preserves ancient philosophy as argument joined to character, civic life, cosmology, and the question of how one ought to live.",
            "Historical setting": "Greek and Hellenistic philosophy, where public argument, metaphysical speculation, and ethical practice develop together.",
            "Primary texts nearby": "Plato's dialogues, Aristotle's major works, Epicurean letters, Stoic fragments, and later Roman mediations such as Cicero and Marcus Aurelius.",
            "Ideas in view": "Virtue, the good life, form and substance, causation, skepticism, rhetoric, and philosophy as a way of living.",
            "Influence trail": "Virtue ethics, logic, metaphysics, political theory, natural law, religious thought, and later revivals of practical philosophy.",
        },
    },
}

SPECIAL_PAGE_PROFILES = {
    "Phenomenologists": {
        "source_heading": "Read Phenomenology as a discipline of description, not a misty atmosphere.",
        "source_intro": "This dossier keeps Phenomenology tied to the stubborn idea that experience has a structure worth describing before theory, reduction, or explanation flatten it into something easier but less faithful.",
        "source_cards": {
            "Original framing": "A branch page that introduces Phenomenology as a method for describing lived experience rather than as a badge for vaguely introspective writing.",
            "Preserved texture": "The page preserves phenomenology as a return to intentionality, embodiment, worldhood, and the first-person structures that make things show up meaningfully at all.",
            "Historical setting": "Late nineteenth- and twentieth-century European philosophy, where psychologism, scientific reduction, and inherited metaphysics all pressed thinkers to ask what experience is like before it is translated into theory.",
            "Primary texts nearby": "Husserl's Ideas, Heidegger's Being and Time, Merleau-Ponty's Phenomenology of Perception, and Beauvoir's phenomenological ethics.",
            "Ideas in view": "Intentionality, epoché, embodiment, lived experience, worldhood, and the difference between description and explanation.",
            "Influence trail": "Existentialism, hermeneutics, psychiatry, theology, literary theory, cognitive science, and later debates about consciousness and first-person method.",
        },
        "source_read": "Read the page with one discipline in mind: phenomenology earns its keep only when it helps the reader notice structures of experience that outside-looking descriptions tend to miss or erase.",
        "sections": {
            "prompt-1": {
                "heading": "What Phenomenology is really trying to do",
                "paragraphs": [
                    "Phenomenology begins from a simple but demanding thought: before we explain experience, measure it, or translate it into theory, we should first describe how the world actually appears in lived consciousness. That means asking how objects show up as meaningful, how attention is directed, and how the subject is always already involved in a world rather than floating outside it.",
                    "Its signature claim is intentionality. Consciousness is not a sealed box full of private pictures; it is always consciousness of something. Perceiving a tree, fearing an exam, remembering a friend, or handling a tool all reveal a mind directed outward, bound up with situations, purposes, expectations, and bodily orientation.",
                    "That is why phenomenology resists premature reduction. A neuroscientific explanation, causal story, or behavioral summary may be useful, but it does not automatically capture what the experience is like as lived. Phenomenology does not deny explanation; it insists that description has its own philosophical work to do before explanation starts claiming completeness.",
                    "The tradition is strongest when it stays disciplined. Husserl emphasizes rigorous description, Heidegger turns toward worldhood and Being, Merleau-Ponty restores embodiment, and Beauvoir shows how lived situation is gendered and social. The unity lies in the method's pressure, not in a single doctrinal formula."
                ],
                "items": [
                    "Core move: describe experience as lived before reducing it to an outside theory.",
                    "Central clue: consciousness is intentional, meaning it is directed toward a world.",
                    "Main resistance: explanation can be powerful without exhausting what experience is like from the inside.",
                    "Best first test: can the page show why embodiment and worldhood matter without sliding into mystification?"
                ],
            },
            "prompt-2": {
                "heading": "How Phenomenology reshaped later philosophy",
                "paragraphs": [
                    "Its first lasting contribution was to make lived experience a serious philosophical starting point rather than a dispensable preface to theory. That move influenced existentialism, hermeneutics, psychiatry, theology, literary studies, and later philosophy of mind.",
                    "Phenomenology also sharpened the distinction between description and explanation. A person using a hammer, grieving a death, or navigating a room is not first encountering neutral data and then adding meaning afterward. Meaning is already there in the experience, and that insight changed how later thinkers approached perception, embodiment, and practical action.",
                    "A further contribution was methodological. The reduction or epoché, whatever one finally thinks of it, trained philosophers to suspend habitual assumptions long enough to ask what structures must be present for a world to appear as familiar, threatening, usable, sacred, or strange.",
                    "Its downstream influence remains strong because many later fields discovered that third-person accounts alone were missing something essential. Phenomenology gave them a way to talk about first-person structure without collapsing into mere autobiography."
                ],
                "items": [
                    "Lived experience: experience becomes a legitimate starting point for rigorous inquiry.",
                    "Embodiment and worldhood: perception and action are situated, not detached data-processing events.",
                    "Methodological suspension: bracketing assumptions can reveal what ordinary explanation overlooks.",
                    "Influence trail: existentialism, hermeneutics, psychiatry, theology, and philosophy of mind all inherit parts of the method."
                ],
            },
            "prompt-3": {
                "heading": "The figures who gave Phenomenology its durable shape",
                "paragraphs": [
                    "Husserl belongs at the center because he made phenomenology a rigorous program. He argued that philosophy should return to the things themselves by examining how objects are given in consciousness rather than treating them only as results of scientific theory or psychological process.",
                    "Heidegger then transformed the project by insisting that human existence is not best understood as a spectator's consciousness, but as being-in-the-world. That shift made practical involvement, mood, finitude, and worldhood central rather than peripheral.",
                    "Merleau-Ponty deepened the embodied side of the tradition. Perception is not a ghost inspecting a machine; it is a body already navigating space, habit, ambiguity, and motor possibility. Beauvoir extended phenomenology into ethics and social existence by showing how lived experience is structured by gender, dependence, and asymmetrical power.",
                    "Those figures matter together because they show how the method branches. Husserl gives rigor, Heidegger reorients ontology, Merleau-Ponty restores the body, and Beauvoir proves that phenomenology can illuminate oppression and situated freedom rather than only abstract consciousness."
                ],
                "items": [
                    "Husserl for intentionality, description, and phenomenological rigor.",
                    "Heidegger for being-in-the-world, finitude, and the structure of practical existence.",
                    "Merleau-Ponty for embodiment, perception, and the lived body.",
                    "Beauvoir for social situation, ambiguity, and phenomenology's ethical reach."
                ],
            },
            "prompt-4": {
                "heading": "A dialogue that shows how a phenomenologist thinks in practice",
                "paragraphs": [
                    "A good beginner's dialogue should start with an everyday act, not a grand abstraction. Let the student reach for a mug, walk through a doorway, or recognize a friend's face in a crowd. The phenomenologist's first move is to slow the event down and ask how the meaning of the situation is already present before a theory about it is supplied.",
                    "The student should voice the natural objection: 'Isn't this just introspection?' That matters because phenomenology is not trying to record random private feelings. It is looking for stable structures in how the world becomes available to experience in the first place.",
                    "The exchange becomes useful when embodiment enters the picture. The student notices that the hand already knows how to grip the mug, that the room is navigated through habit, and that attention shifts according to relevance rather than by scanning neutral pixels. Suddenly the world looks less like raw data and more like a field of meaningful affordances.",
                    "End with a concession and a gain. Phenomenology can become obscure when it forgets public discipline, but it becomes illuminating when it teaches the reader to notice what detached explanations presuppose. The student should leave able to say why lived experience deserves description before reduction."
                ],
                "items": [
                    "Begin with an ordinary act so the method looks disciplined rather than theatrical.",
                    "Let the student raise the introspection worry and answer it directly.",
                    "Use embodiment to show that the body is an active orientation to the world, not a passive container.",
                    "Close by naming both the insight and the risk: richer description on one side, obscurity on the other."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "Phenomenology matters because it insists that experience has describable structure before outside explanation claims the whole field.",
                "Its major figures keep revising that insight, but they agree that worldhood, embodiment, and intentionality cannot be treated as decorative extras.",
                "The page succeeds when the reader can explain why first-person description is not a retreat from rigor, but one of the conditions for getting the phenomenon into view at all."
            ],
            "items": [
                "What part of the lived experience would a purely third-person account miss?",
                "How does intentionality change the picture of mind as a private inner theater?",
                "Where does embodiment become philosophically unavoidable?",
                "What keeps phenomenological description from collapsing into impressionism?"
            ],
        },
    },
    "Continental Philosophers": {
        "source_heading": "Read Continental philosophy as a family of disputes, not a creed.",
        "source_intro": "This dossier keeps the page from collapsing a sprawling tradition into one slogan. The point is to track the recurring pressures that make continental philosophy recognizable even when its major figures disagree sharply.",
        "source_cards": {
            "Original framing": "A branch page that introduces a tradition by way of its fractures, methods, and recurring questions rather than by a loose geography label.",
            "Preserved texture": "The page preserves the habit of turning from abstract system-building toward history, embodiment, interpretation, power, and the instability of supposedly neutral standpoints.",
            "Historical setting": "Nineteenth- and twentieth-century European philosophy, especially after Kant and Hegel, when questions of history, experience, alienation, language, and social critique became impossible to treat as side issues.",
            "Primary texts nearby": "Hegel's Phenomenology of Spirit, Nietzsche's Genealogy of Morals, Husserl's Ideas, Heidegger's Being and Time, Beauvoir's The Ethics of Ambiguity, and Derrida's Of Grammatology.",
            "Ideas in view": "Historicity, lived experience, interpretation, power, critique of neutrality, and suspicion toward the fantasy of a view from nowhere.",
            "Influence trail": "Phenomenology, existentialism, hermeneutics, structuralism, post-structuralism, psychoanalytic theory, cultural criticism, and political critique.",
        },
        "source_read": "Read the page with two warnings in view. First, 'continental' is an administrative umbrella, not a unified doctrine. Second, the tradition earns its place only when the reader can see why embodiment, history, language, and domination keep re-entering the argument.",
        "sections": {
            "prompt-1": {
                "heading": "What Continental philosophy is really trying to do",
                "paragraphs": [
                    "Continental philosophy is less a single doctrine than a recurring refusal to treat human beings as detached spectators of the world. Its central pressure is that consciousness is embodied, historically situated, linguistically mediated, and entangled with institutions of power long before it becomes a neat object of analysis.",
                    "That is why the tradition keeps returning to thinkers as different as Hegel, Nietzsche, Husserl, Heidegger, Beauvoir, Foucault, and Derrida. They do not agree on fundamentals, but they share a suspicion that reality is distorted when philosophy imagines reason as timeless, context-free, and insulated from social life.",
                    "A useful first contrast is with a style of philosophy that starts by clarifying propositions and arguments one by one. Continental philosophy usually starts elsewhere: with lived experience, historical development, interpretation, alienation, finitude, or domination. It is not anti-argument; it is trying to show what arguments forget when they treat those pressures as optional scenery.",
                    "The tradition becomes clearest when the reader sees both its unity and its fractures. Husserl wants a rigorous description of experience; Nietzsche wants genealogical suspicion; Sartre dramatizes freedom; Adorno and Foucault track domination by different routes. The family resemblance is real, but it lives in recurrent problems, not in one party line."
                ],
                "items": [
                    "Shared pressure: human thought is always already shaped by history, embodiment, language, and institutions.",
                    "First major fracture: phenomenological description and existential analysis differ from genealogical and deconstructive suspicion.",
                    "Why it matters: the tradition keeps asking what gets hidden when philosophy speaks as if context were disposable.",
                    "Best first test: can the page explain why neutrality, objectivity, or rationality become contested without collapsing into simple relativism?"
                ],
            },
            "prompt-2": {
                "heading": "How Continental philosophy reshaped later thought",
                "paragraphs": [
                    "Its first major contribution was to insist that experience has structure before it is turned into theory. Phenomenology taught later philosophy to ask how things appear in lived consciousness, which in turn affected psychology, cognitive science, aesthetics, theology, and literary theory.",
                    "A second contribution was historical suspicion. Nietzsche, Marx, Freud, Foucault, and the critical theorists all help build the habit of asking not only whether a claim is true, but whose interests it serves, what history made it plausible, and what forms of domination hide inside apparently neutral categories.",
                    "The tradition also transformed the study of language and interpretation. Hermeneutics and deconstruction showed that meaning is not a sealed object waiting to be extracted by a neutral reader. Context, tradition, rhetorical framing, and unstated hierarchies all affect what a text can say and what a reader can responsibly infer.",
                    "Its political contribution is equally durable. Continental traditions made alienation, ideology, gendered embodiment, colonial power, and disciplinary institutions central philosophical topics rather than peripheral moral commentary."
                ],
                "items": [
                    "Phenomenology: a disciplined account of lived experience before it is translated into theory.",
                    "Genealogy and critique: a method for exposing how values and institutions are historically made rather than naturally given.",
                    "Hermeneutics and deconstruction: a deeper account of interpretation, ambiguity, and the instability of clean oppositions.",
                    "Political and cultural critique: a way to connect philosophy with domination, identity, institutions, and public life."
                ],
            },
            "prompt-3": {
                "heading": "The figures who gave Continental philosophy its durable shape",
                "paragraphs": [
                    "Hegel belongs on any serious list because he made history itself philosophically constitutive. He teaches later thinkers to see consciousness, recognition, and social life as developing through conflict rather than appearing fully formed.",
                    "Nietzsche matters because he turned critique into genealogy. He asks what moral vocabularies are for, who benefits from them, and what forms of resentment, strength, or decadence they conceal.",
                    "Husserl and Heidegger reshape the tradition from another direction. Husserl wants rigorous description of experience; Heidegger turns that project toward being, worldhood, finitude, and the question of how meaning is possible for a situated being at all.",
                    "From there the line branches widely: Beauvoir links existence to gendered embodiment; Sartre dramatizes freedom and bad faith; Adorno and Horkheimer critique instrumental reason and the culture industry; Foucault studies power through institutions and discourse; Derrida pressures inherited binaries; Habermas tries to rescue critique through communicative reason."
                ],
                "items": [
                    "Hegel for history and recognition.",
                    "Nietzsche for genealogy and suspicion.",
                    "Husserl and Heidegger for phenomenology, worldhood, and the structure of experience.",
                    "Beauvoir, Sartre, Adorno, Foucault, Derrida, and Habermas for the tradition's later existential, political, and linguistic turns."
                ],
            },
            "prompt-4": {
                "heading": "A dialogue that shows how a Continental philosopher teaches",
                "paragraphs": [
                    "A good beginner's dialogue starts with an apparently ordinary claim such as 'facts speak for themselves.' The continental philosopher does not answer by denying facts, but by asking who framed the situation, which categories are doing the filtering, and what history made those categories look natural.",
                    "The first-year student should push back in a recognizable way: 'Isn't that just overcomplicating things?' That question matters because it lets the teacher distinguish between needless obscurity and the harder claim that human beings never reason from nowhere.",
                    "The exchange becomes pedagogically useful when one concrete example enters the scene: a law, a medical diagnosis, a social role, or a literary text. Once the case is live, the philosopher can show how experience, language, and power shape what even counts as the obvious description.",
                    "End the dialogue with a disciplined concession. Continental philosophy is strongest when it expands what the reader notices; it is weakest when suspicion becomes a reflex that dissolves all standards. The student should leave with a sharper question, not with a permission slip for fog."
                ],
                "items": [
                    "Begin with a claim that sounds neutral, then ask what historical and social work that neutrality is doing.",
                    "Let the student voice the fear of obscurity or relativism so the page can answer it directly.",
                    "Force one example through the exchange; otherwise the method stays theatrical instead of explanatory.",
                    "Close by naming both the gain and the risk: richer diagnosis on one side, performative suspicion on the other."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "The thread running through the page is that continental philosophy asks what our theories forget about lived, historical, and political existence.",
                "The tradition stays alive because its figures disagree in illuminating ways about how to recover that forgotten depth.",
                "A reader who finishes the page should be able to say why this tradition is more than a geography label and why its best question is often, 'What did your clean abstraction have to leave out to become clean?'"
            ],
            "items": [
                "What pressure on neutrality or objectivity seems most central here?",
                "Which figure on the page offers the most useful entry point for your current question?",
                "Where does the tradition genuinely clarify experience, and where does it risk theatrical vagueness?",
                "What later fields still borrow continental methods even when they reject continental vocabulary?",
                "Which internal fracture matters most: phenomenology versus genealogy, critique versus reconstruction, or language versus embodiment?"
            ],
        },
    },
    "Critical Theorists": {
        "source_heading": "Read Critical Theory as diagnosis under pressure.",
        "source_intro": "This dossier treats Critical Theory as a tradition with a recognizable problem: how domination hides inside ordinary institutions, habits, and ideals that present themselves as rational or natural.",
        "source_cards": {
            "Original framing": "A branch page organized around Frankfurt School pressures, later revisions, and the public stakes of critique rather than around slogan-level invocations of social justice.",
            "Preserved texture": "The page preserves the tradition's habit of moving between economics, culture, psychology, and politics in order to show how power reproduces itself without always relying on open coercion.",
            "Historical setting": "Early- to mid-twentieth-century Europe, marked by capitalism, fascism, mass media, bureaucratic administration, and the collapse of confidence that Enlightenment reason naturally leads to emancipation.",
            "Primary texts nearby": "Horkheimer's Traditional and Critical Theory, Adorno and Horkheimer's Dialectic of Enlightenment, Marcuse's One-Dimensional Man, Benjamin's Work of Art essay, and Habermas's Theory of Communicative Action.",
            "Ideas in view": "Ideology critique, instrumental reason, emancipation, reification, culture industry, public sphere, and communicative rationality.",
            "Influence trail": "Cultural criticism, democratic theory, critical pedagogy, media studies, race and gender critique, and later debates about ideology, discourse, and social reproduction.",
        },
        "source_read": "The page should be read with one practical question in mind: how do apparently reasonable systems teach people to adapt to domination and even misrecognize it as freedom, efficiency, or common sense?",
        "sections": {
            "prompt-1": {
                "heading": "What Critical Theory is really trying to do",
                "paragraphs": [
                    "Critical Theory begins from the thought that philosophy should not merely interpret society from a safe balcony. It should diagnose how domination is organized, reproduced, and disguised inside economies, institutions, media, and habits of thought.",
                    "That is why the tradition is not reducible to partisan denunciation. Its sharper claim is that reason itself can be bent into an instrument of control when efficiency, administration, and social adaptation become higher priorities than truth, freedom, and human flourishing.",
                    "The Frankfurt School gives the tradition its original shape, but the tradition quickly becomes internally divided. Adorno is suspicious of tidy reconciliation; Marcuse emphasizes one-dimensional conformity; Benjamin tracks art, technology, and reproducibility; Habermas later tries to recover a norm of public reason that earlier critical theory often treated with distrust.",
                    "A good summary should therefore sound less like a moral slogan and more like a method: trace the institution, expose the ideology, ask who benefits, and then show which forms of experience or speech have been narrowed in the process."
                ],
                "items": [
                    "Core pressure: domination often survives by presenting itself as normal, rational, or inevitable.",
                    "Method: move across economics, culture, psychology, and politics instead of treating each as a sealed silo.",
                    "Internal split: negative dialectics and suspicion on one side, communicative reconstruction on the other.",
                    "Best test: can the page show how critique differs from mere denunciation?"
                ],
            },
            "prompt-2": {
                "heading": "How Critical Theory reshaped later philosophy",
                "paragraphs": [
                    "Its most famous contribution is ideology critique. Critical theorists taught later readers to ask how cultural forms, media systems, and institutional vocabularies can make contingent arrangements feel natural, necessary, or deserved.",
                    "A second contribution is the critique of instrumental reason. Adorno and Horkheimer argue that a civilization obsessed with control and calculation can become highly rationalized while also becoming morally desensitized. That warning remains potent in debates about technocracy, bureaucracy, data governance, and algorithmic management.",
                    "The tradition also widened the field of philosophy by refusing to segregate aesthetics, politics, and social theory. Benjamin on reproducible art, Marcuse on desire and repression, and Habermas on the public sphere all show that culture is not ornament; it is one of the places where domination and resistance become visible.",
                    "Finally, Critical Theory helped normalize the thought that emancipation is not merely personal. Liberation depends on institutions, discourse, education, and forms of collective life capable of resisting normalization."
                ],
                "items": [
                    "Ideology critique: exposing how domination hides inside common sense.",
                    "Critique of instrumental reason: showing how efficiency can hollow out ethical life.",
                    "Cultural and aesthetic criticism: treating art and media as politically serious sites of struggle.",
                    "Democratic reconstruction: asking what institutions and public discourse would be needed for less distorted social life."
                ],
            },
            "prompt-3": {
                "heading": "The figures who gave Critical Theory its durable shape",
                "paragraphs": [
                    "Max Horkheimer matters because he defines the difference between traditional theory, which describes the world, and critical theory, which reflects on the knower's place inside the world being criticized.",
                    "Theodor Adorno is central because he turns critique into a relentless sensitivity to domination, standardization, and conceptual violence. He is one of the tradition's hardest voices to read, but also one of its clearest warnings against reconciliation that arrives too cheaply.",
                    "Walter Benjamin and Herbert Marcuse widen the field in different directions. Benjamin shows how technology changes perception and the political role of art; Marcuse asks how affluent societies produce compliance by shaping needs, pleasures, and imagination.",
                    "Jürgen Habermas becomes decisive because he refuses to let critique end in despair. By recovering communicative action, deliberation, and the public sphere, he asks whether rational criticism can survive without repeating the domination earlier critical theorists exposed."
                ],
                "items": [
                    "Horkheimer for the basic idea of critique.",
                    "Adorno for domination, culture industry, and negative dialectics.",
                    "Benjamin and Marcuse for media, technology, desire, and one-dimensional conformity.",
                    "Habermas for the reconstructive turn toward communication and democratic legitimacy."
                ],
            },
            "prompt-4": {
                "heading": "A dialogue that shows how Critical Theory teaches",
                "paragraphs": [
                    "A good classroom dialogue opens with a student's commonsense claim such as 'the market just gives people what they want.' The critical theorist should not answer with instant scorn. The first move is to ask how desires are shaped, who benefits from calling them spontaneous, and which institutions train people to mistake adaptation for freedom.",
                    "The student then needs a fair rejoinder: 'Are you saying people never choose anything for themselves?' That pressure matters because Critical Theory is weakest when it makes agency disappear and strongest when it shows how agency is patterned, narrowed, and manipulated rather than erased.",
                    "The exchange becomes valuable when a concrete case enters the room: advertising, university rankings, social media feeds, workplace surveillance, or public debate under mass media conditions. The theory should clarify the case rather than hover above it like moral fog.",
                    "The dialogue should close by distinguishing critique from cynicism. Critical Theory is not saying every institution is fake and every value corrupted beyond repair. It is asking what forms of communication, education, and solidarity would make less distorted life possible."
                ],
                "items": [
                    "Begin with a normalized institution, not an obviously villainous one.",
                    "Let the student raise the agency objection so the page can answer it honestly.",
                    "Use a case from media, work, education, or politics to keep critique concrete.",
                    "End with reconstruction as well as diagnosis; otherwise the theory reads as pure negation."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "Critical Theory is best read as a method for asking how domination gets misrecognized as normality.",
                "Its internal drama runs from suspicion of administered life to the hope that less distorted public reason is still possible.",
                "A serious reader should finish the page able to tell the difference between ideological critique, cultural pessimism, and democratic reconstruction."
            ],
            "items": [
                "Where in ordinary life does domination most successfully present itself as common sense?",
                "Which figure here best explains media and culture, and which best explains institutions and discourse?",
                "What is the strongest objection to Critical Theory's suspicion of neutrality?",
                "How does Habermas both inherit and challenge earlier Frankfurt School themes?",
                "What would count as emancipation on this page beyond individual self-expression?"
            ],
        },
    },
    "Existentialists": {
        "source_heading": "Read existentialism where freedom meets finitude.",
        "source_intro": "This dossier frames existentialism around a durable pressure: human beings must choose, answer, and make meaning without the comfort of a guaranteed script.",
        "source_cards": {
            "Original framing": "A branch page that introduces existentialism as a live confrontation with freedom, anxiety, embodiment, and responsibility instead of a mood of stylish despair.",
            "Preserved texture": "The page preserves the tradition's habit of treating the self as a task rather than a fixed essence and of forcing abstractions about meaning back into lived decisions.",
            "Historical setting": "Nineteenth- and twentieth-century crises of religion, morality, war, alienation, and modern bureaucracy, with earlier roots in Kierkegaard and later explosions in Sartre, Beauvoir, Camus, and Heidegger.",
            "Primary texts nearby": "Kierkegaard's Fear and Trembling, Nietzsche's Thus Spoke Zarathustra, Heidegger's Being and Time, Sartre's Existentialism Is a Humanism, Beauvoir's Ethics of Ambiguity, and Camus's Myth of Sisyphus.",
            "Ideas in view": "Freedom, responsibility, authenticity, bad faith, absurdity, finitude, embodiment, and the refusal of ready-made essence.",
            "Influence trail": "Phenomenology, theology, literature, psychology, feminist theory, political resistance, and modern debates about authenticity and self-creation.",
        },
        "source_read": "The key to reading the page is to ask what existentialism does with the unease that appears when no inherited role can fully answer for your life.",
        "sections": {
            "prompt-1": {
                "heading": "What existentialism is really trying to do",
                "paragraphs": [
                    "Existentialism begins from the thought that a human life is not simply found like a finished object. It has to be inhabited, chosen, interpreted, and answered for under conditions of uncertainty, mortality, and social pressure.",
                    "That makes the tradition easy to caricature. It is not just saying that life feels anxious or absurd. It is asking what freedom means when there is no final script to hide behind and when excuses such as custom, authority, or historical inevitability no longer feel intellectually honest.",
                    "The tradition is internally divided from the start. Kierkegaard turns existential pressure toward faith and inward seriousness. Nietzsche pushes toward self-overcoming and suspicion of herd morality. Heidegger analyzes being-in-the-world and finitude. Sartre radicalizes freedom, while Beauvoir insists that freedom is always entangled with other embodied lives and social structures.",
                    "A good description therefore balances pathos and discipline. Existentialism is not mere confession. It is a philosophical effort to describe what it is like to become answerable for oneself in a world that refuses to hand out certainty."
                ],
                "items": [
                    "Core pressure: the self is a task, not a prefabricated essence.",
                    "First major fracture: religious inwardness, heroic self-creation, phenomenological ontology, and political ethics do not pull in the same direction.",
                    "Why it matters: existentialism makes freedom, responsibility, and bad faith feel concrete instead of ornamental.",
                    "Best first test: can the page show why anxiety is philosophically revealing rather than merely psychological?"
                ],
            },
            "prompt-2": {
                "heading": "How existentialism reshaped later thought",
                "paragraphs": [
                    "Its first contribution was to make lived agency philosophically central. Existentialists forced later ethics and political theory to take seriously the experience of choosing under ambiguity instead of pretending that moral life is solved by rule-application alone.",
                    "A second contribution was the analysis of bad faith and self-deception. Sartre and Beauvoir show that people hide from freedom by pretending they are only roles, functions, or products of circumstances, even while depending on their own agency to sustain the performance.",
                    "Existentialism also changed the philosophical understanding of finitude. Death, contingency, vulnerability, and absurdity stop being edge cases and become features of any honest account of human life.",
                    "Its literary and political influence is equally important. The tradition made philosophical prose more dramatic, porous, and worldly, while also shaping conversations about oppression, resistance, authenticity, and solidarity."
                ],
                "items": [
                    "Freedom under ambiguity: moral life as decision without perfect guarantees.",
                    "Bad faith: a sharper vocabulary for self-deception and role-hiding.",
                    "Finitude and absurdity: mortality and contingency treated as philosophically central.",
                    "Embodied and political existence: existential categories carried into feminism, literature, and resistance."
                ],
            },
            "prompt-3": {
                "heading": "The figures who gave existentialism its durable shape",
                "paragraphs": [
                    "Kierkegaard belongs on the page because he turns existence into inward decision. He cares less about detached theory than about what it means to stand before a demand that cannot be outsourced to the crowd.",
                    "Nietzsche matters because he transforms the problem from guilt and faith into value-creation, self-overcoming, and suspicion of inherited morality. He gives existentialism its ferocious anti-complacency.",
                    "Heidegger and Sartre then reshape the tradition in opposed but connected ways. Heidegger analyzes thrownness, care, and being-toward-death; Sartre emphasizes radical freedom, the look of the other, and bad faith. Beauvoir is indispensable because she shows that freedom is always situated within gendered, social, and material conditions.",
                    "Camus deserves a place not because he solves absurdity, but because he dramatizes the refusal to lie about it. His voice keeps the tradition tied to lucid honesty rather than grand metaphysical rescue."
                ],
                "items": [
                    "Kierkegaard for inward decision and seriousness.",
                    "Nietzsche for self-overcoming and critique of herd morality.",
                    "Heidegger, Sartre, and Beauvoir for finitude, freedom, bad faith, and situated agency.",
                    "Camus for absurdity without surrender."
                ],
            },
            "prompt-4": {
                "heading": "A dialogue that shows how an existentialist teaches",
                "paragraphs": [
                    "A useful dialogue opens with the student saying, 'I do not really have a choice; my situation decides for me.' The existentialist should grant the weight of circumstance and then ask what is still being chosen in the way the situation is interpreted, inhabited, or evaded.",
                    "The student then needs a hard follow-up: 'Isn't this just blaming people for conditions they did not make?' That challenge matters because existentialism becomes cruel if it forgets social reality and becomes empty if it forgets freedom altogether.",
                    "The best exchange turns on one concrete case: staying in a deadening job, remaining silent in the face of injustice, performing a social role one no longer believes, or refusing intimacy under the cover of fatalism. The case reveals what bad faith looks like from street level.",
                    "End the dialogue with ambiguity intact. Existentialism should not promise that every right choice becomes obvious. It should show why honesty, courage, and responsibility become more urgent precisely when certainty does not arrive."
                ],
                "items": [
                    "Begin with the student's appeal to circumstance, duty, or inevitability.",
                    "Let the teacher separate limitation from excuse rather than denying real constraint.",
                    "Use one example where freedom and social pressure are both visible.",
                    "Close on lucid responsibility, not on melodrama or romantic self-invention."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "Existentialism ties together freedom, finitude, and the temptation to hide from both.",
                "Its best pages force readers to notice where they are outsourcing responsibility to roles, systems, or inherited scripts.",
                "The tradition is alive wherever the question remains: what does it mean to choose honestly when no final authority can remove the burden for you?"
            ],
            "items": [
                "Which figure here best captures freedom, and which best captures limitation?",
                "Where does existential honesty differ from self-dramatization?",
                "What concrete case most clearly reveals bad faith on this page?",
                "How does Beauvoir change the tradition's picture of situated freedom?",
                "What objection to existentialism still bites hardest: vagueness, voluntarism, or political thinness?"
            ],
        },
    },
    "Pragmatists": {
        "source_heading": "Read pragmatism as inquiry that has to work in the world.",
        "source_intro": "This dossier presents pragmatism as a tradition that keeps asking what beliefs do, how inquiry actually proceeds, and how ideas earn their keep in experience, experiment, and public life.",
        "source_cards": {
            "Original framing": "A branch page built around pragmatic method, fallibilism, and democratic inquiry rather than around the lazy slogan that pragmatists only care about whatever is convenient.",
            "Preserved texture": "The page preserves the habit of testing meanings and truths by consequences, practices, and inquiry rather than by treating concepts as detached ornaments.",
            "Historical setting": "Late nineteenth- and early twentieth-century American philosophy, shaped by science, Darwin, democracy, industrial modernity, and frustration with sterile metaphysical disputes.",
            "Primary texts nearby": "Peirce's Fixation of Belief, James's Pragmatism and The Will to Believe, and Dewey's Experience and Nature and Democracy and Education.",
            "Ideas in view": "Fallibilism, inquiry, habit, consequences, truth as warranted assertibility, pluralism, and democracy as an epistemic as well as political project.",
            "Influence trail": "Philosophy of science, education, democratic theory, legal realism, cognitive inquiry, and contemporary anti-foundationalism.",
        },
        "source_read": "Read the page with one corrective in mind: pragmatism is not a permission slip for opportunism. It is a disciplined demand that concepts prove their worth in inquiry and action.",
        "sections": {
            "prompt-1": {
                "heading": "What pragmatism is really trying to do",
                "paragraphs": [
                    "Pragmatism asks what difference a belief, concept, or distinction makes once it enters inquiry and life. If two positions sound different but never change what anyone should expect, test, do, or revise, the pragmatist suspects the dispute may be thinner than advertised.",
                    "That does not mean truth is whatever feels useful in the moment. The tradition is much tougher than that. Peirce ties inquiry to fallibilism and communal correction, James stresses lived significance and plural experience, and Dewey turns philosophy outward toward experimentation, education, and democratic problem-solving.",
                    "Pragmatism is therefore both anti-dogmatic and anti-skeptical. It rejects the fantasy of absolute foundations, but it also rejects the lazy move that says nothing can be better or worse because certainty is unavailable.",
                    "Its recurring claim is that intelligence grows inside practices of testing, revision, and consequence-tracking. Philosophy matters when it improves those practices instead of floating above them."
                ],
                "items": [
                    "Core pressure: meaning should cash out in differences to inquiry and conduct.",
                    "First major fracture: Peirce's logical rigor, James's pluralistic temperament, and Dewey's social experimentalism do not coincide perfectly.",
                    "Why it matters: pragmatism turns truth, belief, and method back toward lived inquiry.",
                    "Best first test: can the page distinguish disciplined usefulness from mere expediency?"
                ],
            },
            "prompt-2": {
                "heading": "How pragmatism reshaped later thought",
                "paragraphs": [
                    "Its first contribution is fallibilism with teeth. Pragmatists normalize the thought that belief should remain revisable without collapsing into paralysis. That posture has influenced philosophy of science, epistemology, and public reasoning.",
                    "A second contribution is the pragmatic maxim: to understand a concept, ask what practical and experiential differences it implies. This gave later thinkers a tool for clearing away pseudo-problems and reconnecting abstraction to inquiry.",
                    "The tradition also reshaped theories of truth and justification. James presses the human stakes of belief; Dewey links warranted assertion to inquiry; later pragmatists carry these themes into language, law, and democratic deliberation.",
                    "Pragmatism's political contribution matters as much as its epistemology. Dewey in particular treats democracy not only as a voting mechanism but as a way of organizing collective intelligence, education, and shared experimentation."
                ],
                "items": [
                    "Fallibilism: confidence without infallibility.",
                    "Pragmatic clarification: meanings tested by differences in expectation, action, and inquiry.",
                    "Truth and justification: beliefs assessed within practices of revision and public testing.",
                    "Democratic inquiry: social institutions treated as experiments answerable to consequences."
                ],
            },
            "prompt-3": {
                "heading": "The figures who gave pragmatism its durable shape",
                "paragraphs": [
                    "Charles Sanders Peirce is indispensable because he gives the tradition its logical backbone. He connects meaning to conceivable practical effects, treats inquiry as communal, and refuses to separate truth from disciplined investigation.",
                    "William James matters because he makes the tradition feel human. He cares about temperament, risk, lived experience, and the way abstract arguments touch actual lives without surrendering standards of seriousness.",
                    "John Dewey then broadens pragmatism into a philosophy of education, politics, and culture. He insists that inquiry is not a laboratory luxury; it is a habit a democratic society must cultivate if it wants intelligence rather than dogma to govern collective life.",
                    "Later voices such as Mead, Addams, Rorty, and Putnam matter too, but the Peirce-James-Dewey triad remains the clearest map of the tradition's logic, psychology, and civic ambition."
                ],
                "items": [
                    "Peirce for logical method and communal inquiry.",
                    "James for pluralism, temperament, and the lived stakes of belief.",
                    "Dewey for education, democracy, and social experimentalism.",
                    "Later pragmatists for extensions into language, law, and public reason."
                ],
            },
            "prompt-4": {
                "heading": "A dialogue that shows how a pragmatist teaches",
                "paragraphs": [
                    "A strong beginner's dialogue starts with a question like, 'But is it true in itself?' The pragmatist does not dodge the question. The first reply is: tell me what difference the belief makes to prediction, inquiry, conduct, or revision, because otherwise the question may still be too vague to answer responsibly.",
                    "The student should then object that this sounds anti-metaphysical or shallow. That is the right pressure point. The pragmatist has to show that demanding practical bearings is not trivializing a claim; it is asking what would count for or against it in experience and thought.",
                    "Bring in one concrete case such as prayer, free will, schooling, scientific disagreement, or public policy. The dialogue gets real when the student can see how a belief changes what should be tried, expected, or corrected.",
                    "End by clarifying the danger. Pragmatism can degenerate into short-term utility talk if it forgets inquiry, community, and long-run correction. Its real ideal is not convenience, but intelligent responsiveness to consequences."
                ],
                "items": [
                    "Begin with the student's demand for a truth detached from consequences.",
                    "Make the pragmatist ask what would count as a practical difference or evidential shift.",
                    "Use one case where consequences can be traced rather than merely asserted.",
                    "Close by distinguishing pragmatic method from opportunistic spin."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "Pragmatism ties meaning, truth, and action together through inquiry.",
                "Its major figures differ in tone and emphasis, but all resist the fantasy of thought cut loose from consequences.",
                "A reader should leave the page able to explain why pragmatism is neither soft relativism nor mere common-sense practicality."
            ],
            "items": [
                "What belief on the page becomes clearer once practical consequences are traced?",
                "How does pragmatism preserve standards while rejecting absolute certainty?",
                "Which figure here best captures the tradition's democratic ambitions?",
                "Where is the line between pragmatic clarification and crude utility?",
                "What live debate today most needs a pragmatist treatment?"
            ],
        },
    },
    "Rationalists": {
        "source_heading": "Read rationalism where reason claims explanatory priority.",
        "source_intro": "This dossier frames rationalism around one durable wager: some of the deepest structures of reality, knowledge, and necessity are grasped by reason more fundamentally than by sense experience alone.",
        "source_cards": {
            "Original framing": "A branch page organized around seventeenth-century rationalist ambitions and disputes rather than around the cartoon that rationalists simply disliked the senses.",
            "Preserved texture": "The page preserves the confidence that mathematics, deduction, and conceptual necessity can reveal truths that experience by itself cannot secure.",
            "Historical setting": "Early modern philosophy after the scientific revolution, when thinkers sought certainty, method, and a stable picture of mind, God, substance, and causation.",
            "Primary texts nearby": "Descartes's Meditations, Spinoza's Ethics, and Leibniz's Monadology and Discourse on Metaphysics.",
            "Ideas in view": "Innate ideas, clear and distinct perception, substance, necessity, sufficient reason, and the relation between reason and experience.",
            "Influence trail": "Modern epistemology, metaphysics, philosophy of mathematics, idealism, and later debates between rationalist and empiricist pictures of mind and knowledge.",
        },
        "source_read": "Read the page with one live question in mind: what kinds of truths would be inaccessible or unstable if philosophy had to rely on sensory experience alone?",
        "sections": {
            "prompt-1": {
                "heading": "What rationalism is really trying to do",
                "paragraphs": [
                    "Rationalism is the view that reason has a deeper role in knowledge than passive reception of sensory data. Its strongest forms hold that some truths about reality, self, mathematics, causation, or God are known a priori or made intelligible only through conceptual structure.",
                    "That does not mean rationalists deny experience. The sharper claim is that experience alone cannot generate necessity, universality, or explanatory depth. Something in the intellect has to organize, infer, or disclose what sensation by itself would leave fragmentary.",
                    "The tradition's classical figures share this ambition but pursue it differently. Descartes wants indubitable foundations and a secure method. Spinoza builds a severe metaphysical system from conceptual necessity. Leibniz multiplies subtle distinctions about possibility, sufficient reason, and the structure of the world.",
                    "A useful description keeps the attraction and the risk in view. Rationalism promises depth, necessity, and order; it also risks outrunning what can actually be justified once metaphysical confidence becomes too easy."
                ],
                "items": [
                    "Core pressure: experience alone seems too thin to explain necessity or universal structure.",
                    "First major fracture: foundational certainty, geometric system, and metaphysical pluralism are not the same rationalist strategy.",
                    "Why it matters: rationalism shapes what later philosophy means by reason, mind, and a priori knowledge.",
                    "Best first test: can the page explain why necessity is central to the rationalist imagination?"
                ],
            },
            "prompt-2": {
                "heading": "How rationalism reshaped later thought",
                "paragraphs": [
                    "Its first contribution is the modern a priori problem. Rationalists force later philosophers to ask whether mathematics, logic, and metaphysical structure can be reduced to experience or whether they depend on irreducible features of reason.",
                    "A second contribution is methodological ambition. Descartes, Spinoza, and Leibniz all raise the standard for what counts as an explanation by seeking clarity, deduction, and systematic unity rather than a pile of disconnected observations.",
                    "The tradition also leaves behind durable metaphysical tools: substance, modes, sufficient reason, and the demand that nothing be brute without necessity or intelligible ground.",
                    "Even philosophers who reject rationalism keep borrowing from it. Kant, idealism, analytic metaphysics, philosophy of mathematics, and debates over nativism all inherit questions rationalism sharpened."
                ],
                "items": [
                    "A priori knowledge: the problem of truths reason seems able to reach independently of observation.",
                    "Systematic explanation: philosophy as ordered understanding rather than mere reporting.",
                    "Metaphysical structure: substance, necessity, and sufficient reason as enduring tools and temptations.",
                    "Long afterlife: empiricism, Kantianism, and contemporary nativism all define themselves partly against rationalist pressure."
                ],
            },
            "prompt-3": {
                "heading": "The figures who gave rationalism its durable shape",
                "paragraphs": [
                    "Descartes anchors the tradition because he turns radical doubt into a search for certainty and gives rationalism its most famous appeal to clear and distinct ideas. He also sets the mind-body problem in a form later philosophy cannot ignore.",
                    "Spinoza matters because he pushes rationalism toward a breathtaking system. In his hands the world becomes intelligible through necessity, and freedom is re-described as understanding rather than indeterministic choice.",
                    "Leibniz completes the classical trio by combining logical subtlety with metaphysical exuberance. His principles of sufficient reason and identity of indiscernibles press the demand that reality be fully intelligible in concept.",
                    "The figures matter together because they show rationalism's range: secure foundations, geometric system, and pluralistic metaphysics are different expressions of one deeper trust in reason."
                ],
                "items": [
                    "Descartes for method, certainty, and dualism.",
                    "Spinoza for necessity, substance, and systematic metaphysics.",
                    "Leibniz for sufficient reason, possibility, and metaphysical analysis.",
                    "Their shared legacy: reason as a source of structure, not merely a tool for sorting experience."
                ],
            },
            "prompt-4": {
                "heading": "A dialogue that shows how a rationalist teaches",
                "paragraphs": [
                    "A strong dialogue opens with the student saying, 'If I did not observe it, how could I know it?' The rationalist's first move is to point toward cases like mathematics, logic, or modality, where observation seems insufficient to explain the necessity of what is known.",
                    "The student should then press the obvious objection: 'How do I know I am not just projecting ideas onto the world?' That is the right difficulty, because rationalism is at its best when it earns the bridge from thought to reality and at its worst when it assumes the bridge for free.",
                    "Bring the exchange down to one example such as causation, infinity, or personal identity. The page becomes useful when the reader sees why the rationalist thinks experience gives fragments while reason offers structure.",
                    "End the dialogue by letting empiricism answer back in outline. A rationalist page should teach not only confidence in reason, but also why later critics thought that confidence could become overreach."
                ],
                "items": [
                    "Begin with the student's demand for sensory evidence.",
                    "Use mathematics or modality to show why the rationalist thinks sensation is not enough.",
                    "Let the projection objection land so rationalism has to justify its ambition.",
                    "Close by naming the empiricist counterpressure that keeps the tradition honest."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "Rationalism ties together necessity, intelligibility, and trust in reason's reach.",
                "Its central debate is whether that reach reveals reality or merely reveals the mind's own habits.",
                "A serious reading of the page should leave the reader able to say why the rationalist-empiricist divide still structures modern philosophy."
            ],
            "items": [
                "What kind of truth here seems strongest for the rationalist case: mathematics, modality, self-knowledge, or metaphysics?",
                "Where does rationalism most plausibly outrun experience?",
                "Which of the classical figures best captures the tradition's ambition for your purposes?",
                "How does the sufficient reason impulse shape later metaphysics?",
                "What would an empiricist say is being smuggled in too quickly on this page?"
            ],
        },
    },
    "Scholastics": {
        "source_heading": "Read scholasticism as disciplined argument, not dead jargon.",
        "source_intro": "This dossier frames scholasticism around a method and a problem: how to reason with maximum precision about theology, metaphysics, ethics, and law without pretending faith excuses the hard work of distinction.",
        "source_cards": {
            "Original framing": "A branch page built around university disputation, medieval conceptual rigor, and the faith-reason relation rather than around caricatures of dusty medievalism.",
            "Preserved texture": "The page preserves the scholastic habit of stating objections fairly, distinguishing senses carefully, and answering by tightening the question instead of widening the rhetoric.",
            "Historical setting": "Medieval university culture, where Aristotle, Christian theology, Roman law, and institutional education converged into a high-pressure environment for formal argument.",
            "Primary texts nearby": "Aquinas's Summa Theologiae, Scotus's Ordinatio, Ockham's Summa Logicae, and selections from Anselm, Bonaventure, and late scholastic commentators.",
            "Ideas in view": "Faith and reason, universals, essence and existence, natural law, analogy, individuation, and parsimony.",
            "Influence trail": "Natural law theory, formal logic, metaphysics, philosophy of religion, legal reasoning, and early modern reactions against scholastic conceptual machinery.",
        },
        "source_read": "The page should be read with one corrective in mind: scholasticism is not a stack of answers but a disciplined style of asking, dividing, and defending questions that later philosophy often inherits even while mocking the vocabulary.",
        "sections": {
            "prompt-1": {
                "heading": "What scholasticism is really trying to do",
                "paragraphs": [
                    "Scholasticism is a medieval style of philosophical and theological inquiry marked by structured disputation, conceptual precision, and an unusual confidence that difficult questions become clearer when the relevant distinctions are sharpened rather than blurred.",
                    "Its best-known practitioners are working inside religious traditions, but the method is philosophically larger than confessional loyalty. A scholastic asks what exactly is being claimed, what objections arise, what ambiguity is distorting the issue, and what follows if each option is pursued consistently.",
                    "That is why scholasticism matters beyond medieval history. It helps explain how philosophy learned to build objections systematically, organize debates by distinctions, and pursue metaphysical structure without treating rhetoric as argument.",
                    "The tradition is not internally uniform. Anselm, Aquinas, Scotus, and Ockham disagree deeply about universals, individuation, God's relation to reason, and how much conceptual economy should guide theory. The unity lies in disciplined argument, not in doctrinal sameness."
                ],
                "items": [
                    "Core pressure: difficult questions become tractable only when key distinctions are made explicit.",
                    "Method: objection, reply, distinction, and ordered conclusion.",
                    "Why it matters: scholasticism helped standardize rigorous argumentative form.",
                    "Best first test: can the page show why formal precision was intellectually productive rather than merely ornamental?"
                ],
            },
            "prompt-2": {
                "heading": "How scholastics reshaped later philosophy",
                "paragraphs": [
                    "Their first contribution is procedural. Scholastics made the objection-and-reply format intellectually serious, which later philosophy inherits even when it abandons medieval metaphysics.",
                    "A second contribution is metaphysical refinement. Questions about substance, essence, existence, universals, individuation, and causation were sharpened with a level of precision that early modern philosophers could not simply ignore.",
                    "The tradition also gave later ethics and political thought natural law resources that remain active in debates about rights, moral realism, and the structure of practical reason.",
                    "Finally, scholasticism shaped logic and semantic analysis. Ockham in particular shows that medieval thinkers were often much closer to later analytic concerns than the usual caricature admits."
                ],
                "items": [
                    "Argumentative form: the disciplined staging of objections and replies.",
                    "Metaphysical precision: refined vocabularies for being, causation, universals, and individuation.",
                    "Natural law and ethics: durable tools for thinking about normativity and human goods.",
                    "Logic and semantics: medieval resources that quietly prefigure later analytic rigor."
                ],
            },
            "prompt-3": {
                "heading": "The figures who gave scholasticism its durable shape",
                "paragraphs": [
                    "Anselm matters because he shows the early medieval fusion of prayerful seriousness and argumentative daring. He is an early sign that theological commitment need not preclude conceptual boldness.",
                    "Thomas Aquinas stands near the center because he integrates Aristotelian metaphysics, Christian theology, and legal reasoning into a vast but surprisingly orderly architecture. He makes scholasticism look comprehensive without making it shapeless.",
                    "John Duns Scotus matters for the sheer sharpness of his distinctions and for his influence on later debates about individuation, will, and univocity. William of Ockham matters because he pushes economy, logic, and anti-metaphysical caution harder than many predecessors.",
                    "Together these figures show why scholasticism should not be treated as one voice. It is a field of high-resolution disagreement carried out under shared norms of argumentative discipline."
                ],
                "items": [
                    "Anselm for early rigor and conceptual daring.",
                    "Aquinas for synthesis, natural law, and metaphysical architecture.",
                    "Scotus for subtle distinction and the sharpened will/intellect debate.",
                    "Ockham for logical economy, nominalism, and resistance to metaphysical excess."
                ],
            },
            "prompt-4": {
                "heading": "A dialogue that shows how a scholastic teaches",
                "paragraphs": [
                    "A useful dialogue begins with the student's impatience: 'Why not just answer the question directly?' The scholastic's first reply is methodological. Direct answers often fail because the question is still ambiguous, and ambiguity is where error enters.",
                    "The student should then complain that all this distinction-making looks evasive. That objection matters because scholasticism really can degenerate into verbal overproduction when distinctions multiply without explanatory payoff.",
                    "The page becomes pedagogically alive when one case is used to justify the method: perhaps free will and foreknowledge, universals, natural law, or whether existence belongs to essence. In a good exchange the distinctions reduce confusion rather than inflate prestige.",
                    "End by showing why the style survives. Modern readers may not inherit every thesis, but they still inherit the demand to state objections fairly, define terms carefully, and resist the temptation to win by blur."
                ],
                "items": [
                    "Begin with the student's impatience about method.",
                    "Let the charge of hair-splitting speak clearly so the page can answer it.",
                    "Use one classical puzzle to prove that distinctions can genuinely clarify.",
                    "Close by connecting scholastic habits to later standards of rigor."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "Scholasticism ties argumentative form to metaphysical seriousness.",
                "Its living legacy is not that modern readers must endorse every medieval thesis, but that clear objections and precise distinctions are still conditions of serious thought.",
                "The page should leave the reader able to say why later philosophy both inherited scholastic rigor and rebelled against scholastic overreach."
            ],
            "items": [
                "Which scholastic tool here still feels most alive: distinction, natural law, logic, or metaphysical system?",
                "Where does scholastic precision clarify a real problem rather than multiplying jargon?",
                "How do Aquinas, Scotus, and Ockham differ in what they think rigor requires?",
                "What early modern revolt against scholasticism now looks oversimplified?",
                "What current debate would improve if argued in a more scholastic way?"
            ],
        },
    },
    "Philosopher Club Membership": {
        "source_heading": "Read this page as a test of the category, not as a trivia game.",
        "source_intro": "This dossier turns the page's odd question into a serious one: what are we really rewarding when we call someone a philosopher, and what gets erased when the label becomes gatekeeping shorthand?",
        "source_cards": {
            "Original framing": "A classificatory page about who counts as a philosopher and why the answer keeps moving with institutions, genres, and standards of rigor.",
            "Preserved texture": "The page preserves the pressure between philosophy as a professional discipline and philosophy as a lived practice of inquiry, criticism, and self-examination.",
            "Historical setting": "A long history in which sages, theologians, essayists, dramatists, scientists, and public intellectuals have all sometimes done philosophy before departments decided who counted officially.",
            "Primary texts nearby": "Dialogues, aphorisms, meditations, sermons, essays, treatises, and public interventions that blur the line between philosopher, teacher, critic, and cultural theorist.",
            "Ideas in view": "Criteria of rigor, method, conceptual originality, public argument, practical wisdom, and institutional gatekeeping.",
            "Influence trail": "Canon formation, curriculum design, public philosophy, and disputes over whether philosophy is mainly a profession, a genre, or a practice.",
        },
        "source_read": "The useful question is not who wins admission to an honor society. It is which criteria help us separate serious philosophical work from mere reputation without shrinking philosophy down to one modern academic costume.",
        "sections": {
            "prompt-1": {
                "heading": "How to sort the category without pretending it is natural",
                "paragraphs": [
                    "The prompt about categories is useful only if the page turns it into criteria. A serious answer should distinguish at least five different ways people end up in the philosopher club: system-builders, conceptual arguers, moral teachers, public critics, and border figures whose work crosses literature, religion, science, or politics.",
                    "That matters because the history of philosophy has never been populated by one genre alone. Plato writes dialogues, Marcus Aurelius writes self-addressed reflections, Kierkegaard uses pseudonyms, Nietzsche writes aphoristically, and Simone Weil often sounds like a mystic and a political critic at once.",
                    "So the page should not imply that all categories are equally philosophically fertile. The better question is what intellectual work justifies each category: original concepts, disciplined argument, interpretive transformation, practical wisdom, or a sustained challenge to reigning assumptions.",
                    "Once those criteria are visible, the category list stops being arbitrary. It becomes a map of the many forms philosophical labor has actually taken."
                ],
                "items": [
                    "Possible categories: canonical system-builders, argumentative analysts, sages and moral cultivators, public critics, and hybrid border figures.",
                    "What matters is not the label but the kind of philosophical work being done.",
                    "Some figures belong in more than one category; overlap is evidence of range, not of conceptual failure.",
                    "A good list names the criterion for each bucket instead of merely dropping names."
                ],
            },
            "prompt-2": {
                "heading": "Why some historical figures would be surprised by the label",
                "paragraphs": [
                    "Several major figures would likely find the modern job title 'philosopher' too narrow for what they were doing. Confucius would probably hear the label as incomplete because he taught moral formation, ritual cultivation, and political seriousness rather than merely an academic subject.",
                    "Socrates might be surprised for the opposite reason. He left no treatise and would likely resist being treated as a canonized content-provider rather than as a disruptive practice of questioning in public.",
                    "Marcus Aurelius is another good case. He wrote for self-discipline, not for professional recognition. To classify him straightforwardly as a philosopher is accurate, but it risks muting the way his writing functions as spiritual exercise rather than detached theory.",
                    "The page should tell these stories not to destabilize the category for sport, but to remind the reader that philosophical identity has often been assigned retrospectively by later institutions with different priorities."
                ],
                "items": [
                    "Confucius: teacher of cultivation whose work exceeds a modern disciplinary box.",
                    "Socrates: a public interrogator who would resist being reduced to doctrinal ownership.",
                    "Marcus Aurelius or Pascal: a writer whose practical or devotional aim complicates modern professional labels.",
                    "The lesson: categories are retrospective tools, not timeless self-descriptions."
                ],
            },
            "prompt-3": {
                "heading": "What it takes to become a practical philosopher",
                "paragraphs": [
                    "A practical philosopher is not simply someone with advice. The phrase should name a person who can carry conceptual clarity into lived pressure: conflicting duties, public disagreement, distorted incentives, self-deception, and institutional compromise.",
                    "That requires at least three things. First, the person must be able to state a problem without hiding its tension. Second, they must know enough philosophical structure to separate principles, evidence, and rhetoric. Third, they must show how those distinctions change conduct rather than ending in decorative commentary.",
                    "The practical philosopher therefore sits between the detached theorist and the motivational speaker. They keep rigor without becoming inert and seek action without downgrading difficulty.",
                    "A good closing line for the page is that practical philosophy is not philosophy diluted for ordinary life. It is philosophy tested by whether it can survive ordinary life without losing its standards."
                ],
                "items": [
                    "Practical philosophy requires clarity about the problem, not just confidence about the answer.",
                    "It demands translation from principle to case without losing the friction of the principle.",
                    "It should improve judgment, not merely produce quotable slogans.",
                    "Its real mark is whether people can reason better in action because of it."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "The page works when it turns a club-membership joke into a serious question about criteria, genre, and institutional memory.",
                "Its deepest point is that philosophy has always been broader than the contemporary department model, but not so broad that every provocative voice counts equally.",
                "The reader should finish able to explain both why the category matters and why it cannot be treated as natural or self-evident."
            ],
            "items": [
                "Which criterion for 'philosopher' feels most defensible here?",
                "Which historical figure most clearly exposes the limits of a modern professional definition?",
                "How should public philosophy differ from academic philosophy without losing rigor?",
                "Where does canon formation distort the category most severely?",
                "What kind of practical philosopher does the archive itself seem to value?"
            ],
        },
    },
    "Philosophers or Philosophy?": {
        "source_heading": "Read this page as a choice about framing, not a false dichotomy.",
        "source_intro": "This dossier treats the title as an editorial problem: should inquiry be organized around big thinkers or around the concepts and arguments that outlive them?",
        "source_cards": {
            "Original framing": "A meta-page about whether philosopher-centered pathways illuminate philosophical ideas or accidentally replace them with personality and lineage.",
            "Preserved texture": "The page preserves the tension between historical voice and conceptual clarity rather than choosing one and pretending the tradeoff disappears.",
            "Historical setting": "A long intellectual history in which schools, canons, and classrooms have often been organized by charismatic figures even when the underlying questions cut across those figures.",
            "Primary texts nearby": "Author-centered dialogues, concept pages, branch guides, and case studies showing how ideas migrate beyond the people most associated with them.",
            "Ideas in view": "Pedagogy, canon formation, accidents of transmission, conceptual clarity, hero-worship, and the danger of losing live questions inside historical sorting.",
            "Influence trail": "Survey-course design, public philosophy, biography-heavy teaching, and ongoing debates about whether history of philosophy should lead or follow conceptual inquiry.",
        },
        "source_read": "The page should be read with one pedagogical question in view: when does a philosopher help us think, and when does the philosopher become a substitute for thinking?",
        "sections": {
            "prompt-1": {
                "heading": "The benefits and dangers of leading with philosophers",
                "paragraphs": [
                    "Focusing on philosophers has real benefits. It gives ideas a voice, a historical setting, and a recognizable argumentative temperament. Readers often understand skepticism better through Hume, duty better through Kant, or power better through Foucault than through abstract bullet points.",
                    "The danger is that personality and canon can quietly replace the concept. Once that happens, readers learn to say what Plato or Nietzsche thought without learning what the underlying problem is, why the argument bites, or how the idea mutates when removed from its original owner.",
                    "A concept-first approach corrects that problem by showing how questions about freedom, knowledge, language, or justice travel across thinkers and eras. But concept-first work can also become sterile if it erases the historical situations that made those concepts sharp in the first place.",
                    "The page should therefore resist the false choice. Philosophers are often the best entry points into philosophy, provided the reader is continually pushed back from name recognition toward problem recognition."
                ],
                "items": [
                    "Benefit of philosopher-first framing: voice, context, and argumentative personality.",
                    "Danger of philosopher-first framing: hero-worship, canon inertia, and doctrinal memorization.",
                    "Benefit of concept-first framing: comparison, portability, and cleaner problem structure.",
                    "Best editorial rule: use thinkers as entry points, but make concepts the final object of understanding."
                ],
            },
            "prompt-2": {
                "heading": "How accidents of history steer philosophy",
                "paragraphs": [
                    "The trajectory of philosophy is partly an achievement of genius and partly an accident of preservation, translation, institutional prestige, and political survival. Entire traditions become central or peripheral not only because they were best, but because their manuscripts endured, their languages were taught, or their institutions won.",
                    "That matters because readers can mistake the received sequence of influence for the best available development of the ideas. If different texts had been preserved, if more women and non-Western thinkers had been institutionally centered earlier, or if theological and colonial filters had been weaker, our conceptual map might look substantially different.",
                    "The page should not use counterfactuals to flatten real achievements. Plato, Aristotle, Aquinas, Descartes, Kant, Marx, and others matter because they did extraordinary work. The point is that the canon is not self-justifying, and historical success can conceal intellectual path dependence.",
                    "A mature reader therefore treats the history of philosophy as both inheritance and hypothesis: this is the path we got, not automatically the path that would have best served every question."
                ],
                "items": [
                    "Preservation and translation shape what later generations can even read.",
                    "Institutions amplify some voices and bury others for reasons partly independent of merit.",
                    "Canon history is informative but not infallible; it should invite counterfactual humility.",
                    "The best use of history is to ask which neglected trajectories might still improve present inquiry."
                ],
            },
            "prompt-3": {
                "heading": "When influential philosophers made later correction costly",
                "paragraphs": [
                    "Aristotle's physics is a classic case. Its prestige slowed correction because generations inherited not only claims but a whole framework of authority. The deeper lesson is that great philosophers can be wrong in ways that become culturally expensive to challenge.",
                    "Descartes's sharp mind-body split is another useful example. Even where later thought rejects substance dualism, the vocabulary it imposed still structures how people imagine consciousness, mechanism, and subjectivity.",
                    "A third case is the long afterlife of crude social Darwinist or hierarchical readings falsely naturalized through philosophical and quasi-philosophical authority. Once a framework starts looking like reason itself, later correction must fight not only arguments but educational inertia.",
                    "The page should emphasize that errors become entrenched not merely because thinkers were persuasive, but because institutions, curricula, and cultural prestige kept the errors attached to intellectual seriousness."
                ],
                "items": [
                    "Aristotelian physics as a case of prestige delaying correction.",
                    "Cartesian dualism as a case of a framework surviving even after its strongest form weakens.",
                    "Authority-backed hierarchies and pseudoscientific moral theories as cases of canon plus institution reinforcing error.",
                    "The broader lesson: great thinkers should be read with gratitude and suspicion at once."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "This page works when it teaches readers to use philosophers without becoming captive to them.",
                "Its strongest claim is that biography, canon, and conceptual inquiry all matter, but they matter in different roles.",
                "The practical takeaway is editorial: let names open the door, then make the ideas walk out of the building and prove they can stand on their own."
            ],
            "items": [
                "When does a philosopher clarify a concept best on this page?",
                "Where does philosopher-centered teaching become a substitute for real comparison?",
                "Which accident of history seems most distortive for the canon you know best?",
                "What entrenched framework here still shapes current thinking more than it deserves?",
                "How should a site like this balance figures and concepts going forward?"
            ],
        },
    },
    "Philosophical Gradients": {
        "source_heading": "Read this page as a map of continua, not boxes.",
        "source_intro": "This dossier turns the page into a practical methodological guide: many philosophical positions are better understood as gradients with pressure points than as sharply isolated camps.",
        "source_cards": {
            "Original framing": "A meta-page about building gradients that can later hold named philosophers without turning those names into crude stereotypes.",
            "Preserved texture": "The page preserves the intuition that philosophical disagreement often concerns degree, emphasis, and threshold rather than all-or-nothing opposition.",
            "Historical setting": "A long history of taxonomy in which schools and labels help orientation but also create false binaries that conceal intermediate or mixed positions.",
            "Primary texts nearby": "Comparative branch pages, chart pages, and cross-era case studies where one question reappears with multiple gradations rather than a simple yes/no split.",
            "Ideas in view": "Continuum thinking, threshold effects, mixed positions, dimensional analysis, and the difference between a useful axis and a misleading one.",
            "Influence trail": "Pedagogy, comparative philosophy, conceptual cartography, and later work assigning thinkers to spectra without flattening them.",
        },
        "source_read": "The point of a philosophical gradient is not to blur all differences. It is to make the right differences visible by showing where movement along an axis changes what a thinker can consistently say.",
        "sections": {
            "prompt-1": {
                "heading": "Which gradients are worth building",
                "paragraphs": [
                    "A good gradient tracks one real pressure at a time. Instead of vague spectra like 'more philosophical' versus 'less philosophical,' the page should build axes such as rationalism to empiricism, realism to anti-realism, individualism to communitarianism, essentialism to constructivism, or determinism to libertarian freedom.",
                    "Each of those gradients matters because philosophers often disagree by degree and starting point rather than by total opposition. Kant, for example, cannot be plotted usefully on the same line as a simple empiricist-versus-rationalist fight without adding nuance about synthesis and conditions of experience.",
                    "The page should also warn against fake gradients. If an axis bundles multiple issues together, it becomes an instrument of distortion rather than clarity. A moral realism gradient should not secretly do the work of a political conservatism gradient, and a metaphysical materialism scale should not also measure methodological naturalism unless the overlap is argued for explicitly.",
                    "The real test of a gradient is whether movement along it changes what arguments become available, what objections arise, and what neighboring positions look like."
                ],
                "items": [
                    "Possible axes: rationalism-empiricism, realism-anti-realism, freedom-determinism, individualism-communitarianism, and essentialism-constructivism.",
                    "Each gradient should isolate one pressure rather than blending several into one fuzzy line.",
                    "Mixed or intermediate positions are often more illuminating than the poles.",
                    "A useful gradient predicts argumentative consequences, not just labels."
                ],
            },
            "prompt-2": {
                "heading": "How to define points along a gradient",
                "paragraphs": [
                    "For each gradient, the points should be defined by claims, not by names. On a realism-anti-realism gradient, for example, one point might say that truth is fully mind-independent, a middle point might allow structured dependence on conceptual schemes, and an anti-realist point might treat truth as inseparable from warranted assertion or communal practice.",
                    "Using at least five points is wise because it forces nuance. Binary maps tempt readers to force everyone into camps. Five-point or seven-point scales let you distinguish strong, moderate, hybrid, and unstable positions.",
                    "The descriptions should be short but substantive. Each point needs a defining claim, one implication, and one likely objection. That keeps the gradient from becoming decorative terminology.",
                    "If the points are well defined, later placement of philosophers becomes easier and less dogmatic because the reader can see what exactly is being attributed."
                ],
                "items": [
                    "Define points by theses, not by famous names.",
                    "Use enough points to separate strong, moderate, hybrid, and transitional positions.",
                    "Give each point a consequence and an objection, not just a slogan.",
                    "Keep the scale internally consistent so movement from one point to the next is intelligible."
                ],
            },
            "prompt-3": {
                "heading": "How to place philosophers on the gradients without flattening them",
                "paragraphs": [
                    "The next step should be treated as provisional mapping, not final taxonomy. Many philosophers occupy different places on different gradients, and some even move within one gradient across different works or questions.",
                    "That means placement should be justified locally. Do not simply write 'Aristotle is point three' or 'Nietzsche is point five.' State which text, concept, or argumentative habit warrants the placement and where the placement becomes contestable.",
                    "It also helps to mark confidence levels. Some cases are straightforward; others are deliberately mixed or strategically unstable. A page that can say 'provisional placement with reasons' is more trustworthy than one that pretends every figure sits neatly on a chart.",
                    "The best use of gradients is comparative. Once thinkers are placed, the real payoff is seeing why neighbors who look close on one axis may differ sharply on another."
                ],
                "items": [
                    "Place philosophers by text and argument, not by reputation.",
                    "Expect one thinker to occupy different regions on different gradients.",
                    "Mark low-confidence or contested placements explicitly.",
                    "Use the gradients to generate comparisons, not to end them."
                ],
            },
        },
        "synthesis": {
            "paragraphs": [
                "Philosophical gradients are useful when they replace crude binaries with structured comparison.",
                "Their danger is that a bad axis can look precise while smuggling together unrelated questions.",
                "A good reader should leave the page able to design a gradient, define its points, and place thinkers on it without pretending the map is the territory."
            ],
            "items": [
                "Which axis here seems most pedagogically useful?",
                "What would count as a misleading or overloaded gradient?",
                "How many points are enough for nuance without making the scale mushy?",
                "Which philosopher would be hardest to place honestly on a single axis?",
                "What comparison becomes possible once the gradients are built well?"
            ],
        },
    },
}

SPECIAL_PAGE_PROFILES.update(CURRENT_BATCH_SPECIAL_PAGE_PROFILES)


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
        subject = match.group(1).strip().rstrip(".")
        return f"What {subject} actually clarifies"

    match = re.fullmatch(r"What changes once we define (.+) more carefully", text)
    if match:
        subject = match.group(1).strip().rstrip(".")
        return f"What becomes clearer once {subject} is defined carefully"

    match = re.fullmatch(r"A concrete case shows what (.+) explains and where it strains\.", text)
    if match:
        return f"What {match.group(1)} clarifies, and where its limits show"

    match = re.fullmatch(r"The map of (.+) becomes useful once the parts stop doing different work\.", text)
    if match:
        return f"Why {match.group(1)} matters in practice"

    match = re.fullmatch(r"(.+) matters only if it survives the strongest pressure against it\.", text)
    if match:
        return f"Testing {match.group(1)} under pressure"

    match = re.fullmatch(r"Vanishing-probability mistakes recur whenever .+", text)
    if match:
        return "How vanishing-probability mistakes take hold"

    if text.startswith("Clarifying "):
        subject = text[len("Clarifying ") :].strip().rstrip(".")
        return f"What {subject} helps clarify"

    if text.startswith("Testing ") and text.endswith(" under pressure"):
        subject = text[len("Testing ") : -len(" under pressure")].strip().rstrip(".")
        return f"Putting {subject} under pressure"

    match = re.fullmatch(r"Putting (.+) under pressure", text)
    if match:
        subject = match.group(1).strip().rstrip(".")
        return f"Testing {subject} more closely"

    match = re.fullmatch(r"What (.+) explains, and where it starts to strain", text)
    if match:
        return f"What {match.group(1)} clarifies, and where its limits show"

    match = re.fullmatch(r"What (.+) actually clarifies", text)
    if match:
        subject = match.group(1).strip().rstrip(".")
        return f"What {subject} really means in practice"

    return text


def heading_from_prompt(prompt_text: str, page_title: str, heading_text: str, section_id: str) -> str:
    prompt_text = " ".join(prompt_text.split())
    heading_text = " ".join(heading_text.split())
    prompt_lower = prompt_text.lower()
    title_subject = page_title.split(" on ", 1)[0].strip()

    match = re.match(r"Provide a general description of (?:the philosophical school of )?(.+?)\.$", prompt_text, re.IGNORECASE)
    if match and section_id == "prompt-1":
        return f"What {match.group(1)} is really trying to do"

    if section_id == "prompt-1":
        if "influence on philosophy" in prompt_lower:
            return f"Why {page_title} still matters to later philosophy"
        if "remains philosophically important" in prompt_lower:
            return f"Why {page_title} remains philosophically important"
        if prompt_lower.startswith("what are the major schools of thought"):
            return "What are the major schools of thought in philosophy of mind?"
        if "background of the author of this article" in prompt_lower:
            return "Who the author is, and why that matters here"

    if section_id == "prompt-2":
        if prompt_lower.startswith("using the 7 schools of thought"):
            return "How the main schools divide over whether mind is fundamental"
        if "7 greatest contributions" in prompt_lower:
            return f"How {page_title} still shapes later thought"
        if "annotated list" in prompt_lower and "contributions" in prompt_lower:
            return f"How {page_title} still shapes later thought"
        match = re.match(r"Provide a list of the key contributions (.+?) ha(?:s|ve) made to philosophical thought\.$", prompt_text, re.IGNORECASE)
        if match:
            return f"How {match.group(1)} reshaped later philosophy"
        if "key concepts" in prompt_lower or "major concepts" in prompt_lower:
            return f"The ideas that make {page_title} more than a label"
        if "6-month self-study program" in prompt_lower:
            return f"A six-month path into {page_title}"
        if "well-structured assessment" in prompt_lower or "assessment of" in prompt_lower:
            return f"The strongest parts of the argument, and where they strain"
        if "provide a profile of the podcast guest" in prompt_lower or (
            prompt_lower.startswith("provide a profile of")
            and "links to media" in prompt_lower
        ):
            return f"Who {title_subject} is and where to explore more of the work"
        if "actual historical examples" in prompt_lower and "trauma of what happened" in prompt_lower:
            return "Five traumas that look different once counterfactuals enter"
        if "nicholas cage" in prompt_lower and "swimming pool drownings" in prompt_lower:
            return "A famous spurious correlation, and what it actually teaches"

    if section_id == "prompt-3":
        if "most likely causes behind" in prompt_lower and "becoming a notable philosopher" in prompt_lower:
            return f"Why {page_title} became so influential"
        match = re.match(r"List the most influential (.+?) in history\.$", prompt_text, re.IGNORECASE)
        if match:
            subject = match.group(1).strip()
            subject = SCHOOL_NAME_BY_FIGURE_LABEL.get(subject.lower(), subject)
            return f"The figures who gave {subject} its durable shape"
        if "strongest objection" in prompt_lower:
            return f"The hardest objection {page_title} still has to answer"
        if "25 of the most relevant questions" in prompt_lower:
            return "Questions that still organize philosophy of mind"
        if "actual historical examples" in prompt_lower and "greater success" in prompt_lower:
            return "Five successes that may have hidden even better possibilities"
        if "new industries and career opportunities" in prompt_lower:
            return "What new work AI may create as old roles disappear"

    if section_id == "prompt-4":
        if "which schools of philosophical thought" in prompt_lower or "which academic domains" in prompt_lower:
            return f"Where {page_title} left the deepest mark"
        match = re.match(r"Produce a 20-line hypothetical dialogue between (?P<subject>(?:an?|the) .+?) and .+\.$", prompt_text, re.IGNORECASE)
        if match:
            return f"A dialogue that shows how {match.group('subject')} thinks in practice"
        if "dialogue" in prompt_lower:
            return f"A dialogue that tests what {page_title} can explain"
        if "how should a contemporary reader begin with" in prompt_lower:
            return f"How to begin reading {page_title} today"
        if "entry point" in prompt_lower or "best entry point" in prompt_lower:
            return f"The best way into {page_title} for a new reader"
        if "20 questions/answer pairs" in prompt_lower:
            return "A classroom dialogue that surfaces the live disputes"
        if "negatively affect rationality" in prompt_lower:
            return "How this asymmetry distorts rational judgment"
        if "human psyche and social interactions" in prompt_lower:
            return "How optional work could reshape identity and social life"

    if section_id == "prompt-5":
        if "what other disciplines are a good foundation" in prompt_lower:
            return "Which disciplines best prepare you for advanced work in philosophy of mind"
        if "how might we inoculate ourselves" in prompt_lower:
            return "How to keep the actual from burying the plausible"

    if prompt_lower.startswith("provide a list of proposed ontological domains"):
        return "The main ontological domains philosophers tend to propose"
    if prompt_lower.startswith("what is economics"):
        return "What economics studies, and why scarcity is only the beginning"
    if prompt_lower.startswith("what are the minimal conditions for a stable economy"):
        return "What most economists mean by a stable economy"
    if prompt_lower.startswith("describe the major schools of economic thought"):
        return "The major schools of economic thought, and what divides them"
    if prompt_lower.startswith("provide a clear definition of moral hazards and 7 examples"):
        return "What moral hazard means in economics, with seven examples"
    if prompt_lower.startswith("how essential is taxation to a functioning state"):
        return "Why taxation matters to a functioning state"
    if prompt_lower.startswith("what common categories and definitions of “explanation”"):
        return "The main kinds of explanation philosophers use"
    if prompt_lower.startswith("what common categories and definitions of \"explanation\""):
        return "The main kinds of explanation philosophers use"
    if prompt_lower.startswith("what are the components and qualities of a powerful analogy"):
        return "What makes an analogy clarifying rather than misleading"
    if prompt_lower.startswith("assess the following statement against the notion that rational belief"):
        return "Why evidence usually supports degrees of belief, not a binary leap"
    if prompt_lower.startswith("what are other terms similar to “preponderance”"):
        return "Threshold language that can distort graded belief"
    if prompt_lower.startswith("what are other terms similar to \"preponderance\""):
        return "Threshold language that can distort graded belief"
    if prompt_lower.startswith("provide the necessary and sufficient conditions for land ownership"):
        return "What a society needs before land ownership can emerge"
    if prompt_lower.startswith("many religious ideologies insist that humans know"):
        return "Why 'you already know it is true' works as a gaslighting tactic"
    if prompt_lower.startswith("one rather dishonorable tactic in public discourse is moving"):
        return "How connotative equivocation manipulates audiences"
    if prompt_lower.startswith("elaborate on any dependencies among these ontological domains"):
        return "How the proposed ontological domains depend on one another"
    if prompt_lower.startswith("for each of the following types of explanation"):
        return "How different kinds of explanation work in practice"
    if prompt_lower.startswith("for the following types of emergence"):
        return "Examples that show where kinds of emergence differ"
    if prompt_lower.startswith("list and define 30 key terms in metaphysics"):
        return "Thirty anchor terms in metaphysics"
    if prompt_lower.startswith("list and provide explanations of 15 key concepts in metaphysics"):
        return "Fifteen concepts that organize metaphysical debate"
    if prompt_lower.startswith("list and define 30 key terms fundamental to understanding the philosophy of science"):
        return "Thirty anchor terms in philosophy of science"
    if prompt_lower.startswith("list and provide explanations of 15 key concepts in philosophy of science"):
        return "Fifteen concepts that organize philosophy of science"

    return normalize_heading_text(heading_text)


def should_remove_paragraph(text: str) -> bool:
    cleaned = " ".join(text.split())
    if "Gemini failed" in cleaned or "GEMINI:" in cleaned:
        return True
    if cleaned.startswith((
        "The prompt matters because it changes what the reader should investigate next about ",
        "The prompt is valuable only if it makes ",
        "This section should orient the reader to the structure of ",
        "The point of this prompt is to make ",
        "This section should test how much argumentative weight ",
        "A useful explanation of ",
        "The exchange should surface the real dispute behind ",
        "After this section, the reader should be able to restate ",
        "A strong ethical explanation should be able to survive one concrete case ",
        "The page becomes clearer once the idea is tied to a recognizable life problem ",
        "An introductory page works best when it gives the reader a map for comparison ",
        "A metaphysical claim earns trust when it clarifies one stubborn puzzle, ",
        "A good language example shows how a phrase can sound harmless in ordinary conversation ",
        "A concrete case helps here because consciousness talk becomes vague very quickly ",
        "A useful example should move the discussion from labels to judgment ",
        "A map is an argument about importance. ",
        "The payoff is not tech awe but cleaner distinctions ",
        "The payoff should be a judgment the reader can actually use outside this single page.",
        "The earlier sections should already have put ",
    )):
        return True
    if cleaned.startswith("First get clear on "):
        return True
    if cleaned.startswith("Try a live borderline case."):
        return True
    if cleaned.startswith("A fair pushback is that ordinary life cannot wait for perfect evidence."):
        return True
    if cleaned.startswith("A fair pushback is that real decisions often happen quickly."):
        return True
    if cleaned.startswith("The deeper issue in "):
        return True
    if cleaned.startswith("The payoff is "):
        return True
    if cleaned.startswith("A strong example does more than decorate "):
        return True
    if cleaned.startswith("A clear page should therefore hold apart two issues:"):
        return True
    if cleaned.startswith("What makes ") and " worth slowing down over is that the topic changes how the reader organizes " in cleaned:
        return True
    if cleaned.startswith("The page becomes more useful once that organizational work is explicit"):
        return True
    if cleaned.startswith("The topic becomes more useful once the reader can state plainly what claim is being made"):
        return True
    if cleaned.startswith("That clarity matters because the page should help the reader sort core claims"):
        return True
    if cleaned.startswith("A workable definition of ") and "has to do more than offer a tidy phrase." in cleaned:
        return True
    if cleaned.startswith("That boundary matters because people often move from one familiar example"):
        return True
    if cleaned.startswith("A useful dialogue about ") and "claim precise enough to be tested" in cleaned:
        return True
    if "remains epistemically opaque" in cleaned:
        return True
    if cleaned.startswith("This section should give the reader a usable epistemic lever:"):
        return True
    if cleaned.startswith("Start with ") and "Without that first grip" in cleaned:
        return True
    if cleaned.startswith("Keep ") and " in the same frame." in cleaned:
        return True
    if cleaned.startswith("Keep ") and "That is what shows what the page is claiming" in cleaned:
        return True
    if cleaned.startswith("Keep ") and (
        " distinct from " in cleaned
        and "They are not interchangeable bits of vocabulary; they point the reader toward different judgments, objections, or next steps." in cleaned
    ):
        return True
    return any(pattern.match(cleaned) for pattern in REMOVE_PARAGRAPH_PATTERNS)


def should_remove_list_item(text: str) -> bool:
    cleaned = " ".join(text.split())
    return any(pattern.match(cleaned) for pattern in REMOVE_LIST_ITEM_PATTERNS)


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
    stock_phrases = (
        "One practical test is to place the idea next to a familiar case and ask what changes in the analysis once the distinction is taken seriously.",
        "The section is doing its job when the reader can explain",
        "is best approached as a live problem with pressure points rather than as a settled slogan.",
        "becomes more intelligible when it is forced into a concrete case instead of left at the level of slogan.",
        "looks simpler than it is when the page treats every nearby idea as interchangeable.",
        "The central question is whether ",
    )
    if any(phrase in content for phrase in stock_phrases):
        return True
    if heading_text.startswith("What changes once we define "):
        return True
    if heading_text.startswith("Now provide "):
        return True
    if len(content.split()) < 95:
        return True
    if len(paragraphs) < 2:
        return True
    if "in from vocabulary" in content or "disappeared ." in content:
        return True
    if "The pedagogical payoff is practical." in content:
        return True
    if "matters because it clarifies" in content:
        return True
    if heading_text and heading_text.endswith("had been"):
        return True
    return bool(GENERIC_SECTION_RE.search(content))


def synthesize_section_paragraphs(page: dict, page_title: str, prompt_text: str, heading_text: str) -> list[str]:
    topic = topic_label(page_title)
    focus = prompt_focus(prompt_text)
    key = clean_discussion_key(short_prompt_key(prompt_text, topic), topic, topic)
    frame, example = page_frame(page)
    subject = key or topic or page_title

    first_by_focus = {
        "definition": f"{subject} matters because people often use one label for several different claims at once. A solid definition separates those claims so the reader can see {frame}.",
        "mapping": f"{subject} looks simpler than it is when the page treats every nearby idea as interchangeable. The job here is to show which parts belong together, which do not, and where the boundaries actually matter.",
        "examples": f"{subject} becomes more intelligible when it is forced into a concrete case instead of left at the level of slogan. Examples expose whether the distinction guides judgment or merely decorates it.",
        "argument": f"The central question is whether {subject} can bear the conclusion being attached to it. That requires isolating the strongest support, the hidden assumptions, and the point where the argument is most likely to overreach.",
        "description": f"A worthwhile description of {subject} should do more than rename the topic. It should show what ordinary talk blurs together and why the distinction earns a place in careful thinking.",
        "inquiry": f"{subject} is best approached as a live problem with pressure points rather than as a settled slogan. The reader should come away clearer on what supports the view, what weakens it, and what confusion it is trying to prevent.",
        "dialogue": f"A dialogue about {subject} earns its place only when the speakers force each other to say something answerable to reasons. The exchange should clarify assumptions, expose tensions, and leave the disagreement sharper than it began.",
    }
    first = first_by_focus.get(focus, first_by_focus["inquiry"])
    second_by_focus = {
        "definition": f"Start by separating the nearby questions the label tends to hide. Once those are visible, the reader can tell whether the page is defining a mechanism, a norm, a historical pattern, or only a loose family resemblance.",
        "mapping": f"A useful map should help with borderline cases, not just obvious ones. The important step is to show where a neighboring position starts to do different explanatory work and why that difference matters.",
        "examples": example,
        "argument": f"The charitable version should be stated before the criticism lands. Only then can the page test whether the conclusion outruns the premises, whether a missing distinction is doing damage, or whether an overlooked rival explanation does the real work.",
        "description": f"Description becomes useful only when it reorganizes attention. The reader should be able to point to one feature that was previously blurred and explain why the cleaner description changes later judgment.",
        "inquiry": example,
        "dialogue": f"The exchange should move through one recognizable case so that each speaker has to commit to something testable. Without that pressure, dialogue turns into alternating slogans instead of a lesson in disciplined disagreement.",
    }
    second = second_by_focus.get(focus, second_by_focus["inquiry"])
    third_by_focus = {
        "definition": f"By the end, the reader should be able to use {subject} more carefully, reject the most common misclassification, and say what evidence or argument would force a revision.",
        "mapping": f"The section succeeds when the reader can place a new example on the map, defend that placement, and explain which neighboring label would mislead them.",
        "examples": f"The example earns its place only if it sharpens judgment. A good reader should finish the section able to say what the case reveals, what it leaves unresolved, and how a different case might push the conclusion the other way.",
        "argument": f"The section is doing its job when the reader can state the strongest version of the claim, name the pressure point that still threatens it, and see what kind of evidence would actually settle more of the dispute.",
        "description": f"The section earns its keep when the reader can restate {subject} in plain language, connect it to one live case, and avoid the shortcut that originally made the topic look simpler than it is.",
        "inquiry": f"The section is doing its job when the reader can explain {subject} without jargon, spot the most tempting misuse, and identify what further evidence, argument, or comparison would most improve the view.",
        "dialogue": f"A strong closing move leaves the disagreement narrower and more honest. The reader should see what each side now owes in reasons, where the real disagreement remains, and why the issue is not settled by verbal confidence alone.",
    }
    third = third_by_focus.get(focus, third_by_focus["inquiry"])
    return [first, second, third]


def synthesized_section_items(page: dict, page_title: str, prompt_text: str) -> list[str]:
    topic = topic_label(page_title)
    key = clean_discussion_key(short_prompt_key(prompt_text, topic), topic, topic)
    focus = prompt_focus(prompt_text)
    subject = key or topic or page_title

    if focus == "examples":
        return [
            f"Ask what the example clarifies about {subject}, not just whether it sounds vivid.",
            "Notice which background assumptions the example quietly relies on.",
            "Check whether the case supports the conclusion or merely illustrates it.",
            "Ask what a nearby counterexample would have to look like."
        ]
    if focus == "dialogue":
        return [
            "The exchange should reveal a real disagreement, not just alternate monologues.",
            f"Watch for the point where one speaker forces a clearer definition of {subject}.",
            "A good dialogue earns one concession without pretending the dispute is finished.",
            "The best closing move sharpens the question rather than dissolving it."
        ]
    if focus == "mapping":
        return [
            f"Keep the parts of {subject} distinct enough that each one does identifiable work.",
            "Look for the boundary between neighboring positions, not just the names of the positions.",
            "Ask which distinction would matter most in a real disagreement.",
            "A useful map should help the reader classify a borderline case."
        ]
    return [
        f"State the clearest version of {subject} before testing it.",
        "Ask what evidence, example, or argument would genuinely change the reader's judgment.",
        "Notice where a familiar phrase is doing more work than the reasoning beneath it.",
        "Keep the neighboring concepts visible so the page does not collapse different questions together."
    ]


def paragraph_is_generic_scaffold(text: str) -> bool:
    cleaned = " ".join(text.split())
    generic_markers = (
        "is best approached as a live problem with pressure points rather than as a settled slogan.",
        "looks simpler than it is when the page treats every nearby idea as interchangeable.",
        "The section is doing its job when the reader can explain",
        "A useful map should help with borderline cases, not just obvious ones.",
        "The section succeeds when the reader can place a new example on the map,",
        "The example earns its place only if it sharpens judgment.",
        "Start by separating the nearby questions the label tends to hide.",
        "By the end, the reader should be able to use ",
        "The payoff is ",
        "What makes ",
        "The page becomes more useful once ",
        "The key distinction is not verbal ornament.",
        "That matters because readers otherwise slide too quickly ",
        "A useful dialogue about ",
        "The reader should come away with a narrower disagreement ",
        "The pressure point is whether ",
    )
    return any(marker in cleaned for marker in generic_markers)


def support_paragraphs_for_section(page: dict, page_title: str, prompt_text: str) -> list[str]:
    topic = topic_label(page_title)
    focus = prompt_focus(prompt_text)
    subject = clean_discussion_key(short_prompt_key(prompt_text, topic), topic, topic) or topic or page_title
    frame, example = page_frame(page)

    if focus == "definition":
        return [
            f"A workable definition of {subject} has to do more than offer a tidy phrase. It should identify which features are central, which are optional, and which nearby cases only look similar from a distance.",
            f"That boundary matters because people often move from one familiar example to a much larger conclusion about {frame}. A good definition slows that move down and makes the inference answerable to clearer standards.",
        ]
    if focus == "mapping":
        return [
            f"The point of mapping {subject} is comparative rather than decorative. The reader needs to see which neighboring positions overlap, where they diverge, and why those differences affect later judgment.",
            "Once the boundaries are visible, later disagreements become easier to diagnose because a dispute that looked like one disagreement often turns out to involve several distinct questions moving together.",
        ]
    if focus == "examples":
        return [
            f"A strong example does more than decorate {subject}. It shows which part of the view survives contact with a concrete case and which part starts to wobble once consequences, constraints, or counterexamples become visible.",
            example,
        ]
    if focus == "argument":
        return [
            f"The real test is whether {subject} can support the conclusion being asked of it once the strongest objections are stated clearly and without caricature.",
            "That requires separating what the argument has actually established from what is only being suggested by tone, framing, or a leap that still needs support.",
        ]
    if focus == "dialogue":
        return [
            f"A useful dialogue about {subject} should force each side to make at least one claim precise enough to be tested rather than merely restated more confidently.",
            "The reader should leave with a narrower disagreement, a clearer picture of the main pressure point, and a better sense of what evidence or distinction would matter next.",
        ]
    return [
        f"The topic becomes more useful once the reader can state plainly what claim is being made and how it changes judgment about {frame}.",
        "That clarity matters because the page should help the reader sort core claims from supporting claims, and genuine explanation from rhetorical atmosphere.",
    ]


def list_needs_rewrite(section) -> bool:
    list_tag = section.find(["ol", "ul"], recursive=False)
    if list_tag is None:
        return False
    items = [" ".join(item.get_text(" ", strip=True).split()) for item in list_tag.find_all("li", recursive=False)]
    if not items:
        return False
    generic_prefixes = (
        "The central distinction",
        "Central distinction:",
        "The strongest charitable version:",
        "The main pressure point:",
        "The neighboring question:",
        "Best charitable version:",
        "Pressure point:",
    )
    if any(item.startswith(generic_prefixes) for item in items):
        return True
    return len(set(items)) <= max(1, len(items) // 2)


def strengthen_section_html(section_html: str, page: dict, page_title: str) -> str:
    soup = BeautifulSoup(section_html, "html.parser")
    section = soup.find("section")
    if section is None:
        return section_html

    prompt_note = section.find("p", class_="article-section__prompt", recursive=False)
    heading = section.find("h2", recursive=False)
    dialogue_card = section.find("div", class_="dialogue-card", recursive=False)
    if prompt_note is None or heading is None:
        return section_html

    prompt_text = normalized_prompt_text(prompt_note.get_text(" ", strip=True))
    heading_text = strip_tags(str(heading))
    paragraphs = [
        p for p in section.find_all("p", recursive=False)
        if "article-section__prompt" not in (p.get("class") or [])
    ]
    paragraph_texts = [strip_tags(str(p)) for p in paragraphs]
    needs_paragraph_rewrite = section_needs_rewrite(page, heading_text, paragraph_texts)
    needs_list_rewrite = list_needs_rewrite(section)
    if not needs_paragraph_rewrite and not needs_list_rewrite:
        return str(section)

    if needs_paragraph_rewrite:
        preserved_paragraphs = [
            text for text in paragraph_texts
            if text and not paragraph_is_generic_scaffold(text)
        ]
        for paragraph in paragraphs:
            paragraph.decompose()
        rewritten_paragraphs = preserved_paragraphs[:2] + support_paragraphs_for_section(page, page_title, prompt_text)
        new_paragraphs = BeautifulSoup(
            render_paragraphs(rewritten_paragraphs),
            "html.parser",
        )
        insertion_point = heading
        for new_paragraph in list(new_paragraphs.find_all("p", recursive=False)):
            insertion_point.insert_after(new_paragraph)
            insertion_point = new_paragraph

    if needs_list_rewrite:
        list_tag = section.find(["ol", "ul"], recursive=False)
        if list_tag is not None:
            list_tag.decompose()
        if dialogue_card is None:
            new_list = soup.new_tag("ol")
            for item_text in synthesized_section_items(page, page_title, prompt_text):
                li = soup.new_tag("li")
                li.string = item_text
                new_list.append(li)
            heading.insert_after(new_list)

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

    source_section = soup.select_one("#source-texture")
    if source_section is not None:
        heading = source_section.find("h2", recursive=False)
        paragraphs = source_section.find_all("p", recursive=False)
        intro_paragraph = paragraphs[0] if paragraphs else None
        closing_paragraph = paragraphs[-1] if len(paragraphs) >= 2 else None
        if heading is not None:
            heading.string = f"Read {page_title} as a live method, not just a label."
        if intro_paragraph is not None:
            intro_paragraph.clear()
            intro_paragraph.append(
                f"This dossier keeps the page oriented around the problem, method, and nearby texts "
                f"that make {page_title} worth revisiting."
            )

        cards_by_label = {}
        for card in source_section.select(".source-dossier__card"):
            label = card.select_one(".mini-label")
            bodies = card.find_all("p")
            if not label or len(bodies) < 2:
                continue
            cards_by_label[" ".join(label.get_text(" ", strip=True).split())] = bodies[-1]

        original_framing = cards_by_label.get("Original framing")
        if original_framing is not None:
            original_framing.string = (
                f"An editorial orientation page designed to make {page_title} teachable without "
                f"reducing the figure or school to a slogan."
            )

        preserved_texture = cards_by_label.get("Preserved texture")
        if preserved_texture is not None:
            preserved_text = " ".join(preserved_texture.get_text(" ", strip=True).split())
            preserved_text = re.sub(r"^(?:The page preserves\s+)+", "", preserved_text)
            preserved_text = re.sub(
                rf"^What is being preserved is the way {re.escape(page_title)} proceeds, not just a pile of conclusions\.\s*",
                "",
                preserved_text,
            )
            preserved_text = re.sub(
                r"^What is being preserved is the way .*? proceeds, not just a pile of conclusions\.\s*",
                "",
                preserved_text,
            )
            if preserved_text:
                preserved_texture.string = f"The page preserves {preserved_text[:1].lower()}{preserved_text[1:]}".rstrip()

        if closing_paragraph is not None:
            ideas = cards_by_label.get("Ideas in view")
            ideas_text = ""
            if ideas is not None:
                ideas_text = " ".join(ideas.get_text(" ", strip=True).split())
            focus_sentence = (
                f"Keep asking which distinction does the real explanatory work in {page_title}."
            )
            if ideas_text:
                focus_sentence = (
                    f"Keep asking which distinction among {ideas_text} does the real explanatory work."
                )
            closing_paragraph.string = (
                f"Read with one eye on method and one eye on resistance. The page should leave the "
                f"reader able to name the core move, the pressure it creates, and the later debates it still shapes. "
                f"{focus_sentence}"
            )

        collective_profile = COLLECTIVE_SOURCE_DOSSIERS.get(page_title)
        if collective_profile is not None:
            if intro_paragraph is not None:
                intro_paragraph.clear()
                intro_paragraph.append(collective_profile["source_intro"])
            for label_text, replacement in collective_profile["source_cards"].items():
                body = cards_by_label.get(label_text)
                if body is not None:
                    body.clear()
                    body.append(replacement)

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


def polish_special_batch_page(path: Path, original: str, page_title: str) -> str:
    profile = SPECIAL_PAGE_PROFILES.get(page_title)
    if not profile:
        return original

    soup = BeautifulSoup(original, "html.parser")
    page = page_dict_for_path(path, page_title)

    source_section = soup.select_one("#source-texture")
    if source_section is not None:
        heading = source_section.find("h2", recursive=False)
        source_heading = profile.get("source_heading")
        if heading is not None and source_heading:
            heading.string = source_heading
        paragraphs = source_section.find_all("p", recursive=False)
        source_intro = profile.get("source_intro")
        if len(paragraphs) >= 2 and source_intro:
            paragraphs[1].string = source_intro
        source_cards = profile.get("source_cards", {})
        for card in source_section.select(".source-dossier__card"):
            label = card.select_one(".mini-label")
            bodies = card.find_all("p")
            if not label or len(bodies) < 2:
                continue
            key = " ".join(label.get_text(" ", strip=True).split())
            replacement = source_cards.get(key)
            if replacement:
                bodies[-1].clear()
                fragment = BeautifulSoup(render_inline_text(replacement), "html.parser")
                for child in list(fragment.contents):
                    bodies[-1].append(child)
        source_read = profile.get("source_read")
        paragraphs = source_section.find_all("p", recursive=False)
        if paragraphs and source_read:
            paragraphs[-1].clear()
            fragment = BeautifulSoup(render_inline_text(source_read), "html.parser")
            for child in list(fragment.contents):
                paragraphs[-1].append(child)

    for section_id, section_profile in profile["sections"].items():
        section = soup.select_one(f"section#{section_id}")
        if section is None:
            continue
        meta = section.find("div", class_="article-section__meta", recursive=False)
        prompt_note = section.find("p", class_="article-section__prompt", recursive=False)
        heading = section.find("h2", recursive=False)
        learning_card = section.find("aside", class_="learning-card")
        if meta is None or prompt_note is None or heading is None:
            continue
        heading.string = section_profile["heading"]
        prompt_text = strip_tags(prompt_note.get_text(" ", strip=True))
        dialogue_turns = section_profile.get("dialogue_turns") or synthetic_prompt_dialogue_turns(page, prompt_text)
        dialogue_html = render_dialogue_card(dialogue_turns, "") if dialogue_turns else ""
        list_html = "" if dialogue_turns else render_list_section(section_profile["items"])
        new_section_html = (
            f'<section class="{" ".join(section.get("class", []))}" id="{section.get("id", "")}">'
            f"{str(meta)}"
            f"{str(prompt_note)}"
            f"{str(heading)}"
            f"{render_paragraphs(section_profile['paragraphs'])}"
            f"{dialogue_html}"
            f"{list_html}"
            f"{str(learning_card) if learning_card else ''}"
            "</section>"
        )
        replace_with_fragment(section, new_section_html)

    synthesis = profile.get("synthesis")
    if synthesis:
        section = soup.select_one("section#synthesis")
        if section is not None:
            meta = section.find("div", class_="article-section__meta", recursive=False)
            heading = section.find("h2", recursive=False)
            learning_card = section.find("aside", class_="learning-card")
            if meta is not None and heading is not None:
                new_section_html = (
                    f'<section class="{" ".join(section.get("class", []))}" id="{section.get("id", "")}">'
                    f"{str(meta)}"
                    f"{str(heading)}"
                    f"{render_paragraphs(synthesis['paragraphs'])}"
                    f"{render_list_section(synthesis['items'])}"
                    f"{str(learning_card) if learning_card else ''}"
                    "</section>"
                )
                replace_with_fragment(section, new_section_html)

    return str(soup)


def clean_learning_cards(updated: str) -> str:
    soup = BeautifulSoup(updated, "html.parser")
    generic_prefixes = (
        "By the end, the reader should be able to say what difference ",
        "The exchange works only if its movement through ",
        "Track confidence calibration:",
        "Use (Gemini failed",
        "Ask what pressure this section makes hard to dodge:",
        "Use one concept as a tool: apply Philosophers or Philosophy",
        "Use some suggest that the notion",
        "Keep the page tied to a judgment a reader could actually use outside this one discussion.",
        "Keep the lived cost visible: the view matters only if it changes attention, practice, courage, or consolation.",
    )

    for learning_card in soup.select("aside.learning-card"):
        items = learning_card.select("li")
        for item in items:
            text = strip_tags(str(item))
            if any(text.startswith(prefix) for prefix in generic_prefixes):
                item.decompose()
        if not learning_card.select("li"):
            learning_card.decompose()

    return str(soup)


def clean_generic_paragraphs_globally(updated: str) -> str:
    soup = BeautifulSoup(updated, "html.parser")
    for paragraph in soup.find_all("p"):
        classes = paragraph.get("class") or []
        if "article-section__prompt" in classes:
            continue
        text = strip_tags(str(paragraph))
        if "The section should narrow the reader's attention toward the tension that actually needs investigation." in text:
            paragraph.decompose()
            continue
        if should_remove_paragraph(text):
            paragraph.decompose()
    for item in soup.find_all("li"):
        text = strip_tags(str(item))
        if should_remove_list_item(text):
            item.decompose()
    for learning_card in soup.select("aside.learning-card"):
        if not learning_card.select("li"):
            learning_card.decompose()
    return str(soup)


def final_batch_cleanup(updated: str) -> str:
    soup = BeautifulSoup(updated, "html.parser")

    for tag in soup.find_all(["p", "li"]):
        text = strip_tags(str(tag))
        if not text:
            continue
        if text.startswith("Keep ") and "That is what shows what the page is claiming" in text:
            tag.decompose()
            continue
        if "GEMINI:" in text or "Pushback for GEMINI:" in text:
            tag.decompose()
            continue
        if text.startswith("Track the movement in the exchange:") and "GEMINI" in text:
            tag.decompose()
            continue
        if text.startswith("Notice what changes if ") and "GEMINI" in text:
            tag.decompose()
            continue
        if text.startswith("Which of these threads matters most right now:"):
            tag.decompose()
            continue
        if "The archive depends on connection without careless merging." in text:
            tag.decompose()
            continue
        if "It is not just a polite way to stop talking." in text:
            tag.decompose()
            continue
        if "The links are not decoration; they show where the pressure continues." in text:
            tag.decompose()

    for learning_card in soup.select("aside.learning-card"):
        if not learning_card.select("li"):
            learning_card.decompose()

    for reading_list in soup.select("ol.reading-path-card__list, ul.reading-path-card__list"):
        if not reading_list.find_all("li", recursive=False):
            reading_list.decompose()

    for section in soup.select("section.article-section--prompt, section#synthesis"):
        previous_text = None
        for paragraph in list(section.find_all("p", recursive=False)):
            text = strip_tags(str(paragraph))
            if not text:
                continue
            if text == previous_text:
                paragraph.decompose()
                continue
            previous_text = text

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
    updated = clean_learning_cards(updated)
    updated = clean_generic_paragraphs_globally(updated)
    updated = final_batch_cleanup(updated)
    updated = SECTION_RE.sub(rewrite_section, updated)
    updated = clean_learning_cards(updated)
    updated = clean_generic_paragraphs_globally(updated)
    updated = final_batch_cleanup(updated)
    return updated


def clean_page(path: Path) -> bool:
    original = path.read_text()
    page_title_match = re.search(r"<h1>(?P<title>.*?)</h1>", original, re.DOTALL)
    page_title = strip_tags(page_title_match.group("title")) if page_title_match else path.parent.name
    page = page_dict_for_path(path, page_title)
    updated = clean_html(original, page, page_title)
    updated = polish_current_batch_philosopher_page(path, updated, page_title)
    updated = polish_special_batch_page(path, updated, page_title)
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
