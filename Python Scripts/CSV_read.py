from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
import requests
import csv
from io import StringIO


# Initialize colorama
init()

# Define color constants
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RED = Fore.RED
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

if __name__=='__main__':
  # URL of the CSV file
  csv_url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv'

  # Specify the target row index (0-based)
  target_row_index = int(input(f"{BOLD}{GREEN}Give me the number of row you need? {RED}"))

  # Make a request to the URL
  response = requests.get(csv_url)

  # Check if the request was successful (status code 200)
  if response.status_code == 200:
      # Create a CSV reader from the response content
      csv_data = StringIO(response.text)
      csv_reader = csv.reader(csv_data)

      # Keep track of the current row index
      current_row_index = 0
      
      # Iterate over each row in the CSV
      for row in csv_reader:
          if current_row_index == target_row_index:
              print(f"""
  {BOLD}{BLUE}Time is {YELLOW}{row[0]}
  {BOLD}{BLUE}latitude is {YELLOW}{row[1]}
  {BOLD}{BLUE}longitude is {YELLOW}{row[2]}
  {BOLD}{BLUE}depth is {YELLOW}{row[3]}
  {BOLD}{BLUE}mag is {YELLOW}{row[4]}
  {BOLD}{BLUE}magType is {YELLOW}{row[5]}
  {BOLD}{BLUE}nst is {YELLOW}{row[6]}
  {BOLD}{BLUE}gap is {YELLOW}{row[7]}
  {BOLD}{BLUE}dmin is {YELLOW}{row[8]}
  {BOLD}{BLUE}rms is {YELLOW}{row[9]}
  {BOLD}{BLUE}net is {YELLOW}{row[10]}
  {BOLD}{BLUE}id is {YELLOW}{row[11]}
  {BOLD}{BLUE}updated is {YELLOW}{row[12]}
  {BOLD}{BLUE}place is {YELLOW}{row[13]}
  {BOLD}{BLUE}type is {YELLOW}{row[14]}
  {BOLD}{BLUE}horizontalError is {YELLOW}{row[15]}
  {BOLD}{BLUE}depthError is {YELLOW}{row[16]}
  {BOLD}{BLUE}magError is {YELLOW}{row[17]}
  {BOLD}{BLUE}magNst is {YELLOW}{row[18]}
  {BOLD}{BLUE}status is {YELLOW}{row[19]}
  {BOLD}{BLUE}locationSource is {YELLOW}{row[20]}
  {BOLD}{BLUE}magSource is {YELLOW}{row[21]}
              """)
              # print(f"Row {target_row_index + 1}: {row}")
              break  # Stop searching after finding the target row
          current_row_index += 1
      else:
          print(f"No row found at index {target_row_index}.")
  else:
      print(f"Failed to fetch CSV file. Status code: {response.status_code}")
