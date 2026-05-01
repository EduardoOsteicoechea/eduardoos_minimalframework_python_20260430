# ./server/http_html_response.py

def http_html_response(html_body: str) -> str:
    # Ensure the body is treated strictly as a string
    html_body_str = str(html_body)
    
    body_bytes_length = len(html_body_str.encode("utf-8"))
    
    return (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=UTF-8\r\n"
        f"Content-Length: {body_bytes_length}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{html_body_str}"
    )