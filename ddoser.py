# - Topics:
# - Understand Distributed Denial-of-Service (DDoS) attacks.
# - Project:
# - Write a basic script that simulates a DDoS attack
# - by sending repeated HTTP requests to a target.

import requests
import threading
import time


TARGET_URL = "http://localhost:8080"  # Target a test server you control
REQUEST_COUNT = 100  # Total requests to send
THREADS = 5           # Simulate multiple clients

def send_request():
    """Send HTTP requests to the target."""
    for _ in range(REQUEST_COUNT // THREADS):
        try:
            requests.get(TARGET_URL, timeout=2)
        except:
            pass  # Ignore errors for simulation

def main():
    print(f"Sending {REQUEST_COUNT} requests to {TARGET_URL}...")
    start_time = time.time()
    
    # Create threads to simulate multiple clients
    threads = []
    for _ in range(THREADS):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Calculate duration
    duration = time.time() - start_time
    print(f"Sent {REQUEST_COUNT} requests in {duration:.2f} seconds.")

if __name__ == "__main__":
    main()