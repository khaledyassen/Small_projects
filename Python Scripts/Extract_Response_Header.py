from colorama import Fore, Style, init
import requests
import csv


# Initialize colorama
init()

# Define color constants
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RED = Fore.RED
WHITE = "\033[97m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

if __name__=='__main__':
  url = input(f"{BOLD}{GREEN}Give me the url to extract the reponse headers? {BLUE}")
  try:
    response = requests.get(url)
    print(f"{BLUE}Status code value is {YELLOW}{response.status_code}")
    print(f"{BLUE}All headers value is {YELLOW}{response.headers}")
    print(f"{BLUE}URL header value is {YELLOW}{response.url}")
    print(f"{BLUE}History header value is {YELLOW}{response.history}")
    print(f"{BLUE}Encoding header value is {YELLOW}{response.encoding}")
    print(f"{BLUE}Reason header value is {YELLOW}{response.reason}")
    print(f"{BLUE}Cookie header value is {YELLOW}{response.cookies}")
    print(f"{BLUE}Elapsed header value is {YELLOW}{response.elapsed}")
    print(f"{BLUE}Request header value is {YELLOW}{response.request}")
    print(f"{BLUE}Content header value is {YELLOW}{response.content}")
  except:
    print(f"{BOLD}{RED}There is something error try again later..")