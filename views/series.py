from ui.layout import article_layout
from ui.html_elements import h1, p, div, strong

def series_view(teacher_name="Pablo"):
    
    dynamic_content = div(
        h1("Llamado a ser apóstol"),
        p("Esta es una lección sobre el fundamento del ", strong("evangelio"), "."),
        class_="lesson-container"
    )
    
    return article_layout(
        content=dynamic_content,
        title=f"Romanos | {teacher_name}"
    )