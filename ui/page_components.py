from styles.global_styles import GLOBAL_STYLES
from styles.theme_styles import THEME_STYLES
from ui.html_sanitize import html_sanitize


def page_top_start(title="App") -> str:
    return f"""
<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8">
      <title>{html_sanitize(title)}</title>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
 """


def page_top_end(custom_tags, custom_css="") -> str:
    return f"""
      {custom_tags}
      <style>
         {THEME_STYLES}
         {GLOBAL_STYLES}
         {custom_css}
      </style>
   </head>
"""


def page_body_start() -> str:
    return "<body>"


def page_body_end() -> str:
    return "</body></html>"