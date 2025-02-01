# - Topics:
# - Understand HTTP headers and how they can reveal vulnerabilities.
# - Project:
# - Write a script that fetches HTTP headers from a target URL 
# -and checks for common security misconfigurations (e.g., missing Strict-Transport-Security header).

'''
  1 - Implementing the Script's Logic
  2 - User Input: Accept a target URL.
  3 - Send Request: Fetch headers using an HTTP request.
  4 - Check Security Headers:
  5 - Print missing headers.
  6 - Suggest fixes.
  7 - Display Findings:
  8 - If headers are misconfigured, alert the user.
  9 - If headers are present but weak, suggest improvements.
'''

import requests

def user_url():
    """
    Get the target URL from the user
    """
    url = input("Enter the URL: ")
    response = requests.get(url)
    headers = response.headers
    return headers,url

def check_security(headers,url):    
    """
    Check for missing security headers and print findings
    """
    print(f"Scanning security headers of {url}...\n")
    if  "Strict-Transport-Security" not in headers:
        # Strict-Transport-Security header is missing
        print("Missing Strict-Transport-Security header,\nEnable HSTS\nFIX:Strict-Transport-Security: max-age= 31536000; includeSubDomains") 
    if "Content-Security-Policy" not in headers:
        # Content-Security-Policy header is missing
        print("Missing Content-Security-Policy header,\nEnable Content Security Policy\nFIX:Content-Security-Policy: default-src 'self';") 
    if "X-Content-Type-Options" not in headers:
        # X-Content-Type-Options header is missing
        print("Missing X-Content-Type-Options header,\nEnable X-Content-Type-Options\nFIX:X-Content-Type-Options: nosniff")
    if "X-Frame-Options" not in headers:
        # X-Frame-Options header is missing
        print("Missing X-Frame-Options header,\nEnable X-Frame-Options\nFIX:X-Frame-Options: DENY")
    if "X-XSS-Protection" not in headers:    
        # X-XSS-Protection header is missing
        print("Missing X-XSS-Protection header,\nEnable X-XSS-Protection\nFIX:X-XSS-Protection: 1; mode=block\n")
    print("*"*50)
    print("\nHeader Detail")
    # Print all headers and their values
    for header, value in headers.items():
        print(f"{header}: {value}")

if __name__ == "__main__":
    headers, url = user_url()
    security = check_security(headers,url)
