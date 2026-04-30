# ui/base_layout.py
from styles.article_styles import ARTICLE_STYLES
from ui.page_components import (
    page_top_start,
    page_top_end,
    page_body_start,
    page_body_end,
)


def base_layout(content: str, title="App", custom_head_tags="", custom_css="") -> str:

    combined_css = f"{custom_css}" if custom_css else ""

    return "".join([
        page_top_start(title=title),
        page_top_end(custom_head_tags, combined_css),
        page_body_start(),
        content,
        page_body_end()
    ])


def article_layout(content: str, title="App", custom_css="") -> str:
    combined_css = f"{ARTICLE_STYLES}\n{custom_css}"
    return base_layout(
        content=content,
        title=title,
        custom_head_tags="",
        custom_css=combined_css
    )
