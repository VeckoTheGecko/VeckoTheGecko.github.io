# Blog Archive Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `/blog/archive/` page showing posts flagged with `archive: true` in frontmatter, hidden from the main feed.

**Architecture:** A MkDocs hook (`hooks/archive.py`) intercepts `on_page_context` to filter archived posts out of the main blog index and inject them into a dedicated archive page. The archive page uses Material's existing `blog.html` template, so it renders identically to the main feed. No new dependencies.

**Tech Stack:** Python 3.12, MkDocs Material ≥9.5.49, MkDocs hooks system

## Global Constraints

- Python 3.12+
- No new pip dependencies
- Hook file must live at `hooks/archive.py` (matches mkdocs.yml reference)
- Archive page src path must be exactly `blog/archive.md` (the hook detects it by this path)
- `archive: true` is the frontmatter key — no other naming
- ruff lint must pass (`uv run ruff check hooks/`)

---

### Task 1: Hook and wiring

**Files:**
- Create: `hooks/archive.py`
- Modify: `mkdocs.yml`

**Interfaces:**
- Produces: `on_page_context(context, *, page, config, nav)` — called by MkDocs for every page render; filters `context["posts"]` on blog views, injects archived posts on the archive page

- [ ] **Step 1: Create `hooks/archive.py`**

```python
"""MkDocs hook: filters archived posts from the main blog feed.

Posts with ``archive: true`` in their frontmatter are excluded from the
main blog index (and all other blog views such as categories and
pagination) and are instead surfaced on the dedicated archive page at
``blog/archive.md``.
"""


def on_page_context(context, *, page, config, nav):
    """Filter archived posts from blog views; inject them on the archive page."""
    blog_plugin = config.plugins.get("blog")
    if not blog_plugin:
        return context

    # Blog index / pagination / category pages already have context["posts"]
    # set by the blog plugin. Strip out any post marked archive: true.
    if "posts" in context:
        context["posts"] = [
            post for post in context["posts"]
            if not post.meta.get("archive")
        ]
        return context

    # The dedicated archive page: inject all archived posts.
    if page.file.src_path == "blog/archive.md":
        context["posts"] = [
            post for post in blog_plugin.blog.posts
            if post.meta.get("archive")
        ]
        context["pagination"] = None

    return context
```

- [ ] **Step 2: Add the hook to `mkdocs.yml`**

In `mkdocs.yml`, add a top-level `hooks:` block (place it after `plugins:`):

```yaml
hooks:
  - hooks/archive.py
```

- [ ] **Step 3: Lint the hook**

```bash
uv run ruff check hooks/archive.py
```

Expected: no output (clean).

- [ ] **Step 4: Verify build succeeds**

```bash
uv run mkdocs build --strict 2>&1 | tail -5
```

Expected: `INFO    -  Documentation built in ...` with no errors or warnings.

- [ ] **Step 5: Commit**

```bash
jj describe -m "Add archive hook and wire into mkdocs.yml" && jj new
```

---

### Task 2: Archive page and end-to-end verification

**Files:**
- Create: `docs/blog/archive.md`
- Modify: `mkdocs.yml` (nav)
- Modify: `docs/blog/posts/001_my-first-post.md` (temporary `archive: true` for testing — revert or keep as desired)

**Interfaces:**
- Consumes: `on_page_context` from Task 1 — injects `context["posts"]` when `page.file.src_path == "blog/archive.md"`

- [ ] **Step 1: Create `docs/blog/archive.md`**

```markdown
---
template: blog.html
hide:
  - navigation
  - toc
  - footer
---

# Archive
```

- [ ] **Step 2: Add the archive page to nav in `mkdocs.yml`**

Change the `nav:` section to:

```yaml
nav:
  - index.md
  - blog/index.md
  - blog/archive.md
  - about.md
```

- [ ] **Step 3: Mark post 001 as archived for testing**

In `docs/blog/posts/001_my-first-post.md`, add `archive: true` to the frontmatter:

```yaml
---
date:
  created: 2022-01-30
  updated: 2025-01-17
slug: welcome-to-vecko.me
archive: true
---
```

- [ ] **Step 4: Build**

```bash
uv run mkdocs build --strict 2>&1 | tail -5
```

Expected: clean build.

- [ ] **Step 5: Verify post is absent from the main blog index**

```bash
grep -i "welcome-to-vecko" site/blog/index.html
```

Expected: no output (post title not present in main feed).

- [ ] **Step 6: Verify post is present on the archive page**

```bash
grep -i "welcome-to-vecko" site/blog/archive/index.html
```

Expected: at least one match (the post card appears on the archive page).

- [ ] **Step 7: Verify the post's own URL is unchanged**

```bash
ls site/blog/welcome-to-vecko.me/
```

Expected: `index.html` exists (post is still rendered at its original slug URL).

- [ ] **Step 8: Decide on test post**

If post 001 should remain archived (it already notes it's out of date), leave `archive: true` in place. If it was just for testing, revert the frontmatter change.

- [ ] **Step 9: Commit**

```bash
jj describe -m "Add archive page and verify end-to-end" && jj new
```
