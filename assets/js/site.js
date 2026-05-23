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

  function normalizeSitePath(path) {
    let normalized = String(path || "/").trim();

    if (!normalized) {
      return "/";
    }

    if (normalized.startsWith(githubPrefix) && githubPrefix) {
      normalized = normalized.slice(githubPrefix.length) || "/";
    }

    normalized = normalized.replace(/\/index\.html$/i, "/");
    if (!normalized.startsWith("/")) {
      normalized = `/${normalized}`;
    }
    normalized = normalized.replace(/\/{2,}/g, "/");
    if (!normalized.endsWith("/") && !/\.[a-z0-9]+$/i.test(normalized)) {
      normalized += "/";
    }

    return normalized || "/";
  }

  function sitePathFromHref(rawHref) {
    if (!rawHref) {
      return "";
    }

    try {
      const parsed = new URL(rawHref, window.location.href);
      let path = decodeURIComponent(parsed.pathname || "/");

      if (isFile && fileRoot && path.startsWith(fileRoot)) {
        path = path.slice(fileRoot.length) || "/";
      } else if (githubPrefix && path.startsWith(githubPrefix)) {
        path = path.slice(githubPrefix.length) || "/";
      }

      return normalizeSitePath(path);
    } catch (_error) {
      return "";
    }
  }

  function currentSection() {
    return document.body.dataset.currentSection || "";
  }

  function currentPage() {
    if (document.body.dataset.currentPage) {
      return document.body.dataset.currentPage;
    }

    let path = decodedPath || "/";
    if (isFile && fileRoot && path.startsWith(fileRoot)) {
      path = path.slice(fileRoot.length) || "/";
    } else if (githubPrefix && path.startsWith(githubPrefix)) {
      path = path.slice(githubPrefix.length) || "/";
    }

    return normalizeSitePath(path);
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

  function findTopicContext(nodes, targetPath, trail = []) {
    for (const node of nodes || []) {
      const nextTrail = [...trail, node];
      if (node.path === targetPath) {
        return { node, trail: nextTrail, siblings: nodes };
      }

      const childMatch = findTopicContext(node.children || [], targetPath, nextTrail);
      if (childMatch) {
        return childMatch;
      }
    }

    return null;
  }

  function uniqueByPath(items) {
    const seen = new Set();
    return (items || []).filter((item) => {
      const key = item?.path || item?.href;
      if (!key || seen.has(key)) {
        return false;
      }
      seen.add(key);
      return true;
    });
  }

  function cleanInlineText(value) {
    return String(value || "").replace(/\s+/g, " ").trim();
  }

  function slugifyText(value) {
    return String(value || "")
      .trim()
      .toLowerCase()
      .replace(/&/g, " and ")
      .replace(/["'`]+/g, "")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");
  }

  function currentPageEntry() {
    return (data.taggedPages || []).find((page) => page.path === currentPage()) || null;
  }

  function directSectionHeading(section) {
    return Array.from(section.children || []).find((child) => /^H[23]$/.test(child.tagName || "")) || null;
  }

  function articleSectionLinks() {
    const seen = new Set();
    return [...document.querySelectorAll(".article-body > .article-section[id]")]
      .filter((section) => {
        if (!section.id || seen.has(section.id)) {
          return false;
        }
        seen.add(section.id);
        return true;
      })
      .map((section, index) => {
        const heading = directSectionHeading(section);
        const title = cleanInlineText(heading?.textContent || section.id.replace(/-/g, " "));
        const metaEyebrow = cleanInlineText(section.querySelector(".article-section__meta .eyebrow")?.textContent || "");
        return {
          id: section.id,
          title,
          meta: metaEyebrow,
          index,
          node: section,
        };
      });
  }

  function ensureAnchorId(node, index, prefix = "section") {
    if (!node) {
      return "";
    }

    if (node.id) {
      return node.id;
    }

    const heading =
      directSectionHeading(node)
      || node.querySelector(":scope > .section-heading h2, :scope > .outline-card__header h2, :scope > h2, :scope > h3, :scope > article h3");
    const label = cleanInlineText(heading?.textContent || node.dataset.sectionAnchor || "");
    let id = slugifyText(label) || `${prefix}-${index + 1}`;

    if (document.getElementById(id)) {
      id = `${id}-${index + 1}`;
    }

    node.id = id;
    return id;
  }

  function sectionMetaLabel(node) {
    if (!node) {
      return "";
    }

    if (node.classList.contains("home-panel")) {
      const homeLabel = cleanInlineText(node.querySelector(":scope > summary .eyebrow")?.textContent || "");
      if (homeLabel) {
        return homeLabel;
      }
      return "Home panel";
    }

    const explicit =
      node.querySelector(":scope > .eyebrow, :scope > .mini-label, :scope > .learning-card__title, :scope > .section-heading .eyebrow")
      || node.querySelector(":scope > .structure-card__header .eyebrow, :scope > .route-card .eyebrow, :scope > .glossary-card .eyebrow");
    const text = cleanInlineText(explicit?.textContent || "");
    if (text) {
      return text;
    }

    if (node.classList.contains("route-card")) return "Reading route";
    if (node.classList.contains("glossary-card")) return "Glossary";
    if (node.classList.contains("structure-card")) return "Branch";
    if (node.classList.contains("feature-card")) return "Featured page";
    if (node.classList.contains("content-card")) return "Section";

    return "";
  }

  function stackSectionLinks() {
    const stack = document.querySelector(".article-stack");
    if (!stack) {
      return [];
    }

    const groups = Array.from(stack.children).filter((node) => node instanceof HTMLElement && !node.matches(".context-rail-slot"));
    const sections = [];

    groups.forEach((node) => {
      if (node.matches(".route-grid, .glossary-grid, .structure-grid, .feature-grid, .taxonomy-grid")) {
        sections.push(...Array.from(node.querySelectorAll(":scope > article, :scope > section")));
      } else if (node.matches(".article-body")) {
        sections.push(...Array.from(node.querySelectorAll(":scope > .article-section")));
      } else if (node.matches("section, article")) {
        sections.push(node);
      }
    });

    const seen = new Set();
    return sections
      .filter((node) => {
        if (!(node instanceof HTMLElement) || seen.has(node)) {
          return false;
        }
        seen.add(node);
        return true;
      })
      .map((node, index) => {
        const id = ensureAnchorId(node, index, "panel");
        const heading =
          directSectionHeading(node)
          || node.querySelector(":scope > .section-heading h2, :scope > .outline-card__header h2, :scope > h2, :scope > h3");
        const title = cleanInlineText(heading?.textContent || id.replace(/-/g, " "));
        return {
          id,
          title,
          meta: sectionMetaLabel(node) || `Section ${index + 1}`,
          index,
          node,
        };
      })
      .filter((entry) => entry.title);
  }

  function homeSectionLinks() {
    const panels = Array.from(document.querySelectorAll(".home-accordion > .home-panel"));
    if (!panels.length) {
      return [];
    }

    return panels
      .map((panel, index) => {
        const id = ensureAnchorId(panel, index, "home-panel");
        const heading = panel.querySelector(":scope > summary h2");
        const title = cleanInlineText(heading?.textContent || id.replace(/-/g, " "));
        return {
          id,
          title,
          meta: sectionMetaLabel(panel) || `Panel ${index + 1}`,
          index,
          node: panel,
        };
      })
      .filter((entry) => entry.title);
  }

  function pageSectionLinks() {
    if (document.body.dataset.pageType === "home") {
      return homeSectionLinks();
    }

    const articleLinks = articleSectionLinks();
    return articleLinks.length ? articleLinks : stackSectionLinks();
  }

  function breadcrumbTrail(pageTitle) {
    const trail = [];
    document.querySelectorAll(".breadcrumbs a, .breadcrumbs span").forEach((node) => {
      const label = cleanInlineText(node.textContent || "");
      if (!label || label === "/") {
        return;
      }

      if (node.tagName === "A") {
        trail.push({
          label,
          href: node.getAttribute("href") || node.href,
        });
        return;
      }

      trail.push({ label });
    });

    if (!trail.length && document.body.dataset.pageType === "home") {
      return [{ label: "Home" }];
    }

    if (pageTitle && trail.at(-1)?.label !== pageTitle) {
      trail.push({ label: pageTitle });
    }

    return trail;
  }

  function renderTrail(trail) {
    return trail
      .map((item, index) => {
        const label = escapeHtml(item.label);
        const node = item.href
          ? `<a href="${escapeHtml(item.href)}">${label}</a>`
          : `<span${index === trail.length - 1 ? ' aria-current="page"' : ""}>${label}</span>`;
        const separator = index < trail.length - 1 ? '<span class="context-rail__trail-sep" aria-hidden="true">/</span>' : "";
        return `${node}${separator}`;
      })
      .join("");
  }

  function ensureContextRailMount() {
    const pageShell = document.querySelector(".page-shell");
    if (pageShell && !pageShell.id) {
      pageShell.id = "top";
    }

    let mount = document.querySelector("[data-context-rail]");
    if (mount) {
      return mount;
    }

    const articleLayout = document.querySelector(".article-layout");
    const articleStack = articleLayout?.querySelector(":scope > .article-stack");
    if (articleLayout && articleStack) {
      articleLayout.classList.remove("article-layout--single");
      articleLayout.classList.add("article-layout--with-rail");

      mount = document.createElement("aside");
      mount.className = "context-rail-slot";
      mount.setAttribute("data-context-rail", "");
      articleStack.insertAdjacentElement("afterend", mount);
      return mount;
    }

    const homeLayout = document.querySelector(".layout--home");
    const homeContent = homeLayout?.querySelector(":scope > .content");
    if (homeLayout && homeContent) {
      homeLayout.classList.add("layout--with-rail");

      mount = document.createElement("aside");
      mount.className = "context-rail-slot";
      mount.setAttribute("data-context-rail", "");
      homeContent.insertAdjacentElement("afterend", mount);
      return mount;
    }

    return null;
  }

  function nearestContextLabel(anchor) {
    const container = anchor.closest(".content-card, .article-section, .route-card, .glossary-card, .structure-card, .feature-card, .home-panel");
    return sectionMetaLabel(container) || "From this page";
  }

  function contentLinksFallback(limit = 7) {
    const root = document.querySelector(".article-stack") || document.querySelector(".content");
    if (!root) {
      return [];
    }

    const items = [];
    root.querySelectorAll("a[href]").forEach((anchor) => {
      if (anchor.closest(".breadcrumbs") || anchor.closest("[data-context-rail]")) {
        return;
      }

      const rawHref = anchor.getAttribute("href");
      if (!rawHref || rawHref.startsWith("#")) {
        return;
      }

      const path = sitePathFromHref(anchor.href || rawHref);
      if (!path || path === currentPage()) {
        return;
      }

      const title = cleanInlineText(anchor.textContent || "");
      if (title.length < 2) {
        return;
      }

      items.push({
        title,
        path,
        href: rawHref,
        meta: nearestContextLabel(anchor),
      });
    });

    return uniqueByPath(items).slice(0, limit);
  }

  function relatedBranchLinks(section, activePage) {
    const items = [];
    const context = findTopicContext(sectionTree(section), activePage);

    if (context) {
      const parent = context.trail.at(-2);
      if (parent?.path) {
        items.push({
          title: parent.title,
          path: parent.path,
          href: href(parent.path),
          meta: "up one level",
        });
      }

      (context.node.children || []).forEach((child) => {
        items.push({
          title: child.title,
          path: child.path,
          href: href(child.path),
          meta: "nested from here",
        });
      });

      (context.siblings || [])
        .filter((candidate) => candidate.path && candidate.path !== activePage)
        .forEach((candidate) => {
          items.push({
            title: candidate.title,
            path: candidate.path,
            href: href(candidate.path),
            meta: "same branch",
          });
        });
    }

    (data.taggedPages || [])
      .filter((page) => page.path !== activePage && page.section === section.name)
      .slice(0, 10)
      .forEach((page) => {
        items.push({
          title: page.title,
          path: page.path,
          href: href(page.path),
          meta: "same branch page",
        });
      });

    return uniqueByPath(items).slice(0, 7);
  }

  function renderContextRail() {
    const mount = ensureContextRailMount();
    if (!mount) {
      return;
    }

    const isHomePage = document.body.dataset.pageType === "home";
    const section = data.sections.find((entry) => entry.id === currentSection());
    const page = currentPageEntry();
    const pageTitle = cleanInlineText(document.querySelector(".hero h1")?.textContent || page?.title || "");
    const sectionLinks = pageSectionLinks();
    const relatedLinks = section && page
      ? relatedBranchLinks(section, currentPage())
      : contentLinksFallback();
    const tags = (page?.tags || []).filter(isUsefulTag).slice(0, 6);
    const trail = breadcrumbTrail(pageTitle);
    const currentPath = currentPage();
    const activeSection = sectionLinks[0];
    const homeActions = isHomePage
      ? [
          { type: "button", action: "search", label: "Search" },
          { href: "#orientation", label: "Orientation" },
          { href: "#branch-guide", label: "Branch guide" },
          { href: "#tag-discovery", label: "Tag discovery" },
          { href: "#featured-pages", label: "Featured pages" },
          { href: "#top", label: "Page top" },
        ]
      : [];
    const pageActions = !isHomePage
      ? [
          { type: "button", action: "search", label: "Search" },
          section?.branchGuidePath && section.branchGuidePath !== currentPath ? { href: href(section.branchGuidePath), label: "Branch guide" } : null,
          section?.samplePath && section.branchGuidePath === currentPath ? { href: href(section.samplePath), label: "Branch entry" } : null,
          currentPath !== "/" ? { href: href("/"), label: "Home" } : null,
          { href: "#top", label: "Page top" },
          document.getElementById("future-branches") ? { href: "#future-branches", label: "Future branches" } : null,
        ].filter(Boolean)
      : [];
    const actionList = (isHomePage ? homeActions : pageActions)
      .filter((entry) => !entry.href || !entry.href.startsWith("#") || document.querySelector(entry.href))
      .map((entry) => {
        if (entry.type === "button" && entry.action === "search") {
          return '<button class="context-rail__action" type="button" data-open-site-search>Search</button>';
        }
        return `<a class="context-rail__action" href="${escapeHtml(entry.href)}">${escapeHtml(entry.label)}</a>`;
      })
      .join("");

    const sectionList = sectionLinks
      .map(
        (entry) => `
          <li>
            <a href="#${escapeHtml(entry.id)}" data-context-section-link="${escapeHtml(entry.id)}">
              <span class="context-rail__link-title">${escapeHtml(entry.title)}</span>
              <span class="context-rail__link-meta">${escapeHtml(entry.meta || `Section ${entry.index + 1}`)}</span>
            </a>
          </li>
        `,
      )
      .join("");

    const relatedList = relatedLinks.length
      ? relatedLinks
          .map(
            (entry) => `
              <li>
                <a href="${escapeHtml(entry.href || href(entry.path))}">
                  <span class="context-rail__link-title">${escapeHtml(entry.title)}</span>
                  <span class="context-rail__link-meta">${escapeHtml(entry.meta)}</span>
                </a>
              </li>
            `,
          )
          .join("")
      : '<li class="context-rail__empty">No nearby branch links yet.</li>';

    const tagList = tags.length
      ? tags.map((tag) => renderTagLink(tag)).join("")
      : '<p class="context-rail__empty">No discovery tags on this page yet.</p>';

    mount.innerHTML = `
      <div class="context-rail">
        <details class="context-rail__shell" open>
          <summary class="context-rail__mobile-summary">
            <div class="context-rail__mobile-main">
              <span class="mini-label">You are here</span>
              <span class="context-rail__mobile-trail">${renderTrail(trail)}</span>
              <a class="context-rail__mobile-active" href="#${escapeHtml(activeSection?.id || "")}" data-context-mobile-active-link>
                ${escapeHtml(activeSection?.title || pageTitle)}
              </a>
            </div>
            <span class="context-rail__mobile-cue" aria-hidden="true">+</span>
          </summary>
          <div class="context-rail__body">
            <div class="context-rail__header">
              <p class="mini-label">You are here</p>
              <div class="context-rail__trail">${renderTrail(trail)}</div>
              <h2 class="context-rail__title">${escapeHtml(pageTitle)}</h2>
              <div class="context-rail__status">
                <span class="context-rail__status-label">Now reading</span>
                <a class="context-rail__active-link" href="#${escapeHtml(activeSection?.id || "")}" data-context-active-link>
                  ${escapeHtml(activeSection?.title || pageTitle)}
                </a>
                <span class="context-rail__status-meta" data-context-active-meta>
                  ${sectionLinks.length ? `Section 1 of ${sectionLinks.length}` : "Top of page"}
                </span>
              </div>
              <div class="context-rail__actions">
                ${actionList}
              </div>
            </div>
            <div class="context-rail__accordion" data-exclusive-accordion>
              <details class="context-rail__group">
                <summary>
                  <span>Page sections</span>
                  <span class="context-rail__count">${sectionLinks.length}</span>
                </summary>
                <ul class="context-rail__list">${sectionList}</ul>
              </details>
              <details class="context-rail__group">
                <summary>
                  <span>${page ? "Nearby in branch" : "Related links"}</span>
                  <span class="context-rail__count">${relatedLinks.length}</span>
                </summary>
                <ul class="context-rail__list">${relatedList}</ul>
              </details>
              <details class="context-rail__group"${!page && !tags.length ? " hidden" : ""}>
                <summary>
                  <span>Concept tags</span>
                  <span class="context-rail__count">${tags.length}</span>
                </summary>
                <div class="context-rail__tags">${tagList}</div>
              </details>
            </div>
          </div>
        </details>
      </div>
    `;

    if (!sectionLinks.length) {
      return;
    }

    const shell = mount.querySelector(".context-rail__shell");
    const activeLinks = [...mount.querySelectorAll("[data-context-active-link], [data-context-mobile-active-link]")];
    const activeMeta = mount.querySelector("[data-context-active-meta]");
    const linkMap = new Map(
      [...mount.querySelectorAll("[data-context-section-link]")].map((link) => [link.dataset.contextSectionLink, link]),
    );
    let activeId = "";
    let ticking = false;

    function applyActiveSection(entry) {
      if (!entry || activeId === entry.id) {
        return;
      }

      activeId = entry.id;
      activeLinks.forEach((link) => {
        link.textContent = entry.title;
        link.setAttribute("href", `#${entry.id}`);
      });
      if (activeMeta) {
        activeMeta.textContent = `Section ${entry.index + 1} of ${sectionLinks.length}${entry.meta ? ` · ${entry.meta}` : ""}`;
      }

      linkMap.forEach((link, id) => {
        const isActive = id === entry.id;
        link.classList.toggle("is-active", isActive);
        if (isActive) {
          link.setAttribute("aria-current", "location");
        } else {
          link.removeAttribute("aria-current");
        }
      });
    }

    function resolveActiveSection() {
      const threshold = window.innerWidth <= 1080 ? 132 : 154;
      let candidate = sectionLinks[0];

      sectionLinks.forEach((entry) => {
        if (entry.node.getBoundingClientRect().top - threshold <= 0) {
          candidate = entry;
        }
      });

      applyActiveSection(candidate);
    }

    function requestActiveSectionUpdate() {
      if (ticking) {
        return;
      }

      ticking = true;
      window.requestAnimationFrame(() => {
        ticking = false;
        resolveActiveSection();
      });
    }

    let compactMode = window.innerWidth <= 760;

    function syncShellMode() {
      if (!shell) {
        return;
      }

      const nextCompactMode = window.innerWidth <= 760;
      if (nextCompactMode !== compactMode) {
        compactMode = nextCompactMode;
        shell.open = !compactMode;
        return;
      }

      if (!compactMode) {
        shell.open = true;
      }
    }

    function bindMobileSummaryLinks() {
      const summaryLinks = mount.querySelectorAll(".context-rail__mobile-summary a[href]");
      summaryLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
          event.preventDefault();
          event.stopPropagation();

          const rawHref = link.getAttribute("href");
          if (!rawHref) {
            return;
          }

          if (rawHref.startsWith("#")) {
            const target = document.querySelector(rawHref);
            if (target) {
              if (compactMode && shell) {
                shell.open = false;
              }
              window.location.hash = rawHref.slice(1);
              return;
            }
          }

          window.location.href = link.href || rawHref;
        });
      });
    }

    syncShellMode();
    bindMobileSummaryLinks();
    resolveActiveSection();
    window.addEventListener("scroll", requestActiveSectionUpdate, { passive: true });
    window.addEventListener("resize", () => {
      syncShellMode();
      requestActiveSectionUpdate();
    });
    window.addEventListener("hashchange", requestActiveSectionUpdate);
    window.addEventListener("load", requestActiveSectionUpdate);
    window.setTimeout(requestActiveSectionUpdate, 140);
    window.setTimeout(requestActiveSectionUpdate, 360);

    shell?.addEventListener("click", (event) => {
      const trigger = event.target.closest("a[href^='#']");
      if (!trigger) {
        return;
      }

      if (window.innerWidth <= 760) {
        window.setTimeout(() => {
          shell.open = false;
        }, 120);
      }
    });
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

  function tagLabel(tag) {
    return data.tagMeta?.[tag]?.label || String(tag || "")
      .replace(/-/g, " ")
      .replace(/\bai\b/gi, "AI")
      .replace(/\bbayes\b/gi, "Bayes")
      .replace(/\b\w/g, (match) => match.toUpperCase());
  }

  function sortTagsByLabel(tags) {
    return [...tags].sort((left, right) => tagLabel(left).localeCompare(tagLabel(right)));
  }

  function renderTagButton(tag, extraClass = "") {
    const count = tagCount(tag);
    const key = escapeHtml(String(tag || ""));
    const label = escapeHtml(tagLabel(tag));
    const className = `tag-chip${extraClass ? ` ${extraClass}` : ""}`;
    const countLabel = count ? `<span class="tag-chip__count">${count}</span>` : "";

    return `
      <button class="${className}" type="button" data-tag-filter="${key}" data-tag-label="${label}" aria-label="Show pages tagged ${label}">
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
    const label = escapeHtml(tagLabel(tag));
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
    ).filter(isUsefulTag);
    mount.innerHTML = tags.length
      ? tags
        .map((tag) => `${renderTagButton(tag, "tag-chip--large")}`)
        .join("")
      : "";
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
        const stats = [route.difficulty, route.length]
          .filter(Boolean)
          .map((value) => `<span class="route-card__stat">${escapeHtml(value)}</span>`)
          .join("");
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
            <div class="route-card__header">
              <p class="eyebrow">${escapeHtml(route.audience)}</p>
              <div class="route-card__stats">${stats}</div>
            </div>
            <h3>${escapeHtml(route.title)}</h3>
            <p>${escapeHtml(route.summary)}</p>
            <div class="route-card__focus">
              <div>
                <p class="mini-label">Best if</p>
                <p>${escapeHtml(route.best_for || "")}</p>
              </div>
              <div>
                <p class="mini-label">Central question</p>
                <p>${escapeHtml(route.central_question || "")}</p>
              </div>
            </div>
            <ol class="route-steps">${steps}</ol>
            <div class="route-card__actions">
              <a class="button button--ghost" href="${href(route.steps?.[0]?.path || "/guided-reading/")}">Start route</a>
              <a class="text-link" href="${href("/guided-reading/")}#route-${escapeHtml(route.id)}">Open full route</a>
            </div>
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
        <h3>${escapeHtml(tagLabel(tag))}</h3>
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

  const SEARCH_SUGGESTIONS = ["belief", "induction", "Aquinas", "moral realism", "consciousness", "game theory"];
  const SEARCH_TYPE_RANK = { page: 30, branch: 24, glossary: 18, route: 14, tag: 2 };
  let cachedSearchEntries = null;
  let searchShell = null;
  let searchShellApi = null;

  function normalizeSearchText(value) {
    return String(value || "")
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, " ")
      .trim();
  }

  function tokenizeSearchText(value) {
    return normalizeSearchText(value).split(/\s+/).filter(Boolean);
  }

  function slugifySearchValue(value) {
    return normalizeSearchText(value).replace(/\s+/g, "-") || "entry";
  }

  function pageFormatLabel(page) {
    const title = String(page?.title || "");
    const tags = page?.tags || [];
    const path = page?.path || "";

    if (title.startsWith("Dialoguing with") || tags.includes("dialogue")) return "Dialogue";
    if (title.startsWith("Charting ")) return "Chart";
    if (/^what (is|are)\b/i.test(title) || tags.includes("primer")) return "Primer";
    if (title.includes("Case") || /\/case-\d+/.test(path)) return "Case study";
    if (tags.includes("comparison")) return "Comparison";
    return "Page";
  }

  function searchTypeLabel(type) {
    return {
      page: "Page",
      branch: "Branch guide",
      route: "Guided route",
      glossary: "Glossary term",
      tag: "Tag",
    }[type] || "Result";
  }

  function searchTypePlural(type) {
    return {
      page: "pages",
      branch: "branch guides",
      route: "guided routes",
      glossary: "glossary terms",
      tag: "tags",
    }[type] || "results";
  }

  function buildSearchEntries() {
    if (cachedSearchEntries) {
      return cachedSearchEntries;
    }

    const entries = [];

    (data.sections || []).forEach((section) => {
      if (!section?.branchGuidePath) {
        return;
      }

      entries.push({
        key: `branch:${section.id}`,
        type: "branch",
        title: `${section.name} Branch Guide`,
        section: section.name,
        meta: `${section.name} branch overview`,
        href: href(section.branchGuidePath),
        path: section.branchGuidePath,
        summary: section.summary || section.editorialIntro || "",
        tags: [...new Set([section.id, ...(section.futureTags || [])])].filter(Boolean).slice(0, 6),
        keywords: [
          section.name,
          section.id.replace(/-/g, " "),
          "branch guide",
          "branch overview",
          ...(section.seedTopics || []),
        ].join(" "),
      });
    });

    (data.taggedPages || []).forEach((page) => {
      entries.push({
        key: `page:${page.path}`,
        type: "page",
        title: page.title,
        section: page.section,
        meta: `${page.section} • ${pageFormatLabel(page)}`,
        href: href(page.path),
        path: page.path,
        summary: page.summary || "",
        tags: (page.tags || []).filter(isUsefulTag).slice(0, 6),
        keywords: [page.title, page.section, page.path.replaceAll("/", " "), ...(page.tags || [])].join(" "),
      });
    });

    (data.guidedReadingPaths || []).forEach((route) => {
      entries.push({
        key: `route:${route.id}`,
        type: "route",
        title: route.title,
        section: "Guided Reading",
        meta: `Guided route • ${route.audience}`,
        href: `${href("/guided-reading/")}#route-${route.id}`,
        path: "/guided-reading/",
        summary: route.summary || "",
        tags: ["guided-reading"],
        keywords: [
          route.title,
          route.audience,
          route.summary,
          ...(route.steps || []).map((step) => step.title),
        ].join(" "),
      });
    });

    (data.glossaryTerms || []).forEach((entry) => {
      entries.push({
        key: `glossary:${entry.term}`,
        type: "glossary",
        title: entry.term,
        section: entry.branch,
        meta: `Glossary term • ${entry.branch}`,
        href: `${href("/concept-glossary/")}#term-${slugifySearchValue(entry.term)}`,
        path: "/concept-glossary/",
        summary: entry.definition || "",
        tags: (entry.tags || []).filter(isUsefulTag).slice(0, 6),
        keywords: [entry.term, entry.branch, entry.definition, ...(entry.tags || []), ...(entry.paths || [])].join(" "),
      });
    });

    Object.entries(data.tagPages || {}).forEach(([tag, path]) => {
      const kind = data.tagMeta?.[tag]?.kind || "concept";
      const prefix = kind === "branch" ? "Branch" : kind === "format" ? "Format" : "Tag";
      entries.push({
        key: `tag:${tag}`,
        type: "tag",
        title: `${prefix}: ${tagLabel(tag)}`,
        section: "Tag discovery",
        meta: `${prefix} • ${tagCount(tag)} linked page${tagCount(tag) === 1 ? "" : "s"}`,
        href: href(path),
        path,
        summary: `Open the discovery page for ${tagLabel(tag)} and jump into the linked pages that use the term.`,
        tags: [tag],
        keywords: [tag, tagLabel(tag), prefix, "discovery", kind].join(" "),
      });
    });

    cachedSearchEntries = entries.map((entry) => {
      const title = normalizeSearchText(entry.title);
      const section = normalizeSearchText(entry.section);
      const tags = (entry.tags || []).map(normalizeSearchText).filter(Boolean);
      const summary = normalizeSearchText(entry.summary);
      const keywords = normalizeSearchText(entry.keywords);
      const pathText = normalizeSearchText(String(entry.path || "").replaceAll("/", " "));
      return {
        ...entry,
        _title: title,
        _section: section,
        _tags: tags,
        _summary: summary,
        _keywords: keywords,
        _pathText: pathText,
        _haystack: [title, section, summary, keywords, pathText, ...tags].join(" "),
      };
    });

    return cachedSearchEntries;
  }

  function highlightSearchTerms(text, terms) {
    const plain = String(text || "");
    if (!plain || !terms.length) {
      return escapeHtml(plain);
    }

    const escapedTerms = [...new Set(terms)]
      .filter(Boolean)
      .sort((a, b) => b.length - a.length)
      .map((term) => term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
    if (!escapedTerms.length) {
      return escapeHtml(plain);
    }

    const matcher = new RegExp(`(${escapedTerms.join("|")})`, "ig");
    const parts = plain.split(matcher);
    return parts
      .map((part) => {
        if (!part) return "";
        return escapedTerms.some((term) => new RegExp(`^${term}$`, "i").test(part))
          ? `<mark>${escapeHtml(part)}</mark>`
          : escapeHtml(part);
      })
      .join("");
  }

  function scoreSearchEntry(entry, normalizedQuery, terms) {
    let score = 0;
    let matchedTerms = 0;

    if (entry._title === normalizedQuery) score += 160;
    if (entry._title.startsWith(normalizedQuery)) score += 90;
    else if (entry._title.includes(normalizedQuery)) score += 56;

    if (entry.type === "page" && entry._title.includes(normalizedQuery)) score += 18;
    if (entry.type === "branch" && entry._title.includes(normalizedQuery)) score += 12;
    if (entry.type === "glossary" && entry._title.includes(normalizedQuery)) score += 8;

    if (entry._section === normalizedQuery) score += 40;
    else if (entry._section.includes(normalizedQuery)) score += 16;

    if (entry._pathText.includes(normalizedQuery)) score += 18;
    if (entry._summary.includes(normalizedQuery)) score += 14;
    if (entry._keywords.includes(normalizedQuery)) score += 20;
    if (entry._tags.some((tag) => tag === normalizedQuery)) score += 12;

    terms.forEach((term) => {
      let matched = false;

      if (entry._title === term) {
        score += 42;
        matched = true;
      } else if (entry._title.startsWith(term)) {
        score += 28;
        matched = true;
      } else if (entry._title.includes(term)) {
        score += 20;
        matched = true;
      }

      if (entry._tags.some((tag) => tag === term)) {
        score += 8;
        matched = true;
      } else if (entry._tags.some((tag) => tag.includes(term))) {
        score += 5;
        matched = true;
      }

      if (entry._section === term) {
        score += 14;
        matched = true;
      } else if (entry._section.includes(term)) {
        score += 7;
        matched = true;
      }

      if (entry._keywords.includes(term)) {
        score += 8;
        matched = true;
      }

      if (!matched && entry._haystack.includes(term)) {
        score += 4;
        matched = true;
      }

      if (matched) {
        matchedTerms += 1;
      }
    });

    if (terms.length > 1 && matchedTerms === terms.length) {
      score += 28;
    }

    score += SEARCH_TYPE_RANK[entry.type] || 0;
    return score;
  }

  function findSearchMatches(query) {
    const normalized = normalizeSearchText(query);
    const terms = tokenizeSearchText(query);
    if (normalized.length < 2 || !terms.length) {
      return { normalized, terms, matches: [] };
    }

    const matches = buildSearchEntries()
      .map((entry) => ({ entry, score: scoreSearchEntry(entry, normalized, terms) }))
      .filter(({ score }) => score > 0)
      .sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title))
      .slice(0, 20);

    return { normalized, terms, matches };
  }

  function renderSearchEmptyState() {
    const suggestions = SEARCH_SUGGESTIONS
      .map(
        (term) => `
          <button class="tag-chip tag-chip--large" type="button" data-site-search-suggestion="${escapeHtml(term)}">
            <span>${escapeHtml(term)}</span>
          </button>
        `,
      )
      .join("");

    return `
      <div class="search-empty">
        <p class="mini-label">Search the inquiry network</p>
        <h3>Start with a concept, thinker, branch, or pressure point.</h3>
        <p>Try a philosophical term like <em>belief</em>, a thinker like <em>Aquinas</em>, or a pressure such as <em>moral realism</em>.</p>
        <div class="tag-row">${suggestions}</div>
      </div>
    `;
  }

  function renderSearchResults(root, query) {
    const resultMount = root.querySelector("[data-site-search-results], [data-page-search-results]");
    if (!resultMount) {
      return;
    }

    const normalized = normalizeSearchText(query);
    if (normalized.length < 2) {
      resultMount.innerHTML = renderSearchEmptyState();
      return;
    }

    const { terms, matches } = findSearchMatches(query);
    if (!matches.length) {
      resultMount.innerHTML = `
        <div class="search-empty">
          <p class="mini-label">Search results</p>
          <h3>No close matches for “${escapeHtml(query)}”</h3>
          <p>Try a broader term, a philosopher’s surname, or a nearby concept.</p>
        </div>
      `;
      return;
    }

    const counts = matches.reduce((totals, { entry }) => {
      totals[entry.type] = (totals[entry.type] || 0) + 1;
      return totals;
    }, {});
    const summary = Object.entries(counts)
      .sort((a, b) => (SEARCH_TYPE_RANK[b[0]] || 0) - (SEARCH_TYPE_RANK[a[0]] || 0))
      .map(([type, count]) => `<span class="search-summary__pill">${count} ${searchTypePlural(type)}</span>`)
      .join("");

    const items = matches
      .map(({ entry }) => {
        const tagRow = entry.type !== "tag" && entry.tags?.length
          ? `<div class="search-result__tags">${entry.tags.slice(0, 4).map((tag) => renderTagLink(tag)).join("")}</div>`
          : "";
        const summaryText = entry.summary
          ? `<p class="search-result__summary">${highlightSearchTerms(entry.summary, terms)}</p>`
          : "";

        return `
          <li class="search-result">
            <p class="search-result__meta">
              <span class="search-result__pill">${escapeHtml(searchTypeLabel(entry.type))}</span>
              <span>${highlightSearchTerms(entry.meta || entry.section || "", terms)}</span>
            </p>
            <a class="search-result__title" href="${escapeHtml(entry.href)}">${highlightSearchTerms(entry.title, terms)}</a>
            ${summaryText}
            ${tagRow}
          </li>
        `;
      })
      .join("");

    resultMount.innerHTML = `
      <div class="search-results">
        <div class="search-results__header">
          <p class="mini-label">Search results</p>
          <h3>${escapeHtml(query)}</h3>
          <p>${matches.length} match${matches.length === 1 ? "" : "es"} shown.</p>
        </div>
        <div class="search-results__summary">${summary}</div>
        <ol class="search-results__list">
          ${items}
        </ol>
      </div>
    `;
  }

  function bindSearchRoot(root) {
    if (!root || root.dataset.searchReady === "true") {
      return root?._siteSearchApi || null;
    }

    const input = root.querySelector("[data-site-search-input], [data-page-search-input]");
    const clear = root.querySelector("[data-site-search-clear], [data-page-search-clear]");
    const syncParam = root.dataset.siteSearchSyncUrl || "";
    if (!input) {
      return null;
    }

    function syncUrl(value) {
      if (!syncParam) {
        return;
      }
      const url = new URL(window.location.href);
      const trimmed = String(value || "").trim();
      if (trimmed) url.searchParams.set(syncParam, trimmed);
      else url.searchParams.delete(syncParam);
      window.history.replaceState({}, "", `${url.pathname}${url.search}${url.hash}`);
    }

    function update(query) {
      renderSearchResults(root, query);
      syncUrl(query);
    }

    const initialQuery = syncParam ? new URLSearchParams(window.location.search).get(syncParam) || "" : input.value || "";
    if (initialQuery) {
      input.value = initialQuery;
    }

    update(input.value);
    input.addEventListener("input", () => update(input.value));
    clear?.addEventListener("click", () => {
      input.value = "";
      update("");
      input.focus();
    });
    root.addEventListener("click", (event) => {
      const suggestion = event.target.closest("[data-site-search-suggestion]");
      if (!suggestion) {
        return;
      }
      const query = suggestion.dataset.siteSearchSuggestion || "";
      input.value = query;
      update(query);
      input.focus();
    });

    const api = {
      setQuery(value) {
        input.value = value;
        update(value);
      },
      focus(select = false) {
        input.focus();
        if (select) {
          input.select();
        }
      },
      getQuery() {
        return input.value;
      },
    };

    root.dataset.searchReady = "true";
    root._siteSearchApi = api;
    return api;
  }

  function ensureSearchShell() {
    if (searchShell) {
      return { shell: searchShell, api: searchShellApi };
    }

    searchShell = document.createElement("div");
    searchShell.className = "site-search-shell";
    searchShell.hidden = true;
    searchShell.innerHTML = `
      <div class="site-search-shell__backdrop" data-close-site-search></div>
      <div class="site-search-shell__panel" role="dialog" aria-modal="true" aria-labelledby="site-search-title">
        <button class="site-search-shell__close" type="button" aria-label="Close site search" data-close-site-search>×</button>
        <div class="site-search site-search--modal" data-site-search-root>
          <label for="global-site-search-input">
            <span class="mini-label">Site search</span>
            <span id="site-search-title">Search the inquiry network</span>
          </label>
          <p class="site-search__hint">Search pages, branch guides, guided routes, glossary terms, and tags.</p>
          <div class="site-search__control">
            <input
              id="global-site-search-input"
              type="search"
              placeholder="Try belief, Aquinas, induction, moral realism..."
              autocomplete="off"
              data-site-search-input
            />
            <button class="button button--ghost" type="button" data-site-search-clear>Clear</button>
          </div>
          <div class="site-search__results" data-site-search-results></div>
        </div>
      </div>
    `;
    document.body.appendChild(searchShell);
    searchShellApi = bindSearchRoot(searchShell.querySelector("[data-site-search-root]"));

    searchShell.addEventListener("click", (event) => {
      if (event.target.closest("[data-close-site-search]")) {
        closeSiteSearch();
        return;
      }
      if (event.target.closest("[data-site-search-results] a[href]")) {
        closeSiteSearch();
      }
    });

    return { shell: searchShell, api: searchShellApi };
  }

  function openSiteSearch(query = "") {
    const { shell, api } = ensureSearchShell();
    shell.hidden = false;
    shell.classList.add("is-open");
    document.body.classList.add("site-search-open");
    if (query) {
      api?.setQuery(query);
    }
    window.requestAnimationFrame(() => api?.focus(true));
  }

  function closeSiteSearch() {
    if (!searchShell) {
      return;
    }
    searchShell.hidden = true;
    searchShell.classList.remove("is-open");
    document.body.classList.remove("site-search-open");
  }

  function isEditableTarget(target) {
    const node = target instanceof HTMLElement ? target : null;
    return Boolean(
      node && (
        node.isContentEditable
        || /^(INPUT|TEXTAREA|SELECT)$/.test(node.tagName)
        || node.closest("[contenteditable='true']")
      ),
    );
  }

  function initSiteSearch() {
    document.querySelectorAll("[data-site-search-root], [data-page-search]").forEach((root) => {
      bindSearchRoot(root);
    });

    document.addEventListener("click", (event) => {
      const trigger = event.target.closest("[data-open-site-search]");
      if (!trigger) {
        return;
      }
      event.preventDefault();
      openSiteSearch();
    });

    document.addEventListener("keydown", (event) => {
      const key = String(event.key || "").toLowerCase();

      if ((event.metaKey || event.ctrlKey) && key === "k") {
        event.preventDefault();
        openSiteSearch();
        return;
      }

      if (!event.metaKey && !event.ctrlKey && !event.altKey && event.key === "/" && !isEditableTarget(event.target)) {
        event.preventDefault();
        openSiteSearch();
        return;
      }

      if (event.key === "Escape" && searchShell && !searchShell.hidden) {
        closeSiteSearch();
      }
    });

    if (currentPage() === "/search/") {
      window.requestAnimationFrame(() => {
        const root = document.querySelector("[data-site-search-root]");
        root?._siteSearchApi?.focus();
      });
    }
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
  renderContextRail();
  initSiteSearch();
  initTagFilters();
  initExclusiveAccordions();
  revealHashTarget();
  window.addEventListener("hashchange", revealHashTarget);
  initQuizzes();
})();
