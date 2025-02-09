# - Topics:
# - Learn how to capture and analyze network packets using the scapy library.
# - Project:
# - Write a Python script that captures 
# - and displays the details of network packets on your local network.

from scapy.all import sniff, TCP, IP, Raw

# Define a function to process each packet
def process_packet(packet):
    # Check if the packet has a TCP layer
    if packet.haslayer(TCP):
        # Extract the source and destination IP addresses
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Extract the source and destination ports
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        
        # Check if the packet has a Raw layer (i.e., payload)
        if packet.haslayer(Raw):
            # Extract the payload
            payload = packet[Raw].load
            
            # Print the packet details
            print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")
            print(f"Source Port: {src_port}, Destination Port: {dst_port}")
            print(f"Payload: {payload}\n")
    
# Start sniffing packets
sniff(prn=process_packet, store=False)

