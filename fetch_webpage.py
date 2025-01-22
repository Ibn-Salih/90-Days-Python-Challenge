# - Understanding HTML structure and HTTP request/response cycle.
# - Inspecting web traffic using browser dev tools.
# - Project:
# - Build a simple HTTP request handler in Python to fetch 
# and display the content of a webpage.

import requests

url = input("Enter URL: ")

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"HTTP error: {response.status}")
