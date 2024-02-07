import requests
from bs4 import BeautifulSoup

# Define the URL
url = 'https://avaltransportadora.com.br'

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all links with 'href' attribute
        links = soup.find_all('a', href=True)

        # Print the extracted links
        for link in links:
            print(link['href'])
    else:
        print(f"Request failed with status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")