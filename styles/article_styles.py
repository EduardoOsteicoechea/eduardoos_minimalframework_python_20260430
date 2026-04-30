ARTICLE_STYLES = """

article {
   display:flex;
   flex-direction:column;
   max-width: 55ch;
   margin: 1rem auto;
   padding: 0 1.5rem;
   gap:20px;
}

.author-meta { 
   color: #aaa; 
   font-size: 0.9rem;
}

h1,h2 {
   color: var(--accent_color_01);
}

section {
   display:flex;
   flex-direction:column;
   gap:30px;
}

.main-verse { 
   font-style: italic; 
   border-left: 4px solid #757575; 
   padding-left: 1rem; 
   color: #ddd; 
   background: #2a2a2a; 
   padding: 1rem; 
   border: solid 1px #fafafa;
}

.bible-quote { 
   display:flex;
   flex-direction:column;
   gap: 15px;
   align-items:start;
   justify-content:start;   
   font-weight:600;
}

.bible_quote_text{
   width:100%;
   color: var(--accent_color_01);
}

.bible_quote_reference {
   text-align:center;
   font-size:.75rem;
   border-radius: var(--border_radius_01) !important;
   padding: 8px 10px;
   background: #ddd;
   color: var(--accent_color_01);
}

h2 {
   font-size:1.5rem;
   margin: 35px 0 0 0;
}

p {
   line-height: 1.25; 
}

strong {
   font-weight:900 !important;
   /*text-decoration: underline;*/
}

"""
 