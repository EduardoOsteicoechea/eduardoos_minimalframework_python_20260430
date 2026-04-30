ARTICLE_STYLES = """

article {
   display:flex;
   flex-direction:column;
   max-width: 55ch;
   margin: 2rem auto;
   padding: 0 1rem;
   gap:45px;
}

.author-meta { 
   color: #aaa; 
   margin-bottom: 2rem; 
   font-size: 0.9rem;
   padding: 0 10px;
}

h1,h2 {
   color: var(--accent_color_01);
}

section {
   display:flex;
   flex-direction:column;
   gap:65px;
}

.main-verse { 
   font-style: italic; 
   border-left: 4px solid #757575; 
   padding-left: 1rem; 
   margin: 1.5rem 0; 
   color: #ddd; 
   background: #2a2a2a; 
   padding: 1rem; 
   border: solid 1px #fafafa;
}

.bible-quote { 
   color: var(--accent_color_01);
   font-weight:600;
}

.biblical_quote_reference {
   display: block;
   margin: 15px 0 0 auto;
   width:100%;
   text-align:right;
   font-size:.8rem;
}

h2 {
   font-size:1.5rem;
}

p {
   line-height: 1.35; 
}

strong {
   font-weight:900 !important;
   text-decoration: underline;
}

"""
 