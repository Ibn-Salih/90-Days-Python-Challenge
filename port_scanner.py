# Topics:
# - Learn how to scan open ports on a target machine using socket module.
# - Project:
# - Build a basic port scanner that checks if a port is open on a target server.


import socket, ipaddress
from concurrent.futures import ThreadPoolExecutor

def validate_target(target):
    """
    Validate the target by checking if it is a valid IP address or domain name.
    """
    try:
        ipaddress.ip_address(target)
        return target
    except ValueError:
        try:
            socket.gethostbyname(target)
            return target
        except socket.gaierror:
            print("Invalid target, please enter a valid target address")
            return None
        

def scan_port(target,port):
    """
    Scan the given port on the target to see if it is open.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex(target, port)
            if result == 0:
                return port
    except Exception:
        pass
    return None

# Save result to file
def save_result(open_ports, target):
    """
    Save the open ports to a file named open_ports{target}.txt
    """
    filename = f"open_ports{target}.txt"
    with open(filename, 'w') as file:
        for port in open_ports:
            file.writelines(f"Port {port} is open")
        print(f"\nResults saved to {filename}")

        


def main():
    """
    Main function to interact with the user and start the port scanner.
    """
    target = input("Enter ip-address of target or hostname: ")
    validate_target(target)
    if not target:
        return
    try:  
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Please enter a valid port range")
            return
    except ValueError as e:
        print(f"Invalid input, please enter a numeric value. {e}")
        return
    print(f"Scanning ports {start_port}-{end_port} on {target}...\n")

    #Using multithreading to scan ports
    open_ports = []
    with ThreadPoolExecutor(max_workers=40) as executor:
        futures = {executor.submit(scan_port, target, port): port for port in range(start_port, end_port+1)}
        for future in futures:
            port = future.result()
            if port:
                print(f"Port {port} is open")
                open_ports.append(port)

    #Summary of results
    if open_ports:
        print("\nOpen ports:")
        for port in open_ports:
            print(f"Port {port}")
        save = input("Save results to file? (y/n): ")
        if save.lower() == "y":
            save_result(open_ports, target)
    else:
        print("No open ports found")

    print("\nScan complete")



if __name__ == "__main__":
    main()
