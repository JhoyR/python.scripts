import re

def monitor_log_for_bruteforce(log_file):
    with open(log_file, 'r') as file:
        log_content = file.read()

    failed_login_attempts = re.findall(r'Failed login attempt from (.+)', log_content)
    unique_ip_addresses = set(failed_login_attempts)

    if len(failed_login_attempts) > 10:
        print("Possible brute force attack detected!")
        print(f"Unique IP addresses: {', '.join(unique_ip_addresses)}")

# Exemplo de uso:
log_file_path = "/var/log/auth.log"  # Substitua pelo caminho do seu arquivo de log
monitor_log_for_bruteforce(log_file_path)
