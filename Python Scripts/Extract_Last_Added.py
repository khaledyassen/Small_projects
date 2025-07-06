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


  Url = "https://catalog.data.gov/dataset?q=&sort=metadata_modified+desc&ext_location=&ext_bbox=&ext_prev_extent="
  response = requests.get(Url)
  if response.status_code==200:
    response2 = response.text
    soup = BeautifulSoup(response2,'html.parser')
    specific_tag = soup.find_all('h3', class_="dataset-heading")
    print(f"{BOLD}{GREEN}\nHere is the lastest datasets added to our website..{RESET} \n")
    for i,tag in enumerate(specific_tag):
      color = BLUE if i % 2 == 0 else YELLOW
      print_colored_line(tag.text.strip(), color)