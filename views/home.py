from ui.layout import base_layout


def home_view(user_name="Guest"):
    dynamic_content = f"""
    <h1>Welcome, {user_name}</h1>
    <p>This is the home page.</p>
    """

    return base_layout(
        content=dynamic_content,
        title="Home"
    )
