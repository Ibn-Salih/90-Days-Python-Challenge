# - Topics:
# - Learn how firewalls work and how to implement simple filtering rules.
# - Project:
# - Write a basic firewall that filters incoming connections
# - based on IP address and port.



import socket

# Define firewall rules: (IP, Port, Action)
FIREWALL_RULES = [
    # Block specific IPs
    ("192.168.1.100", None, "block"),  # Block all traffic from 192.168.1.100
    ("192.168.1.101", 22, "block"),    # Block SSH (port 22) from 192.168.1.101
    # Allow specific IPs
    ("192.168.1.200", None, "allow"),  # Allow all traffic from 192.168.1.200
    ("192.168.1.201", 80, "allow"),    # Allow HTTP (port 80) from 192.168.1.201
]

def evaluate_rules(client_ip, client_port):
    """Evaluate firewall rules for a given IP and port."""
    for rule_ip, rule_port, action in FIREWALL_RULES:
        # Check if the IP matches
        if rule_ip == client_ip:
            # Check if the port matches (or rule applies to all ports)
            if rule_port is None or rule_port == client_port:
                return action  # Return the action (allow/block)
    return "allow"  # Default action if no rules match

def start_firewall(host='0.0.0.0', port=8080):
    """Start a basic firewall that filters incoming connections."""
    # Create a socket to listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Firewall running on {host}:{port}...")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        client_ip, client_port = client_address

        # Evaluate firewall rules
        action = evaluate_rules(client_ip, client_port)

        if action == "block":
            print(f"Blocked connection from {client_ip}:{client_port}")
            client_socket.close()  # Close the connection
        else:
            print(f"Allowed connection from {client_ip}:{client_port}")
            # Handle the connection (e.g., forward to a server)
            client_socket.send(b"Connection allowed by firewall.\n")
            client_socket.close()

if __name__ == "__main__":
    start_firewall()