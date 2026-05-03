from server.router import router

def handle_request_route(request_data):    
    # print(f"[METHOD: handle_request_route]: {request_data}")
    # print(f"    request_data: {request_data}")
    
    request_lines = request_data.split("\r\n")
    
    if not request_lines:        
        print(f"[METHOD: handle_request_route]: missing request_lines")
    
    request_first_line = request_lines[0]
    line_parts = request_first_line.split(" ")
    
    method = "UNKNOWN"
    path = "/"
    
    if len(line_parts) >= 2:
        method = line_parts[0]
        path = line_parts[1]
    
    print(f"Incoming request: {method} {path}")
    
    return router(method, path, get_request_body(request_data))

def get_request_body(request_data):
    splitted_request = request_data.split("\r\n\r\n")
    return splitted_request[1] if len(splitted_request) > 1 else ""