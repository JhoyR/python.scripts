import socket
from struct import unpack

def packet_sniffer():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, _ = conn.recvfrom(65535)
        dest_mac, src_mac, proto, data = unpack('!6s6sH', raw_data[:14]) + (raw_data[14:],)
        print(f"Source: {src_mac}, Destination: {dest_mac}, Protocol: {socket.htons(proto)}")
        print(f"Data: {data}")

# Uso: packet_sniffer()
