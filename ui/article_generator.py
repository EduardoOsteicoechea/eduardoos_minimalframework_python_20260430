from typing import Any
from ui.html_elements import (
    blockquote,
    strong,
    span,
    h1,
    p,
    div,
    h2,
    article
)
from ui.layout import article_layout


def apply_emphasis(text: str, phrases: list[str]) -> str:
    if not phrases or not text:
        return text
    for phrase in phrases:
        if phrase and phrase in text:
            text = text.replace(phrase, strong(phrase, {"class":"biblical_quote_emphasized_phrase"}))
    return text


def format_biblical_quote(text: str, ref: str, phrases: list[str]) -> str:
    formatted_text = p(f"\"{apply_emphasis(text, phrases)}\"", {"class": "bible_quote_text"})
    ref_box = p(ref, {"class": "bible_quote_reference"})
    content = f"{ref_box} {formatted_text}"
    return blockquote(content, {"class": "bible-quote"})


def format_paragraph(text: str, phrases: list[str]) -> str:
    """Formats standard text into a paragraph with emphasis."""
    return p(apply_emphasis(text, phrases))


def format_section(index: int, section: dict[str, Any]) -> list:
   
   section_elements = [f"<section id='section_{index}'>"]

   for item in section.get("content", []):
      if not isinstance(item, dict):
         continue
      text = item.get("text", "")
      ref = item.get("biblical_reference", "")
      phrases = item.get("emphasized_phrases", [])
      if ref:
         section_elements.append(format_biblical_quote(text, ref, phrases))
      elif text:
         section_elements.append(format_paragraph(text, phrases))

   section_elements.append("</section>")

   return section_elements


# --- MAIN GENERATOR ---

def article_generator(json_data: dict[str, Any]) -> str:
    """Turns JSON data into a full HTML article layout."""
    title_text = json_data.get("title", "Estudio Bíblico")
    teacher = json_data.get("creator", "Unknown")
    serie = json_data.get("serie", "").capitalize()

    # 1. Initialize elements with the Header data
    elements = [
        h1(title_text),
        p(f"Serie: {serie} | Facilitador: {teacher}", {"class": "author-meta"})
    ]

    # 2. Iterate through Sections
    section_counter = 1
    for section in json_data.get("sections", []):
       if heading := section.get("heading", ""):
         elements.append(h2(section.get("heading", "")))
         elements.extend(format_section(section_counter, section))
         section_counter = section_counter + 1

    # 3. Wrap everything in a main container
    dynamic_content = article(elements, {"class": "article-container"})

    return article_layout(
        content=dynamic_content,
        title=f"{serie} | {title_text}"
    )
