import time
import ping3
from datetime import datetime

# Endereço IP ou nome de host do servidor a ser monitorado
server = 'example.com'

# Função para verificar o status do servidor
def verify_server_status(address: str) -> bool:
    """
    Verifies the status of a server by pinging it.

    :param address: The IP address or hostname of the server to ping
    :return: True if the server is online, False otherwise
    """
    try:
        result = ping3.ping(address)
    except ping3.exceptions.PingError as e:
        print(f"Error pinging {address}: {str(e)}")
        return False

    return result is not None and result >= 0

# Função para imprimir a mensagem de status com um timestamp
def print_status_message(server: str, status: bool):
    """
    Prints the status message with a timestamp.

    :param server: The name of the server
    :param status: True if the server is online, False otherwise
    """
    status_msg = "online" if status else "offline or inaccessible"
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - The server {server} is {status_msg}.")

# Continuously monitor the server's status
while True:
    status = verify_server_status(server)
    print_status_message(server, status)

    # Sleep for 5 seconds before pinging again
    time.sleep(5)
