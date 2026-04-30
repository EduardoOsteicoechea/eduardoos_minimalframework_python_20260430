from server.router import router

def handle_request_route(request_data):
    request_lines = request_data.split("\r\n")
    request_first_line = request_lines[0]
    line_parts = request_first_line.split(" ")
    
    method = "UNKNOWN"
    path = "/"
    
    if len(line_parts) >= 2:
        method = line_parts[0]
        path = line_parts[1]
    
    print(f"Incoming request: {method} {path}")
    
    return router(method, path)