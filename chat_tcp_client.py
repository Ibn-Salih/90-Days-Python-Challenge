# Topics:
# - Learn how to create both TCP and UDP clients and servers.
# - Introduction to socket programming for network communication.
# - Project:
# - Build a simple chat application using sockets.
# - This will give you a basic understanding of networking principles.



# tcp_client.py
import socket
import threading
# Create a new socket object for the client.
# AF_INET is the address family for IPv4
# SOCK_STREAM is the socket type for TCP
def receive_messages(client_socket):
    # Receive messages from the server and print them.
    # This will run in an infinite loop until the connection is closed.
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(f"\nReceived: {message}")
        except:
            # If there's an error, break the loop and close the connection.
            break

def main():
    # Create the client socket.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server on localhost, port 12345.
    client.connect(("localhost", 12345))

    # Create a new thread for receiving messages from the server.
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    # Start the thread.
    receive_thread.start()

    # Send messages to the server.
    while True:
        # Get the message from the user.
        message = input("Your message: ")
        # Send the message.
        client.send(message.encode())

if __name__ == "__main__":
    # Call main() when the script is run directly.
    main()
