import socket

# Get the private IP address and port number from the user
HOST = str(input("Enter private IP address: "))
PORT = int(input("Enter port number eg'9099': "))

# Create a socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
socket.connect((HOST, PORT))

# Send a message to the server
socket.send("Hello World!".encode("utf-8"))

# Receive a message from the server and print it
print(socket.recv(1024))
