#Topics:
# - Introduction to sockets and networking.
# - Understanding IP addresses, ports, and how to connect to a server.
# - Project:
# - Write a simple TCP client-server application using Python’s socket module.


import socket

HOST = str(input("Enter private IP address: "))
PORT = int(input("Enter port number eg'9099': "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode("utf8")
    communication_socket.send(f"Got your message".encode("utf8"))
    communication_socket.close()
    print(f"Connection with {address} ended successfully")


