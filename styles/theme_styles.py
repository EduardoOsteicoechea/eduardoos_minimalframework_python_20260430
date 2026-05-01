THEME_STYLES = """
/* 1. Default (Light) Theme */
:root,
:root[data-theme="light"] {
   --global_background: #f0f0f0;
   --global_foreground: #555;
   --accent_color_01: #000;
   --border_radius_01: 4px;
   --button_background: #aaa;
}

:root{
   color: var(--global_foreground)   
}

/* 2. Automatic Dark Theme */
@media (prefers-color-scheme: dark) {
    :root {
       --global_background: #121212; /* Deep dark gray */
       --global_foreground: #e0e0e0; /* Off-white text */
       --accent_color_01: #ffffff;   /* White accents */
       /* Notice we don't need to redefine border_radius if it doesn't change */
    }
    
}

/* 3. Manual Dark Theme (Forces dark mode if the user clicks the button) */
:root[data-theme="dark"] {
   --global_background: #121212;
   --global_foreground: #e0e0e0;
   --accent_color_01: #ffffff;
   --button_background: red;
}
"""