from api.handle_register import handle_register
from server.HTTPRequest import HTTPRequest
from router.http_response import http_response
from frontend.pages import pages

# 1. Update the signature to accept the single Request object
def router(request: HTTPRequest):
    
    if request.path == "/" or request.path == "/home":
        html_string = pages.home(user_name="Eduardo")
        return http_response(html_string)
        
    elif request.path == "/register":
        html_string = pages.register()
        return http_response(html_string)        
        
    elif request.path == "/api/register" and request.method == "POST":
        response = handle_register(request.body)
        return response
        
    elif request.path == "/series":
        html_string = pages.series()
        return http_response(html_string)
        
    elif request.path == "/series/romanos/pablo/origen":
        html_string = pages.series_romanos_pablo_origen()
        return http_response(html_string)        
        
    elif request.path == "/series/romanos/pablo/violencia":
        html_string = pages.series_romanos_pablo_violencia()
        return http_response(html_string)
        
    elif request.path == "/series/romanos/pablo/gracia":
        html_string = pages.series_romanos_pablo_gracia()
        return http_response(html_string)
        
    else:
        if hasattr(pages, 'undefined'):
            html_string = pages.undefined()
        else:
            html_string = f"<h1>404 Error</h1><p>The endpoint '{request.path}' does not exist.</p>"
        return http_response(html_string, status_code=404)