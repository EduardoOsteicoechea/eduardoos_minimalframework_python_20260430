# ui/pages.py
import os  # Import os
from frontend.generate_series_article_page import generate_series_article_page
from frontend.generate_series_home_page import generate_series_home_page
from views.home import home_view
from views.register import register_view
from frontend.layout import base_layout

# Get the directory where pages.py is located (the 'ui' folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the root of the project
PROJECT_ROOT = os.path.dirname(BASE_DIR)

series_route = "/static/series/"

class pages:
    @staticmethod
    def undefined():
        return base_layout("<h1>404 Not Found</h1>", title="Error")
    @staticmethod
    def home(user_name="Guest"):
        return home_view(user_name)
    def register():
        return register_view()
    @staticmethod
    def series(user_name="Guest"):
        return generate_series_home_page(PROJECT_ROOT, series_route)
    @staticmethod
    def series_romanos_pablo_origen():
        return generate_series_article_page(PROJECT_ROOT, f"{series_route}romanos/pablo/origen")
    @staticmethod
    def series_romanos_pablo_violencia():
        return generate_series_article_page(PROJECT_ROOT, f"{series_route}romanos/pablo/violencia")
    @staticmethod
    def series_romanos_pablo_gracia():
        return generate_series_article_page(PROJECT_ROOT, f"{series_route}romanos/pablo/gracia")