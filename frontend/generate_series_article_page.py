# ./ui/generate_series_home_page.py

import json
import os

from handlers.handle_exception import handle_exception
from frontend.article_generator import article_generator


def generate_series_article_page(project_root_path, path):
    clean_path = (path + "/data.json").lstrip('/')
    absolute_path = os.path.join(project_root_path, clean_path)
    try:
        with open(absolute_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return article_generator(data)
    except Exception as e:
        handle_exception(e)