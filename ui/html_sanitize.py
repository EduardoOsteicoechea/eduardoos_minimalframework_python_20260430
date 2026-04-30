import html

def html_sanitize(text: str) -> str:
    return html.escape(str(text))