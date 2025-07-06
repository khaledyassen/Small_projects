#!/usr/bin/env python3
# Packages Required
import requests
from bs4 import BeautifulSoup

# Start Coding
if __name__=='__main__':
  # Style for the output
  RESET = "\033[0m"
  BOLD = "\033[1m"
  ITALIC = "\033[3m"
  UNDERLINE = "\033[4m"
  RED = "\033[91m"
  GREEN = "\033[92m"
  YELLOW = "\033[93m"
  BLUE = "\033[94m"
  
  def print_colored_line(line, color):
      print(color + line + RESET)

  Url = 'https://en.wikipedia.org/wiki/Main_Page'
  response = requests.get(Url)
  if response.status_code==200:
    response2 = response.text
    soup = BeautifulSoup(response2, 'html.parser')
    headers = soup.find_all(['h1','h2','h3','h4','h5','h6'])
    print(f'{BOLD}{RED}Here is all headers exists...{RESET}')
    for j,i in enumerate(headers):
      color = BLUE if j % 2 == 0 else YELLOW
      print_colored_line(i.text.strip(), color)