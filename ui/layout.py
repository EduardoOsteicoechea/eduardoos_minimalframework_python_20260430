# ui/base_layout.py
from ui.page_components import (
    page_top_start,
    page_top_end,
    page_body_start,
    page_body_end,
)


def base_layout(content: str, title="App", custom_head_tags="") -> str:
    return "".join([
        page_top_start(title=title),
        page_top_end(custom_head_tags),
        page_body_start(),
        content,
        page_body_end()
    ])


def article_layout(content: str, title="App") -> str:
    return base_layout(
        content=content,
        title=title,
        custom_head_tags="""
        <link rel="stylesheet" href="/static/css/article.css" />
        """
    )
