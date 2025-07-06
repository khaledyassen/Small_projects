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

  Url = "https://data.gov/"
  try:
    response = requests.get(Url)
    if response.status_code == 200:
      response2 = response.text
      soup = BeautifulSoup(response2, 'html.parser')
      specific_tag = soup.find('span', class_='text-color-red')
      if specific_tag:
        print(f"{BOLD}{YELLOW}{specific_tag.text}{RESET}{BOLD} datasets numbers..")
      else:
        print(f"{BOLD}{RED}Tag not found")
    else:
      print(f"{BOLD}{RED}404 Not Found")
  except requests.exceptions.ConnectionError as e:
    print(f"Error while making the request: {BOLD}{BLUE}Can not connect to the target.")
    exit(1)