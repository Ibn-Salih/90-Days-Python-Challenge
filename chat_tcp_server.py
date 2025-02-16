# - Introduction to socket programming for network communication.
# - Project:
# - Build a simple chat application using sockets.
# - This will give you a basic understanding of networking principles.


# tcp_server.py
import socket
import threading

def handle_client(client_socket, address):
    """
    Handle a single client connection. This function is run in a separate
    thread for each client connection. It receives messages from the client,
    prints them, and broadcasts them to other connected clients.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"{address}: {message}")
            # TODO: Broadcast to other clients (add logic here)
        except:
            break
    client_socket.close()

def main():
    """
    Create a TCP server socket and start listening for incoming connections.
    For each incoming connection, create a new thread to handle the client.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))
    server.listen(5)
    print("TCP Server listening on port 12345...")

    while True:
        client_socket, address = server.accept()
        print(f"Connected to {address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    main()
