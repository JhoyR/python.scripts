import requests

def web_vuln_scanner(url):
    payloads = ["' OR '1'='1", "<script>alert('XSS')</script>"]

    for payload in payloads:
        try:
            response = requests.get(url, params={"param": payload})
            response.raise_for_status()
            if payload in response.text:
                print(f"Vulnerability found: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Uso: web_vuln_scanner('https://example.com')
