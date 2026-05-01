from styles.global_styles import GLOBAL_STYLES
from styles.page_actions_styles import PAGE_ACTIONS_STYLES
from styles.theme_styles import THEME_STYLES
from ui.html_sanitize import html_sanitize


def page_top_start(title="App") -> str:
    static_assets_route = "/static/"
    js_static_assets_route = "/static/js"
    return f"""
<!DOCTYPE html>
<html lang="en" data-theme="light">
   <head>
      <meta charset="UTF-8">      
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      
      <title>{html_sanitize(title)}</title>
      <meta name="description" content="Architecturally trained BIM Modeler & Full Stack Developer. Bridging design and technology with custom Automations, AI integrations, and cloud solutions." />
      
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Outfit:wght@100..900&family=Raleway:ital,wght@0,100..900;1,100..900&family=Source+Code+Pro:ital,wght@0,200..900;1,200..900&display=swap" rel="stylesheet">
      
      <link rel="icon" href="/static/media/favicon.ico" sizes="any" />
      <link rel="icon" type="image/png" sizes="32x32" href="/static/media/favicon-32x32.png" />
      <link rel="icon" href="/static/media/favicon-48.png" sizes="48x48" type="image/png" />
      <link rel="icon" href="/static/media/favicon-96.png" sizes="96x96" type="image/png" />
      <link rel="icon" href="/static/media/favicon-192.png" sizes="192x192" type="image/png" />
      <link rel="apple-touch-icon" href="/static/media/favicon-180.png" sizes="180x180" />
      <link rel="shortcut icon" href="/static/media/favicon-32.png" sizes="32x32" type="image/png" />
      
      <meta name="google-site-verification" content="RQdklgFawBo75p5tN7wranunENDjUu27gol9MENm-SM" />
 """


def page_top_end(custom_tags, custom_css="") -> str:
    return f"""
      {custom_tags}
      <style>
         {THEME_STYLES}
         {GLOBAL_STYLES}
         {PAGE_ACTIONS_STYLES}
         {custom_css}
      </style>
   </head>
"""


def page_body_start() -> str:
    return "<body>"


def page_body_end() -> str:
    return """
    <button id="page_actions_button" class="page_actions_button page_actions_button_unactive"></button>
    <div id="page_actions_main_container" class="page_actions_main_container">        
        <button id="toggle_theme_button" class="page_action_button"></button>
        <button id="display_biblical_references_button" class="page_action_button"></button>
    </div>
    <script type="module" src="/static/js/page_actions/page_actions_button.js"></script>
</body>
</html>
 """
