import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def enumerate_url(url):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (links) on the page
            links = soup.find_all('a')

            # Enumerate links
            for link in links:
                href = link.get('href')
                if href:
                    full_url = urljoin(url, href)
                    domain = re.search(r'https?://([^/]+)', url).group(1) if re.search(r'https?://([^/]+)', url) else None
                    if domain in full_url:
                      print(full_url)
                    else:
                      pass
        else:
            pass

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__=='__main__':
    enumerate_url("http://example.com")