from io import BytesIO
from lxml import etree
import requests
import sys
import random
from colorama import init, Fore, Style

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


url = input(f"{BOLD}{BLUE}Give me the URl? {YELLOW}")


r = requests.get(url)

content = r.content

parse = etree.HTMLParser()

content = etree.parse(BytesIO(content),parser=parse)

for link in content.findall('//a'):
    print(f"{link.get('href')}")


'''
Another way using  "BeautifulSoup" module

   soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', href=True):
        print(link['href'])
'''
