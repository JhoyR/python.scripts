import ssl
import socket

def check_ssl_certificate(hostname, port):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            # Realize verificações adicionais conforme necessário

# Exemplo de uso:
target_host = "example.com"
target_port = 443
check_ssl_certificate(target_host, target_port)
