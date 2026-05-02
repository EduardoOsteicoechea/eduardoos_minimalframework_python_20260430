# ui/pages.py
import json
import os  # Import os
import traceback  # Import traceback to get the stack trace

from ui.article_generator import article_generator
from ui.html_sanitize import html_sanitize
from views.home import home_view
from views.register import register_view
from views.series import series_view
from ui.layout import base_layout

# Get the directory where pages.py is located (the 'ui' folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the root of the project
PROJECT_ROOT = os.path.dirname(BASE_DIR)


class pages:

    @staticmethod
    def home(user_name="Guest"):
        return home_view(user_name)

    def register():
        return register_view()

    @staticmethod
    def undefined():
        return base_layout("<h1>404 Not Found</h1>", title="Error")

    @staticmethod
    def series(user_name="Guest"):
        return series_view(user_name)

    @staticmethod
    def series_romanos_pablo_llamado():

        clean_path = "/static/json/series/romanos/pablo/llamado/data.json".lstrip(
            '/')

        absolute_path = os.path.join(PROJECT_ROOT, clean_path)

        try:
            with open(absolute_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return article_generator(data)

        except Exception as e:
            # Capture the full stack trace as a string
            error_trace = traceback.format_exc()

            return base_layout(
                f"""
                <h1>Error loading article</h1>
                <br>
                <p><strong>Error message:</strong> {html_sanitize(str(e))}</p>
                <br>
                <p><strong>Attempted Path:</strong> {html_sanitize(absolute_path)}</p>
                <br>
                <p><strong>clean_path:</strong> {html_sanitize(clean_path)}</p>
                <br>
                <h3>Stack Trace:</h3>
                <pre>{html_sanitize(error_trace)}</pre>
                """,
                title="Error"
            )
