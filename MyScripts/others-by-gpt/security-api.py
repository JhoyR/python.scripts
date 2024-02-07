import requests

def api_security_check(api_url):
    # Realize verificações de segurança específicas para APIs
    response = requests.get(api_url)
    if response.status_code == 200:
        print("API is accessible")
        # Adicione mais verificações conforme necessário
    else:
        print(f"API is not accessible. Status code: {response.status_code}")

# Exemplo de uso:
api_url = "https://api.example.com"
api_security_check(api_url)
