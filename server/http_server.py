import socket

from handlers.handle_exception import handle_exception
from server.parse_http_request import parse_http_request
from router.router import router


def http_server(host="127.0.0.1", port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"[*] Server listening on http://{host}:{port} ...")
        print("[*] Press Ctrl+C to stop the server.")
        try:
            while True:
                client_connection, client_address = server_socket.accept()
                print(f"\n[+] Connection received from {client_address}")
                with client_connection:
                    client_connection.settimeout(5.0)
                    try:
                        print("    -> Waiting for request data...")
                        request_object = parse_http_request(client_connection)
                        if not request_object:
                            print("    -> [!] Empty or broken request, skipping.")
                            continue
                        else:
                            print(f"    -> Request parsed: {request_object.method} {request_object.path}. Routing...")
                            response_data = router(request_object)
                            print(f"    -> Route handled. Sending payload...")
                            client_connection.sendall(response_data.encode("utf-8"))
                            print("    -> [✓] Response sent successfully.")
                    except socket.timeout:
                        print("    -> [!] Socket timed out waiting for data.")
                    except Exception as e:
                        print(
                            f"    -> [!] Socket error processing client: {e}")
                        handle_exception(e)
        except KeyboardInterrupt:
            print("\n[*] Server shutting down gracefully...")
