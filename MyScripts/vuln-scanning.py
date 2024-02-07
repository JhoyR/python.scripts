import requests
from bs4 import BeautifulSoup

# List of URLs to be checked
urls = ["http://localhost:4200/Thanks", "http://localhost:4200"]

# Dictionary of known vulnerabilities
vulnerabilities = {
    "CVE-2019-12345": {"description": "SQL Injection", "severity": "high"},
    "CVE-2020-6789": {"description": "Cross-Site Scripting (XSS)", "severity": "high"},
    "CVE-2018-5432": {"description": "Cross-Site Request Forgery (CSRF)", "severity": "medium"},
    "CVE-2017-8765": {"description": "Deserialization Vulnerabilities", "severity": "medium"},
    "CVE-2021-3456": {"description": "Authentication and Authorization Vulnerabilities", "severity": "high"},
    "CVE-2016-7890": {"description": "Session Management Vulnerabilities", "severity": "medium"},
    "CVE-2015-4321": {"description": "Sensitive Data Exposure", "severity": "high"},
    "CVE-2014-5678": {"description": "Web Server Vulnerabilities", "severity": "medium"},
    "CVE-2023-1111": {"description": "Library and Framework Vulnerabilities", "severity": "high"},
}

# Function to get the page title
def get_title(soup):
    try:
        return soup.html.head.title.string
    except AttributeError:
        return None

# Function to check for vulnerabilities
def check_vulnerabilities(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
        return
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error for {url}: {e}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    title = get_title(soup)

    if response.status_code == 200:
        print(f"Checking {url} ({title})")
    else:
        print(f"Skipping {url} (non-200 status code)")
        return

    for vuln, details in vulnerabilities.items():
        if vuln in response.text:
            print(f"Vulnerability found in {url}: {details['description']} ({vuln}), severity: {details['severity']}")
    else:
        print(f"No vulnerabilities found in {url} ({title})")

# Check each URL in the list
for url in urls:
    check_vulnerabilities(url)