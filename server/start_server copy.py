import socket
from server.handle_request_route import handle_request_route


def start_server(host="127.0.0.1", port=8080):
    # 1. CREATE the socket instance first
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # 2. CONFIGURE the socket instance
        # Prevent the "Address already in use" error when restarting rapidly
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the server to the network interface and port
        server_socket.bind((host, port))

        # Tell the OS to start listening for incoming connections
        server_socket.listen(1)
        print(f"Raw API listening on http://{host}:{port} ...")

        # Set the Infinite Event Loop
        while True:
            # The script completely pauses until a client connects
            client_connection, client_address = server_socket.accept()

            with client_connection:
                try:
                    request_data = client_connection.recv(1024).decode("UTF-8")
                    if not request_data:
                        continue

                    final_payload = handle_request_route(request_data)
                    client_connection.sendall(final_payload.encode("utf-8"))
                except Exception as e:
                    print(f"Socket error: {e}"),
