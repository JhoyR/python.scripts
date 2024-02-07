import scapy.all as scapy

def sniff_packets(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        print(packet.show())

# Exemplo de uso:
sniff_packets("eth0")  # Substitua "eth0" pela sua interface de rede
