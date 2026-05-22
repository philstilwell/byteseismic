(function () {
  const data = window.BYTESEISMIC_DATA;

  if (!data) {
    initQuizzes();
    return;
  }

  const isFile = window.location.protocol === "file:";
  const decodedPath = decodeURIComponent(window.location.pathname);
  const repoMarker = "/BYTESEISMIC/";
  const repoIndex = decodedPath.indexOf(repoMarker);
  const fileRoot = isFile && repoIndex !== -1 ? decodedPath.slice(0, repoIndex + repoMarker.length - 1) : "";
  const githubPrefix =
    window.location.hostname.endsWith("github.io") &&
    window.location.pathname.startsWith("/byteseismic/")
      ? "/byteseismic"
      : "";

  function href(path) {
    const normalized = path.startsWith("/") ? path : `/${path}`;

    if (isFile && fileRoot) {
      if (normalized === "/") {
        return `file://${fileRoot}/index.html`;
      }

      if (normalized.endsWith("/")) {
        return `file://${fileRoot}${normalized}index.html`;
      }

      return `file://${fileRoot}${normalized}`;
    }

    return `${githubPrefix}${normalized}`;
  }

  function escapeHtml(value) {
    return String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function homeAnchor(sectionId) {
    return `${href("/")}#section-${sectionId}`;
  }

  function currentSection() {
    return document.body.dataset.currentSection || "";
  }

  function currentPage() {
    return document.body.dataset.currentPage || "";
  }

  function countTree(nodes) {
    return (nodes || []).reduce(
      (total, node) => total + 1 + countTree(node.children || []),
      0,
    );
  }

  function fallbackTopicTree(section) {
    return (section.seedTopics || []).map((topic) => ({
      title: topic,
      path: data.topicPaths?.[topic] || "",
    }));
  }

  function sectionTree(section) {
    return section.topicTree?.length ? section.topicTree : fallbackTopicTree(section);
  }

  function hasCurrentDescendant(node, activePage) {
    if (!node || !activePage) {
      return false;
    }

    if (node.path === activePage) {
      return true;
    }

    return (node.children || []).some((child) => hasCurrentDescendant(child, activePage));
  }

  function renderOutlineTree(nodes, activePage, fallbackTarget, level = 0) {
    if (!nodes?.length) {
      return "";
    }

    const listClass = level === 0 ? "outline-topic-tree" : "outline-subtree";
    const items = nodes
      .map((node) => {
        const hasChildren = Boolean(node.children?.length);
        const target = node.path ? href(node.path) : fallbackTarget;
        const isCurrent = node.path === activePage;
        const containsCurrent = hasCurrentDescendant(node, activePage);

        if (hasChildren) {
          const nestedCount = countTree(node.children);
          const jumpLink = node.path
            ? `
                <a class="outline-node__jump${isCurrent ? " is-current" : ""}" href="${target}">
                  Open ${node.title}
                </a>
              `
            : "";

          return `
            <li class="outline-tree__item outline-tree__item--branch">
              <details class="outline-branch"${containsCurrent ? " open" : ""}>
                <summary>
                  <span class="outline-branch__summary">
                    <span class="outline-branch__label">${node.title}</span>
                    <span class="outline-branch__count">${nestedCount}</span>
                  </span>
                </summary>
                <div class="outline-branch__body">
                  ${jumpLink}
                  ${renderOutlineTree(node.children, activePage, fallbackTarget, level + 1)}
                </div>
              </details>
            </li>
          `;
        }

        if (!target) {
          return `
            <li class="outline-tree__item outline-tree__item--leaf">
              <span class="outline-node__text">${node.title}</span>
            </li>
          `;
        }

        return `
          <li class="outline-tree__item outline-tree__item--leaf">
            <a class="outline-node__link${isCurrent ? " is-current" : ""}" href="${target}">
              ${node.title}
            </a>
          </li>
        `;
      })
      .join("");

    return `<ul class="${listClass}">${items}</ul>`;
  }

  function renderStructurePreview(section) {
    const tree = sectionTree(section);
    const items = tree
      .slice(0, 6)
      .map((node) => {
        const target = node.path ? href(node.path) : sectionTarget(section);
        const nestedCount = countTree(node.children || []);
        const meta = nestedCount ? `${nestedCount} nested` : "leaf page";

        return `
          <li>
            <a href="${target}">${node.title}</a>
            <span class="seed-list__meta">${meta}</span>
          </li>
        `;
      })
      .join("");

    return `<ul class="seed-list seed-list--preview">${items}</ul>`;
  }

  function topicTarget(section, topic) {
    const builtPath = data.topicPaths?.[topic];
    return builtPath ? href(builtPath) : homeAnchor(section.id);
  }

  function sectionTarget(section) {
    return section.samplePath ? href(section.samplePath) : homeAnchor(section.id);
  }

  function isUsefulTag(tag) {
    const normalized = String(tag || "").trim().toLowerCase();
    const stopTags = new Set([
      "1",
      "2",
      "3",
      "4",
      "5",
      "with",
      "what",
      "where",
      "when",
      "from",
      "that",
      "this",
      "into",
      "core",
    ]);
    if (normalized === "ai") {
      return true;
    }
    return normalized.length >= 3 && !stopTags.has(normalized) && !/^\d[\d-]*$/.test(normalized);
  }

  function tagCount(tag) {
    if (data.tagCounts?.[tag]) {
      return data.tagCounts[tag];
    }

    return (data.taggedPages || []).filter((page) => (page.tags || []).includes(tag)).length;
  }

  function renderTagButton(tag, extraClass = "") {
    const count = tagCount(tag);
    const label = escapeHtml(tag);
    const className = `tag-chip${extraClass ? ` ${extraClass}` : ""}`;
    const countLabel = count ? `<span class="tag-chip__count">${count}</span>` : "";

    return `
      <button class="${className}" type="button" data-tag-filter="${label}" aria-label="Show pages tagged ${label}">
        <span>${label}</span>${countLabel}
      </button>
    `;
  }

  function slugifyTag(tag) {
    return String(tag || "")
      .trim()
      .toLowerCase()
      .replace(/&/g, " and ")
      .replace(/["'`]+/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "") || "tag";
  }

  function renderTagLink(tag, extraClass = "") {
    const count = tagCount(tag);
    const label = escapeHtml(tag);
    const className = `tag-chip${extraClass ? ` ${extraClass}` : ""}`;
    const countLabel = count ? `<span class="tag-chip__count">${count}</span>` : "";
    const path = data.tagPages?.[tag] || `/tags/${slugifyTag(tag)}/`;

    return `
      <a class="${className}" href="${href(path)}" aria-label="Open tag page for ${label}">
        <span>${label}</span>${countLabel}
      </a>
    `;
  }

  function renderNav() {
    const mounts = document.querySelectorAll("[data-site-nav]");
    if (!mounts.length) {
      return;
    }

    const activeSection = currentSection();
    const list = data.sections
      .map((section) => {
        const isActive = section.id === activeSection ? " is-active" : "";
        const count = section.topicCount || countTree(sectionTree(section));
        const target =
          document.body.dataset.pageType === "home" ? `#section-${section.id}` : sectionTarget(section);

        return `
          <li class="site-nav__item${isActive}">
            <a href="${target}">
              <span class="site-nav__name">${section.name}</span>
              <span class="site-nav__meta">${count} topics</span>
            </a>
          </li>
        `;
      })
      .join("");

    mounts.forEach((mount) => {
      mount.innerHTML = `
        <div class="site-nav">
          <p class="site-nav__eyebrow">Inquiry Map</p>
          <h2 class="site-nav__title">Branch Guide</h2>
          <p class="site-nav__intro">
            A condensed guide to the inquiry branches, including nested paths where the visible hierarchy goes deeper.
          </p>
          <ul class="site-nav__list">${list}</ul>
        </div>
      `;
    });
  }

  function renderArticleOutline() {
    const mount = document.querySelector("[data-article-outline]");
    if (!mount) {
      return;
    }

    const activeSection = currentSection();
    const activePage = currentPage();
    const groups = data.sections
      .map((section) => {
        const open = section.id === activeSection ? " open" : "";
        const tree = sectionTree(section);
        const count = section.topicCount || countTree(tree);
        const topics = renderOutlineTree(tree, activePage, sectionTarget(section));

        return `
          <details class="outline-group"${open}>
            <summary>
              <span class="outline-group__name">${section.name}</span>
              <span class="outline-group__count">${count}</span>
            </summary>
            <div class="outline-group__body">
              <a class="outline-group__jump" href="${sectionTarget(section)}">${section.summary}</a>
              ${topics}
            </div>
          </details>
        `;
      })
      .join("");

    mount.innerHTML = `
      <div class="outline-card">
        <div class="outline-card__header">
          <p class="eyebrow">Branch Hierarchy</p>
          <h2>Condensed branch view</h2>
          <p>
            Each branch opens into its own nested path. Sub-branches get their own compact accordions so the larger inquiry network stays legible.
          </p>
        </div>
        <div class="outline-accordion">${groups}</div>
      </div>
    `;
  }

  function renderStructureGrid() {
    const mount = document.querySelector("[data-section-grid]");
    if (!mount) {
      return;
    }

    mount.innerHTML = data.sections
      .map((section) => {
        const sampleLink = section.samplePath
          ? `<a class="text-link" href="${href(section.samplePath)}">Open branch entry</a>`
          : `<span class="muted-label">Branch entry coming next</span>`;
        const branchGuideLink = section.branchGuidePath
          ? `<a class="text-link" href="${href(section.branchGuidePath)}">Open branch guide</a>`
          : "";
        const tags = section.futureTags
          .filter((tag) => tagCount(tag) > 0 || section.id === "philosophers")
          .map((tag) => renderTagLink(tag))
          .join("");
        const tensions = (section.coreTensions || [])
          .slice(0, 4)
          .map((item) => `<li>${escapeHtml(item)}</li>`)
          .join("");

        return `
          <article class="structure-card" id="section-card-${escapeHtml(section.id)}" data-section-anchor="section-${escapeHtml(section.id)}">
            <div class="structure-card__header">
              <p class="eyebrow">${escapeHtml(section.name)}</p>
              <h3>${escapeHtml(section.summary)}</h3>
              <p>${escapeHtml(section.editorialIntro || "")}</p>
            </div>
            <div class="structure-card__body">
              <div>
                <p class="mini-label">Reader route</p>
                <p>${escapeHtml(section.route || "")}</p>
              </div>
              <div>
                <p class="mini-label">Visible top-level paths in this branch</p>
                ${renderStructurePreview(section)}
              </div>
              <div>
                <p class="mini-label">Core tensions</p>
                <ul class="seed-list">${tensions}</ul>
              </div>
              <div>
                <p class="mini-label">Starter tags for future expansion</p>
                <div class="tag-row">${tags}</div>
              </div>
            </div>
            <div class="structure-card__footer">${branchGuideLink}${sampleLink}</div>
          </article>
        `;
      })
      .join("");
  }

  function renderTagCloud() {
    const mount = document.querySelector("[data-tag-cloud]");
    if (!mount) {
      return;
    }

    const tags = (data.landingTags?.length
      ? data.landingTags
      : [...new Set(data.sections.flatMap((section) => section.futureTags || []))]
    ).filter(isUsefulTag).sort();
    mount.innerHTML = tags
      .map(
        (tag) => `
          ${renderTagButton(tag, "tag-chip--large")}
        `,
      )
      .join("");
  }

  function renderFeaturedPages() {
    const mount = document.querySelector("[data-featured-pages]");
    if (!mount) {
      return;
    }

    mount.innerHTML = data.featuredPages
      .map((page) => {
        const tags = page.tags
          .map((tag) => renderTagLink(tag))
          .join("");

        return `
          <article class="feature-card">
            <p class="eyebrow">${escapeHtml(page.section)}</p>
            <h3>${escapeHtml(page.title)}</h3>
            <p>${escapeHtml(page.summary)}</p>
            <div class="tag-row">${tags}</div>
            <a class="button button--ghost" href="${href(page.path)}">Read the page</a>
          </article>
        `;
      })
      .join("");
  }

  function renderGuidedRoutes() {
    const mount = document.querySelector("[data-guided-routes]");
    if (!mount) {
      return;
    }

    mount.innerHTML = (data.guidedReadingPaths || [])
      .map((route) => {
        const steps = (route.steps || [])
          .map(
            (step) => `
              <li>
                <a href="${href(step.path)}">${escapeHtml(step.title)}</a>
                <span>${escapeHtml(step.reason)}</span>
              </li>
            `,
          )
          .join("");

        return `
          <article class="route-card">
            <p class="eyebrow">${escapeHtml(route.audience)}</p>
            <h3>${escapeHtml(route.title)}</h3>
            <p>${escapeHtml(route.summary)}</p>
            <ol class="route-steps">${steps}</ol>
          </article>
        `;
      })
      .join("");
  }

  function renderGlossaryPreview() {
    const mount = document.querySelector("[data-glossary-preview]");
    if (!mount) {
      return;
    }

    mount.innerHTML = (data.glossaryTerms || [])
      .slice()
      .sort((a, b) => a.term.localeCompare(b.term))
      .slice(0, 9)
      .map((entry) => {
        const links = (entry.paths || [])
          .slice(0, 2)
          .map((path) => {
            const label = path
              .replace(/^\/|\/$/g, "")
              .split("/")
              .pop()
              .replace(/-/g, " ");
            return `<a class="text-link" href="${href(path)}">${escapeHtml(label)}</a>`;
          })
          .join("");
        const tags = (entry.tags || []).map((tag) => renderTagLink(tag)).join("");

        return `
          <article class="glossary-card">
            <p class="eyebrow">${escapeHtml(entry.branch)}</p>
            <h3>${escapeHtml(entry.term)}</h3>
            <p>${escapeHtml(entry.definition)}</p>
            <div class="glossary-card__links">${links}</div>
            <div class="tag-row">${tags}</div>
          </article>
        `;
      })
      .join("");
  }

  function renderTagResults(tag) {
    const resultMount = document.querySelector("[data-tag-results]");
    if (!resultMount || !tag) {
      return;
    }

    const pages = (data.taggedPages || data.featuredPages || [])
      .filter((page) => (page.tags || []).includes(tag))
      .sort((a, b) => a.section.localeCompare(b.section) || a.title.localeCompare(b.title));

    const sections = [...new Set(pages.map((page) => page.section))];
    const groups = sections
      .map((section) => {
        const sectionPages = pages.filter((page) => page.section === section).slice(0, 14);
        const items = sectionPages
          .map(
            (page) => `
              <li>
                <a href="${href(page.path)}">${escapeHtml(page.title)}</a>
                <span>${escapeHtml(page.section)}</span>
              </li>
            `,
          )
          .join("");
        const overflow = pages.filter((page) => page.section === section).length - sectionPages.length;

        return `
          <details class="tag-results__group" open>
            <summary>
              <span>${escapeHtml(section)}</span>
              <span>${sectionPages.length}${overflow > 0 ? `+${overflow}` : ""}</span>
            </summary>
            <ul class="archive-year-list tag-results__list">
              ${items}
            </ul>
          </details>
        `;
      })
      .join("");

    resultMount.innerHTML = `
      <div class="tag-results__header">
        <p class="mini-label">Selected tag</p>
        <h3>${escapeHtml(tag)}</h3>
        <p>${pages.length} page${pages.length === 1 ? "" : "s"} use this tag.</p>
      </div>
      <div class="tag-results__groups">
        ${groups || "<p class=\"muted-label\">No pages use this tag yet.</p>"}
      </div>
    `;
  }

  function openTagDiscoveryPanel() {
    const tagPanel = document.querySelector("#tag-discovery");
    if (!tagPanel) {
      return null;
    }

    const accordion = tagPanel.closest("[data-exclusive-accordion]");
    accordion?.querySelectorAll(".home-panel[open]").forEach((panel) => {
      if (panel !== tagPanel) {
        panel.removeAttribute("open");
      }
    });
    tagPanel.setAttribute("open", "");
    return tagPanel;
  }

  function selectTag(tag, { openPanel = false, scroll = false } = {}) {
    if (!tag) {
      return;
    }

    document.querySelectorAll("[data-tag-filter]").forEach((candidate) => {
      candidate.classList.toggle("is-active", candidate.dataset.tagFilter === tag);
    });
    renderTagResults(tag);

    const tagPanel = openPanel ? openTagDiscoveryPanel() : null;
    const results = document.querySelector("[data-tag-results]");
    if (scroll) {
      (results || tagPanel)?.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }
  }

  function renderSearchResults(query) {
    const resultMount = document.querySelector("[data-page-search-results]");
    if (!resultMount) {
      return;
    }

    const normalized = String(query || "").trim().toLowerCase();
    if (normalized.length < 2) {
      resultMount.innerHTML = '<p class="muted-label">Type at least two characters to search the inquiry network.</p>';
      return;
    }

    const terms = normalized.split(/\s+/).filter(Boolean);
    const pages = (data.taggedPages || [])
      .map((page) => {
        const haystack = [
          page.title,
          page.section,
          page.summary,
          ...(page.tags || []),
        ].join(" ").toLowerCase();
        const score = terms.reduce((total, term) => {
          if (page.title.toLowerCase().includes(term)) return total + 8;
          if ((page.tags || []).some((tag) => tag.toLowerCase().includes(term))) return total + 4;
          if (page.section.toLowerCase().includes(term)) return total + 2;
          return haystack.includes(term) ? total + 1 : total;
        }, 0);
        return { page, score };
      })
      .filter((entry) => entry.score > 0)
      .sort((a, b) => b.score - a.score || a.page.title.localeCompare(b.page.title))
      .slice(0, 18);

    const items = pages
      .map(
        ({ page }) => `
          <li>
            <a href="${href(page.path)}">${escapeHtml(page.title)}</a>
            <span>${escapeHtml(page.section)}</span>
          </li>
        `,
      )
      .join("");

    resultMount.innerHTML = `
      <div class="tag-results__header">
        <p class="mini-label">Search results</p>
        <h3>${escapeHtml(query)}</h3>
        <p>${pages.length} close match${pages.length === 1 ? "" : "es"} shown.</p>
      </div>
      <ul class="archive-year-list tag-results__list">
        ${items || "<li><span>No close matches. Try a broader term.</span></li>"}
      </ul>
    `;
  }

  function initPageSearch() {
    const input = document.querySelector("[data-page-search-input]");
    const clear = document.querySelector("[data-page-search-clear]");
    const resultMount = document.querySelector("[data-page-search-results]");
    if (!input || !resultMount) {
      return;
    }

    renderSearchResults("");
    input.addEventListener("input", () => renderSearchResults(input.value));
    clear?.addEventListener("click", () => {
      input.value = "";
      input.focus();
      renderSearchResults("");
    });
  }

  function initTagFilters() {
    document.addEventListener("click", (event) => {
      const trigger = event.target.closest("[data-tag-filter]");
      if (!trigger) {
        return;
      }

      const tag = trigger.dataset.tagFilter;
      selectTag(tag, {
        openPanel: !document.querySelector("#tag-discovery")?.contains(trigger),
        scroll: true,
      });
    });

    const requestedTag = new URLSearchParams(window.location.search).get("tag");
    if (requestedTag) {
      selectTag(requestedTag, { openPanel: true, scroll: window.location.hash === "#tag-discovery" });
      return;
    }

    const firstTag = document.querySelector("[data-tag-cloud] [data-tag-filter]");
    if (firstTag) {
      firstTag.classList.add("is-active");
      renderTagResults(firstTag.dataset.tagFilter);
    }
  }

  function initExclusiveAccordions() {
    document.querySelectorAll("[data-exclusive-accordion]").forEach((group) => {
      group.addEventListener("toggle", (event) => {
        const opened = event.target;
        if (!(opened instanceof HTMLDetailsElement) || !opened.open) {
          return;
        }

        group.querySelectorAll("details[open]").forEach((details) => {
          if (details !== opened) {
            details.open = false;
          }
        });
      }, true);
    });
  }

  function revealHashTarget() {
    const hash = decodeURIComponent(window.location.hash || "");
    if (!hash || hash === "#") {
      return;
    }

    const hashId = hash.slice(1);
    document.querySelectorAll(".structure-card.is-anchor-target").forEach((card) => {
      card.classList.remove("is-anchor-target");
    });

    const sectionCard = document.querySelector(`[data-section-anchor="${CSS.escape(hashId)}"]`);
    const target = sectionCard || document.getElementById(hashId);
    if (!target) {
      return;
    }
    sectionCard?.classList.add("is-anchor-target");

    const containingPanel = target.closest(".home-panel");
    if (containingPanel) {
      const accordion = containingPanel.closest("[data-exclusive-accordion]");
      accordion?.querySelectorAll(".home-panel[open]").forEach((panel) => {
        if (panel !== containingPanel) {
          panel.removeAttribute("open");
        }
      });
      containingPanel.setAttribute("open", "");
    }

    window.requestAnimationFrame(() => {
      window.setTimeout(() => {
        const block = target.classList?.contains("article-section") ? "start" : "center";
        target.scrollIntoView({ behavior: "smooth", block });
      }, 60);
    });
  }

  function initQuizzes() {
    document.querySelectorAll("[data-quiz-item]").forEach((item) => {
      const reset = item.querySelector("[data-quiz-reset]");
      const options = item.querySelectorAll("button.quiz-option[data-feedback]");

      if (reset) {
        reset.addEventListener("click", () => {
          item.querySelectorAll(".quiz-choice__input").forEach((input) => {
            input.checked = false;
          });

          options.forEach((candidate) => {
            candidate.classList.remove("is-selected", "is-correct", "is-incorrect");
            candidate.setAttribute("aria-pressed", "false");
          });

          const feedback = item.querySelector(".quiz-feedback");
          if (feedback && options.length) {
            feedback.textContent = "";
            feedback.classList.remove("is-correct", "is-incorrect");
          }

          item.classList.remove("is-answered");
        });
      }

      if (!options.length) {
        return;
      }

      const feedback = item.querySelector(".quiz-feedback");

      options.forEach((option) => {
        option.addEventListener("click", () => {
          const isCorrect = option.dataset.correct === "true";

          options.forEach((candidate) => {
            candidate.classList.remove("is-selected", "is-correct", "is-incorrect");
            candidate.setAttribute("aria-pressed", "false");
          });

          option.classList.add("is-selected", isCorrect ? "is-correct" : "is-incorrect");
          option.setAttribute("aria-pressed", "true");
          item.classList.add("is-answered");

          if (feedback) {
            feedback.textContent = option.dataset.feedback || "";
            feedback.classList.toggle("is-correct", isCorrect);
            feedback.classList.toggle("is-incorrect", !isCorrect);
          }
        });
      });
    });
  }

  renderNav();
  renderArticleOutline();
  renderStructureGrid();
  renderTagCloud();
  renderFeaturedPages();
  renderGuidedRoutes();
  renderGlossaryPreview();
  initPageSearch();
  initTagFilters();
  initExclusiveAccordions();
  revealHashTarget();
  window.addEventListener("hashchange", revealHashTarget);
  initQuizzes();
})();
