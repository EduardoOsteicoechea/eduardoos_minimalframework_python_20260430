import traceback

from frontend.html_sanitize import html_sanitize
from frontend.layout import base_layout


def handle_exception(exception, *args, **kwargs):
    """
    Application global error handler. 
    Accepts the exception and any extra arguments safely.
    """
    error_trace = traceback.format_exc()

    # Safely extract paths if they exist in kwargs, otherwise default to "Unknown"
    absolute_path = kwargs.get('absolute_path', 'Unknown')
    clean_path = kwargs.get('clean_path', 'Unknown')
    response =  f"""
        <h1>Application Error</h1>
        <br>
        <p><strong>Error message:</strong> {html_sanitize(str(exception))}</p>
        <br>
        <p><strong>Attempted Path:</strong> {html_sanitize(str(absolute_path))}</p>
        <br>
        <p><strong>clean_path:</strong> {html_sanitize(str(clean_path))}</p>
        <br>
        <h3>Stack Trace:</h3>
        <pre>{html_sanitize(error_trace)}</pre>
        """
    print(f"{response}")
    return base_layout(response, title="Error")
