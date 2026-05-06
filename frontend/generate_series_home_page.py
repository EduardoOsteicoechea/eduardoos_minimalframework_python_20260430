# ./ui/generate_series_home_page.py

import json
import os

from handlers.handle_exception import handle_exception


def generate_series_home_page(project_root_path, path):
    
    clean_path = (path + "/data.json").lstrip('/')
    absolute_path = os.path.join(project_root_path, clean_path)
    
    try:
        
        with open(absolute_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return f"{data}"
    
    except Exception as e:
        
        handle_exception(e)