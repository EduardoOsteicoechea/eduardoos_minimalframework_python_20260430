from typing import Optional
from frontend.html_tag import html_tag


def h1(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("h1", tag_content, tag_attributes)


def p(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("p", tag_content, tag_attributes)


def div(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("div", tag_content, tag_attributes)


def strong(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("strong", tag_content, tag_attributes)


def h2(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("h2", tag_content, tag_attributes)


def blockquote(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("blockquote", tag_content, tag_attributes)


def iframe(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("iframe", tag_content, tag_attributes)


def em(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("em", tag_content, tag_attributes)


def span(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("span", tag_content, tag_attributes)


def article(
    tag_content: Optional[list[str]] = None,
    tag_attributes: Optional[dict[str, str]] = None
): return html_tag("article", tag_content, tag_attributes)
