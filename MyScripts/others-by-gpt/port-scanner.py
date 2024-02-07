import socket

def scan_ports(target_host, target_ports):
    open_ports = []
    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Exemplo de uso:
target_host = "example.com"
target_ports = range(1, 1025)

open_ports = scan_ports(target_host, target_ports)
print(f"Open ports on {target_host}: {open_ports}")
