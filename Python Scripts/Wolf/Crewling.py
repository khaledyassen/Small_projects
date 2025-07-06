import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import init, Fore, Style
import re
import random
import json
# =================================================================================================================================================== #

# Initialize colorama
init()

# Define ANSI escape codes for colors and formatting
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
WHITE = Fore.WHITE
# =================================================================================================================================================== #

random_agents = [
    'Mozilla/5.0 (Linux i686; U; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.51',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
    'Opera/9.64 (Windows NT 6.1; U; MRA 5.5 (build 02842); ru) Presto/2.1.1',
    'Mozilla/5.0 (compatible; Windows; U; Windows NT 6.2; WOW64; en-US; rv:12.0) Gecko/20120403211507 Firefox/12.0',
    'Mozilla/5.0 (Linux i686; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0',
    'Mozilla/5.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b11pre) Gecko/20110126 Firefox/4.0b11pre',
    'Mozilla/5.0 Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.13) Firefox/3.6.13',
    'Mozilla/5.0 (X11; U; Slackware Linux i686; en-US; rv:1.9.0.10) Gecko/2009042315 Firefox/3.0.10',
    'Mozilla/4.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11.0.1245.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.68 Safari/534.30',
    'Mozilla/5.0 (Windows 8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11',
    'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Opera/9.61 (Windows NT 6.0; U; pt-BR) Presto/2.1.1',
    'Mozilla/4.0 (compatible; Intel Mac OS X 10.6; rv:2.0b8) Gecko/20100101 Firefox/4.0b8)',
    'Mozilla/5.0 ArchLinux (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0b11pre) Gecko/20110126 Firefox/4.0b11pre',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'
    ]

# Get the links in the target url using BeautifulSoup
def spider(url):
  try:
    # Send an HTTP request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code != 404:
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
                  print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}")
                else:
                  pass
    else:
        print(f"{BOLD}{RED}URL Not found{RESET}")

  except Exception as e:
    print(f"An error occurred: {e}")
# =================================================================================================================================================== #

# Enumerating paths from the Archive
def Archive_paths(base_url):
  bytes_io = BytesIO()
  try:
    url = f"http://web.archive.org/cdx/search/cdx?url={base_url}/*&output=text&fl=original&collapse=urlkey&filter=statuscode%3A200"
    response = requests.get(url)
    if response.status_code == 200:
        # Print to the console
        print(f"{BOLD}{GREEN}{url}")
        print(f"{BLUE}{UNDERLINE}{bytes_io.getvalue().decode()}{RESET}")
    else:
      print(f"{RED}Something bad happen, check the Archive url")
  except Exception as e:
    print(f"{BOLD}{RED}An error occurred:{WHITE} {e}")
# =================================================================================================================================================== #


# Enumerating paths using custom word list
async def process_path(session, base_url, path):
    full_url = urljoin(base_url, path)
    async with session.get(full_url) as response:
        if response.status != 404:
            print_status(full_url, response.status)
        await asyncio.sleep(0.5)

def print_status(full_url, status_code):
    if status_code == 200:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {GREEN}{status_code}")
    elif status_code in {302, 301, 307}:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {MAGENTA}{status_code}")
    elif status_code in {403, 401}:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {YELLOW}{status_code}")
    elif status_code == 405:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {WHITE}{status_code} Method Not Allowed")
    else:
        print(f"{BOLD}{BLUE}{UNDERLINE}{full_url}{RESET} {RED}{status_code}")

async def enumerate_paths(base_url, paths, requests_per_second, delay_between_threads):
    try:
        async with aiohttp.ClientSession() as session:
            # Control the number of requests per second
            for path in paths:
                await asyncio.gather(process_path(session, base_url, path))
                await asyncio.sleep(1 / requests_per_second)  # Introduce delay based on requests per second

                # Introduce delay between threads
                await asyncio.sleep(delay_between_threads)

    except Exception as e:
        print(f"{BOLD}{RED}An error occurred:{WHITE} {e}")

# # Example usage
# base_url = "http://localhost"
# paths_file = "path_list.txt"
# requests_per_second = float(input("Enter number of requests per second: "))
# delay_between_threads = float(input("Enter delay between threads (in seconds): "))

"""#  [add it to the main function]
with open(paths_file, 'r') as file:
    paths = [path.strip() for path in file.readlines()]

# Run the event loop to execute asynchronous code [add it to the main function]
asyncio.run(enumerate_paths(base_url, paths, requests_per_second, delay_between_threads))
"""

if __name__=='__main__':
  bytes_io = BytesIO()
  header = {'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent':'df','Referer': 'Add here the target URL'}
  base_url = "http://localhost"
  paths_file = "common.txt"
  requests_per_second = float(input("Enter number of requests per second: "))
  delay_between_threads = float(input("Enter delay between threads (in seconds): "))
  user_agent = input("Enter your custom user agent")
  
  print(header)
  header2 = input("Enter header  ")
  # Convert headers and cookies to dictionaries if provided
  try:
    if header2:
      headers = json.loads(header2)
    else:
      headers = header
  except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
    print("Invalid input for dictionary. Please enter a valid JSON-formatted dictionary.")
    exit()
  except ValueError as ve:
    print(ve)
    exit()
  # enumerate_paths(base_url, paths_file)
  # Archive_paths(base_url)
  # spider(base_url)
