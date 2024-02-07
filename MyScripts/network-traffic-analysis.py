import pcapy
from impacket.ImpactDecoder import EthDecoder

# Interface to monitor (replace with the name of your interface)
interface = "eth0"

try:
    # Open the capture device
    capture_device = pcapy.open_live(interface, 65536, 1, 0)
except pcapy.PcapError as e:
    print(f"Error opening interface {interface}: {e}")
    exit()

# Initialize the Ethernet decoder
eth_decoder = EthDecoder()

# Capture and analyze packets in a loop
with capture_device as cap:
    while True:
        # Capture a packet
        header, packet = cap.next()

        # Decode the packet
        eth_packet = eth_decoder.decode(packet)

        # Extract information from the Ethernet header
        src_mac = eth_packet.get_ether_shost()
        dest_mac = eth_packet.get_ether_dhost()

        # Print the MAC addresses
        print(f"Source MAC address: {src_mac}")
        print(f"Destination MAC address: {dest_mac}")