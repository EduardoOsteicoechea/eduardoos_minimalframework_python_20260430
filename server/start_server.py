import socket
from server.handle_request_route import handle_request_route

def start_server(host="127.0.0.1", port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(5) # Allow a small backlog
        print(f"Raw API listening on http://{host}:{port} ...")

        while True:
            client_connection, client_address = server_socket.accept()
            print(f"\n[+] Connection received from {client_address}")
            
            with client_connection:
                try:
                    # Set a timeout so the socket doesn't hang forever if Caddy keeps it alive
                    client_connection.settimeout(2.0)
                    
                    print("    -> Waiting for request data...")
                    # 8192 is large enough to catch all proxy headers in one go
                    request_data = client_connection.recv(8192).decode("UTF-8")
                    
                    if not request_data:
                        print("    -> [!] Empty request data, skipping.")
                        continue
                        
                    print(f"    -> Request received ({len(request_data)} bytes). Routing...")
                    
                    # Call your router (which should return the output of http_html_response)
                    final_payload = handle_request_route(request_data)
                    
                    print(f"    -> Route handled. Sending payload ({len(final_payload)} bytes)...")
                    client_connection.sendall(final_payload.encode("utf-8"))
                    print("    -> [✓] Response sent successfully.")
                    
                except socket.timeout:
                    print("    -> [!] Socket timed out waiting for data.")
                except Exception as e:
                    print(f"    -> [!] Socket error: {e}")