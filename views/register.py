from frontend.layout import base_layout


def register_view():
    dynamic_content = f"""

<form method="post" action="http://localhost:3000/api/register">

    <div>
        <label for="username">Username</label>
        <input type="text" name="username" id="username" />
    </div>

    <div>
        <label for="username">Email</label>
        <input type="email" name="email" id="email" />
    </div>

    <div>
        <label for="username">Password</label>
        <input type="password" name="password" id="password" />
    </div>

    <input type="submit" name="submit" content="Save">
</form>    



    """

    return base_layout(
        content=dynamic_content,
        title="Home"
    )
