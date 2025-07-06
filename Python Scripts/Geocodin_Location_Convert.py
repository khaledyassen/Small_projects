import json
import requests

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

  try:
    addr = input(f"{BOLD}{BLUE}Give me the addresses to convert it[Geocodin]?{YELLOW} ")
    url = f"https://api.opencagedata.com/geocode/v1/json?q={addr}&key=28cf05a4ea424038b52ff7b5681a4a5a"
    res = requests.get(url)
    json_Data = res.text
    data = json.loads(json_Data)
    Result = data['results'][0]['geometry']
    print(f"{BOLD}{GREEN}The Lat value is {RED}{Result['lat']}{RESET}")
    print(f"{BOLD}{GREEN}The lng value is {RED}{Result['lng']}{RESET}")
  except requests.exceptions.ConnectionError as e:
    print(f"Error while making the request: {BOLD}{BLUE}{RED}Need a valid address.")
    exit(1)