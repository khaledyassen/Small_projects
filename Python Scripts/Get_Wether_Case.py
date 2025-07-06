#!/usr/bin/env python3
# Packages Required
import requests
from bs4 import BeautifulSoup
import argparse , textwrap
import json
import os

# Style for the output
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

if __name__=='__main__':
  print(f"{GREEN}You must know that you need Valid City key{RESET}")
  city = input(f"{BLUE}City Value:{YELLOW} ")
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=79464a23e43db158ecc524f85dc1590a"
  print(f"Checking the {BLUE}{url} ..")

  try:
    snt = requests.get(url)
    if snt.status_code==200:
      json_value = snt.text
      json_v = json.loads(json_value)
      print(f"{YELLOW}The temperature betweeen {GREEN}{json_v['coord']['lon']} {YELLOW}-{GREEN} {json_v['coord']['lat']}")
      print(f"{YELLOW}The Speed is {GREEN}{json_v['wind']['speed']}")
      print(f"{YELLOW}The Description is {GREEN}{json_v['weather'][0]['description']}")
      # print(json_value)
    else:
      print(f"{RED}Something bad happened Try again with valid value..")
      
  except Exception as e:
    print(f"{RED}Bad request or Bad Value try again later..{YELLOW}{e}")
