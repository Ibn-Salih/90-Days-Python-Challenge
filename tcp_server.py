#Topics:
# - Introduction to sockets and networking.
# - Understanding IP addresses, ports, and how to connect to a server.
# - Project:
# - Write a simple TCP client-server application using Python’s socket module.



import socket

# Get the private IP address and port number from the user
HOST = str(input("Enter private IP address: "))
PORT = int(input("Enter port number eg'9099': "))

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server.bind((HOST, PORT))

# Listen for incoming connections
server.listen(5)

print("Listening for incoming connections...")

while True:
    # Accept an incoming connection
    communication_socket, address = server.accept()
    print(f"Connected to {address}")

    # Receive a message from the client
    message = communication_socket.recv(1024).decode("utf8")

    # Send a message back to the client
    communication_socket.send(f"Got your message".encode("utf8"))

    # Close the connection
    communication_socket.close()
    print(f"Connection with {address} ended successfully")


