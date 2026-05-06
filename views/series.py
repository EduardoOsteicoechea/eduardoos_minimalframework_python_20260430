from frontend.layout import article_layout
from frontend.html_elements import h1, p, div, strong

def series_view(teacher_name="Pablo"):
    
    dynamic_content = div(
        h1("Series"),
        "sdfsd",
        class_="lesson-container"
    )
    
    return article_layout(
        content=dynamic_content,
        title=f"Romanos | {teacher_name}"
    )