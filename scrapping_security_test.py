# - Topics:
# - Learn how to scrape data from websites for security testing purposes.
# - Use requests and BeautifulSoup to gather publicly available information.
# - Project:
# - Build a scraper that collects metadata from websites 
# - to identify potential attack surfaces (e.g., outdated software versions).

import requests
from bs4 import BeautifulSoup
import re

# Step 1: Fetch Page Content
def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/115.0"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Step 2: Extract Server Headers
def get_server_headers(response):
    headers = response.headers
    security_headers = ["Server", "X-Powered-By", "X-AspNet-Version"]
    return {k: headers.get(k) for k in security_headers if headers.get(k)}

# Step 3: Parse HTML for Software Versions
def parse_versions(html):
    soup = BeautifulSoup(html, "html.parser")
    meta_data = {}

    # Check generator meta tags (common in CMS)
    generator = soup.find("meta", {"name": "generator"})
    if generator:
        meta_data["generator"] = generator.get("content")

    # Look for jQuery versions in script tags
    scripts = soup.find_all("script", src=re.compile(r"jquery.*\.js"))
    for script in scripts:
        if "src" in script.attrs:
            meta_data["jquery"] = script["src"].split("/")[-1]

    return meta_data

# Step 4: Check Common Files
def check_common_files(url):
    common_files = [
        "/CHANGELOG.txt",   # Drupal/WordPress
        "/wp-config.php",   # WordPress
        "/package.json"     # Node.js apps
    ]
    found_files = []
    for file in common_files:
        response = requests.get(url + file, allow_redirects=False)
        if response.status_code == 200:
            found_files.append(file)
    return found_files

# Step 5: Full Workflow
def analyze_site(url):
    response = fetch_page(url)
    if not response:
        return
    
    # Collect headers
    headers = get_server_headers(response)
    print("Server Headers:", headers)

    # Parse HTML for versions
    html_versions = parse_versions(response.text)
    print("HTML Metadata:", html_versions)

    # Check sensitive files
    exposed_files = check_common_files(url)
    print("Exposed Files:", exposed_files)

# Example usage
if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g., https://example.com): ")
    analyze_site(target_url)