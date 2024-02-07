import socket
from contextlib import closing

def is_valid_host(host):
    """Check if the given host is valid."""
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

def scan_port(target_host, target_port):
    """Scan the given target_port on target_host."""
    try:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(1)
            sock.connect((target_host, target_port))
            return True
    except OSError as e:
        return False

def print_results(results):
    """Print the scan results in a readable format."""
    open_ports = [port for port, is_open in results.items() if is_open]
    if open_ports:
        print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {target_host}.")

if __name__ == "__main__":
    # Define the target (host) and a list of ports to be verified
    target_host = "example.com"
    if not is_valid_host(target_host):
        print(f"Invalid host: {target_host}")
        exit(1)
    target_ports = [80, 443, 22, 21, 25]

    # Scan each port in the list
    results = {port: scan_port(target_host, port) for port in target_ports}

    # Print the results
    print_results(results)