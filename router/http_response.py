# ./server/http_response.py

def http_response(
    body: str, 
    status_code: int = 200, 
    content_type: str = "text/html; charset=UTF-8",
    cookies: list = None
) -> str:
    """
    Builds a complete HTTP response string with dynamic status codes and content types.
    """
    
    # 1. A dictionary to translate numbers into standard HTTP status messages
    status_messages = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error"
    }
    
    # Safely get the message, default to "Unknown" if you pass a weird number
    status_text = status_messages.get(status_code, "Unknown Status")

    body_str = str(body)
    body_bytes_length = len(body_str.encode("utf-8"))
    
    cookie_headers = ""
    if cookies:
        for cookie in cookies:
            cookie_headers += f"Set-Cookie: {cookie}\r\n"
            
    return (
        f"HTTP/1.1 {status_code} {status_text}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {body_bytes_length}\r\n"
        f"{cookie_headers}"
        "Connection: close\r\n"
        "\r\n"
        f"{body_str}"
    )