# Blog Archive Section — Design Spec

**Date:** 2026-07-31

## Overview

Add an archive section to the blog. Posts are opted into the archive via frontmatter (`archive: true`). Archived posts:
- Do **not** appear in the main blog feed or any other blog views (categories, pagination, etc.)
- Are visible on a dedicated `/blog/archive/` page that uses the same card style as the main feed
- Retain their original URLs unchanged

## Approach

MkDocs hook + archive page using Material's existing `blog.html` template. No custom plugin, no new dependencies.

## Components

### 1. Frontmatter convention

Any post can be archived by adding `archive: true` to its YAML frontmatter:

```yaml
---
date:
  created: 2022-01-30
archive: true
---
```

All other frontmatter fields remain unchanged. The post file location and rendered URL are unaffected.

### 2. Hook — `hooks/archive.py`

A single `on_page_context(context, *, page, config, nav)` function. Runs after Material's blog plugin has already populated the page context (hooks load after plugins in MkDocs).

**Behaviour:**

- If `"posts"` is in `context` (i.e. this is a blog index, pagination, or category page): filter the list to exclude posts where `post.meta.get("archive")` is truthy. Return the modified context.
- If `page.file.src_path == "blog/archive.md"` (the archive page): read all posts from `config.plugins["blog"].blog.posts`, filter to those with `archive: true` in meta, assign to `context["posts"]`, set `context["pagination"] = None`. Return context.
- Otherwise: return context unchanged.

No monkey-patching. The hook relies on two stable MkDocs/Material surfaces: `context["posts"]` (set by the blog plugin's own `on_page_context`) and `plugin.blog.posts` (the full post list populated during `on_files`).

### 3. Archive page — `docs/blog/archive.md`

A standard MkDocs page. Uses `template: blog.html` in frontmatter so Material renders it with the same post-card loop as the main blog index. The hook injects `posts` into its context at build time.

```yaml
---
template: blog.html
hide:
  - navigation
  - toc
  - footer
---

# Archive
```

### 4. `mkdocs.yml` changes

Add `hooks:` block and add the archive page to `nav`:

```yaml
hooks:
  - hooks/archive.py

nav:
  - index.md
  - blog/index.md
  - blog/archive.md
  - about.md
```

## Data flow

```
Build start
  └─ blog plugin on_files: loads all posts, populates plugin.blog.posts
  └─ blog plugin on_nav: attaches posts to views

Page render (main blog index / pagination / category pages)
  └─ blog plugin on_page_context: sets context["posts"] = all matching posts
  └─ hooks/archive.py on_page_context: filters context["posts"] to remove archived

Page render (blog/archive.md)
  └─ blog plugin on_page_context: skips (not a managed view)
  └─ hooks/archive.py on_page_context: injects archived posts into context["posts"]
  └─ blog.html template: renders post cards via partials/post.html
```

## Constraints and non-goals

- No pagination on the archive page (acceptable for a personal blog with few archived posts)
- Archived posts still appear in the RSS feed (`rss` plugin matches `blog/posts/.*` regardless of archive status) — acceptable, no change needed
- No visual indicator on the archive cards distinguishing them from regular posts — not requested
