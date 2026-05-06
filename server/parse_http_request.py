from server.HTTPRequest import HTTPRequest
from server.deserialize_http_request import deserialize_http_request


def parse_http_request(client_connection) -> HTTPRequest:
    """Safely reads an HTTP request from a socket and returns an HTTPRequest object."""
    raw_data = b""
    while b"\r\n\r\n" not in raw_data:
        chunk = client_connection.recv(4096)
        if not chunk:
            return None
        raw_data += chunk
    parts = raw_data.split(b"\r\n\r\n", 1)
    raw_headers = parts[0]
    raw_body = parts[1] if len(parts) > 1 else b""    
    headers_text = raw_headers.decode("utf-8", errors="replace")
    content_length = 0
    for line in headers_text.split("\r\n"):
        if line.lower().startswith("content-length:"):
            content_length = int(line.split(":")[1].strip())
            break
    while len(raw_body) < content_length:
        chunk = client_connection.recv(4096)
        if not chunk:
            break
        raw_body += chunk
    return deserialize_http_request(raw_headers, raw_body)