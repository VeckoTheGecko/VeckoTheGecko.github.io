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
