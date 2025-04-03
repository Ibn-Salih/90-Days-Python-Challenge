# - Topics:
# - Understand how honeypots work and how they are used to detect attackers.
# - Project:
# - Build a simple honeypot in Python that simulates a vulnerable service
#  and logs all incoming attempts to exploit it.



import socket
import threading
from datetime import datetime

# Configuration
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 2222        # Default SSH port is 22, but we use 2222 to avoid conflicts
LOG_FILE = 'honeypot.log'
BANNER = "SSH-2.0-OpenSSH_7.9p1 Ubuntu-10ubuntu2.1\r\n"  # Fake SSH banner

def handle_connection(client_socket, client_ip):
    """Handle incoming connection attempts"""
    try:
        # Send fake SSH banner
        client_socket.send(BANNER.encode())
        
        # Log connection details
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - Connection from {client_ip}\n"
        
        # Simulate authentication attempt
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Log credentials if provided
            if b"ssh-user" in data.lower() or b"password" in data.lower():
                log_entry += f"Attempted credentials: {data.decode(errors='ignore').strip()}\n"
            
            # Send fake error
            client_socket.send(b"Permission denied, please try again.\r\n")
    
    except Exception as e:
        log_entry += f"Error: {str(e)}\n"
    finally:
        client_socket.close()
        with open(LOG_FILE, 'a') as f:
            f.write(log_entry + "\n")
        print(f"Logged attack from {client_ip}")

def start_honeypot():
    """Main honeypot server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    
    print(f"[*] Honeypot running on {HOST}:{PORT}")
    print(f"[*] Logging to {LOG_FILE}")
    
    try:
        while True:
            client_socket, addr = server.accept()
            client_ip = addr[0]
            print(f"[!] New connection from {client_ip}")
            
            # Handle each connection in a new thread
            threading.Thread(
                target=handle_connection,
                args=(client_socket, client_ip)
            ).start()
    except KeyboardInterrupt:
        print("\n[!] Shutting down honeypot")
        server.close()

if __name__ == "__main__":
    # Create log file header
    with open(LOG_FILE, 'a') as f:
        f.write("\n" + "="*50 + "\n")
        f.write(f"Honeypot started at {datetime.now()}\n")
        f.write("="*50 + "\n\n")
    
    start_honeypot()