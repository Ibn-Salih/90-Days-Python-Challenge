# - Topics:
# - Learn about robots.txt in website and how to access them
# - Project:
# - Write a Python script that retrieves and analyzes robots.txt of a website 
# - and save the results to a file




import requests
from datetime import datetime
from urllib.parse import urlparse

def get_robots_txt(url):
    """Fetch robots.txt content from a given domain."""
    try:
        # Ensure the URL starts with http:// or https://
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        # Parse the URL to extract the domain
        parsed_url = urlparse(url)
        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
        
        # Send a GET request to fetch robots.txt
        response = requests.get(robots_url, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)
        
        return response.text  # Return the content of robots.txt
    except requests.exceptions.RequestException as e:
        print(f"Error fetching robots.txt: {e}")
        return None

def analyze_robots(content):
    """Parse and analyze the content of robots.txt."""
    analysis = {
        'disallowed': [],  # List of disallowed paths
        'allowed': [],     # List of allowed paths
        'sitemaps': [],    # List of sitemap URLs
        'wildcards': False,  # Flag for wildcard rules
        'sensitive_paths': []  # List of sensitive paths (e.g., /admin, /login)
    }
    
    # Keywords to identify sensitive paths
    sensitive_keywords = ['admin', 'login', 'wp-admin', 'config', 'sql', 'backup']
    
    # Iterate through each line in robots.txt
    for line in content.splitlines():
        line = line.strip()  # Remove leading/trailing whitespace
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            continue
        
        # Check for Disallow rules
        if line.lower().startswith('disallow:'):
            path = line.split(': ')[1].strip()  # Extract the disallowed path
            analysis['disallowed'].append(path)
            
            # Check for wildcards in the path
            if '*' in path:
                analysis['wildcards'] = True
            
            # Check if the path contains sensitive keywords
            if any(keyword in path for keyword in sensitive_keywords):
                analysis['sensitive_paths'].append(path)
        
        # Check for Allow rules
        elif line.lower().startswith('allow:'):
            analysis['allowed'].append(line.split(': ')[1].strip())
        
        # Check for Sitemap entries
        elif line.lower().startswith('sitemap:'):
            analysis['sitemaps'].append(line.split(': ')[1].strip())
    
    return analysis

def save_results(domain, analysis):
    """Save the analysis results to a timestamped file."""
    # Generate a timestamp for the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{domain}_robots_analysis_{timestamp}.txt"
    
    # Write the analysis results to the file
    with open(filename, 'w') as file:
        file.write(f"Robots.txt Analysis for {domain}\n{'='*30}\n")
        file.write(f"Disallowed paths: {len(analysis['disallowed'])}\n")
        file.write(f"Allowed paths: {len(analysis['allowed'])}\n")
        file.write(f"Sitemaps found: {len(analysis['sitemaps'])}\n\n")
        
        # Write critical findings
        file.write("Critical Findings:\n")
        if analysis['wildcards']:
            file.write("- Wildcard (*) rules detected (broad restrictions).\n")
        if analysis['sensitive_paths']:
            file.write("- Sensitive paths exposed:\n")
            for path in analysis['sensitive_paths']:
                file.write(f"  - {path}\n")
        
        # Write full details
        file.write("\nFull Details:\n")
        file.write("\nDisallowed Paths:\n" + '\n'.join(analysis['disallowed']))
        file.write("\n\nSitemaps:\n" + '\n'.join(analysis['sitemaps']))
    
    print(f"Results saved to {filename}")

def main():
    """Main function to execute the script."""
    # Prompt the user for a domain
    domain = input("Enter website domain (e.g., example.com): ").strip()
    
    # Fetch the robots.txt content
    content = get_robots_txt(domain)
    
    # If robots.txt is not found or cannot be fetched, exit
    if not content:
        print("No robots.txt found or unable to fetch.")
        return
    
    # Analyze the robots.txt content
    analysis = analyze_robots(content)
    
    # Save the analysis results to a file
    save_results(domain, analysis)

if __name__ == "__main__":
    main()