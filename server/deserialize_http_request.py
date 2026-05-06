from server.HTTPRequest import HTTPRequest


def deserialize_http_request(raw_headers, raw_body) -> HTTPRequest:
    
    print(f"    [raw_headers] -> {raw_headers}")
    print(f"    [raw_body] -> {raw_body}")
    
    headers_text = raw_headers.decode("utf-8", errors="replace")
    lines = headers_text.split("\r\n")
    
    request_line = lines[0].split(" ")
    method = request_line[0] if len(request_line) > 0 else "GET"
    path = request_line[1] if len(request_line) > 1 else "/"
    
    headers = {}
    for line in lines[1:]:
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip().lower()] = value.strip()
            
    cookies = {}
    if "cookie" in headers:
        raw_cookie_string = headers["cookie"] 
        cookie_pairs = raw_cookie_string.split(";")        
        for pair in cookie_pairs:
            if "=" in pair:
                cookie_key, cookie_val = pair.split("=", 1)
                cookies[cookie_key.strip()] = cookie_val.strip()
            
    body = raw_body.decode("utf-8", errors="replace")
    
    return HTTPRequest(
        method=method, 
        path=path, 
        headers=headers, 
        body=body, 
        cookies=cookies
        )