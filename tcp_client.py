import socket

HOST = str(input("Enter private IP address: "))
PORT = int(input("Enter port number eg'9099': "))

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))

socket.send("Hello World!".encode("utf-8"))
print(socket.recv(1024))
