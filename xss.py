# - Learn about XSS attacks and how they occur in web applications.
# - Project:
# - Create a script that detects potential XSS vulnerabilities in a simple web application 
# - by checking for unsanitized user input.


import requests

def check_xss(url):
    # List of simple XSS payloads
    payloads = [
        "<script>alert('XSS');</script>",
        "\"/><script>alert('XSS');</script>",
        "';alert('XSS');//",
        "\";alert('XSS');//",
        "<img src=x onerror=alert('XSS')>"
    ]
    
    vulnerable = False
    
    for payload in payloads:
        # Assume the vulnerable parameter is named 'q'
        params = {"q": payload}
        try:
            response = requests.get(url, params=params, timeout=5)
            # Check if the injected payload appears in the response content as-is.
            if payload in response.text:
                print(f"Potential XSS vulnerability detected with payload: {payload}")
                vulnerable = True
        except requests.RequestException as e:
            print(f"Error during request: {e}")
    
    if not vulnerable:
        print("No potential XSS vulnerabilities detected.")

if __name__ == "__main__":
    # Prompt user for a target URL, which should include a parameter placeholder.
    # For example: http://example.com/search?q=
    target_url = input("Enter target URL (with query parameter, e.g., http://example.com/search?q=): ").strip()
    check_xss(target_url)
