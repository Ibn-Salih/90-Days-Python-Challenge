# - Topics:
# - Learn how to use Nmap for network scanning and discovering open ports.
# - Project:
# - Write a Python script that automates Nmap scans 
# and stores the results in a file or database.




import nmap
import sqlite3
import datetime
import xml.etree.ElementTree as ET
import json

def run_nmap_scan(target, ports='1-1000', arguments='-sV'):
    """Run an Nmap scan and return results."""
    scanner = nmap.PortScanner()
    print(f"Scanning {target} on ports {ports}...")
    
    try:
        scanner.scan(target, ports, arguments=arguments)
        return scanner
    except nmap.PortScannerError as e:
        print(f"Error: {e}")
        return None

def save_to_xml(scanner, filename):
    """Save scan results to an XML file."""
    if not scanner:
        return
    with open(filename, 'w') as f:
        f.write(scanner.get_nmap_last_output().decode('utf-8'))
    print(f"Results saved to {filename}")

def save_to_json(scanner, filename):
    """Save scan results to a JSON file."""
    if not scanner:
        return
    scan_data = {}
    for host in scanner.all_hosts():
        scan_data[host] = {
            'status': scanner[host].state(),
            'protocols': list(scanner[host].all_protocols()),
            'ports': {port: scanner[host]['tcp'][port] for port in scanner[host]['tcp']}
        }
    with open(filename, 'w') as f:
        json.dump(scan_data, f, indent=4)
    print(f"Results saved to {filename}")

def save_to_database(scanner, db_name='scan_results.db'):
    """Save results to a SQLite database."""
    if not scanner:
        return
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY,
            target TEXT,
            port INTEGER,
            service TEXT,
            version TEXT,
            timestamp DATETIME
        )
    ''')
    
    timestamp = datetime.datetime.now()
    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                service = scanner[host][proto][port]['name']
                version = scanner[host][proto][port]['version']
                cursor.execute('''
                    INSERT INTO scans (target, port, service, version, timestamp)
                    VALUES (?, ?, ?, ?, ?)
                ''', (host, port, service, version, timestamp))
    
    conn.commit()
    conn.close()
    print(f"Results saved to database: {db_name}")

def main():
    # User input
    target = input("Enter target IP/hostname: ").strip()
    ports = input("Enter port range (default: 1-1000): ").strip() or '1-1000'
    
    # Run scan
    scanner = run_nmap_scan(target, ports)
    if not scanner:
        return
    
    # Save results
    save_to_xml(scanner, f"{target}_scan.xml")
    save_to_json(scanner, f"{target}_scan.json")
    
    # Optional: Save to database
    if input("Save to database? (y/n): ").lower() == 'y':
        save_to_database(scanner)

if __name__ == "__main__":
    main()