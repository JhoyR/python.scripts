import requests
import os

# URL do site a ser verificado
url = os.environ.get("VERIFY_URL", "https://github.com/hclproducts/AltoroJ")

# Parâmetro de teste de injeção SQL
injection_payload = os.environ.get("INJECTION_PAYLOAD", "' OR '1'='1")

# Enviar uma solicitação GET para a URL com o parâmetro de injeção
try:
    response = requests.get(url, params={"username": injection_payload, "password": injection_payload})
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
    exit(1)

# Verificar se o código de status indica um erro de servidor (500) ou sucesso (200)
if response.status_code == 500:
    print("Vulnerability of SQL injection detected.")
elif response.status_code == 200:
    print("No SQL injection vulnerabilities were found.")
else:
    print(f"Unexpected status code: {response.status_code}")
