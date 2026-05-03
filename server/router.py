from api.handle_register import handle_register
from server.http_html_response import http_html_response
from ui.pages import pages

def router(method, path, body):
    # print(f"[METHOD: router]:")
    # print(f"    method: {method}")
    # print(f"    path: {path}")
    # print(f"    body: {body}")
    
    if path == "/" or path == "/home":
        html_string = pages.home(user_name="Eduardo")
        return http_html_response(html_string)
        
    elif path == "/register":
        html_string = pages.register()
        return http_html_response(html_string)        
    elif path == "/api/register" and method == "POST":
        response = handle_register(body)
        return response
        
    elif path == "/series":
        html_string = pages.series()
        return http_html_response(html_string)
        
    elif path == "/series/romanos/pablo/llamado":
        html_string = pages.series_romanos_pablo_llamado()
        return http_html_response(html_string)
        
    else:
        if hasattr(pages, 'undefined'):
            html_string = pages.undefined()
        else:
            html_string = f"<h1>404 Error</h1><p>The endpoint '{path}' does not exist.</p>"
            
        return http_html_response(html_string)