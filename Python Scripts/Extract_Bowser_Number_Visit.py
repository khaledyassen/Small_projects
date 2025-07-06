import requests
import json


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

  
  URL = "https://analytics.usa.gov/data/live/browsers.json"
  requ = requests.get(URL)
  if requ.status_code == 200:
    res = requ.text
    data = json.loads(res)
    Goal = data['totals']['browser']
    # print(f"{BLUE}{BOLD}90 days of visits broken down by browser for all sites:\n{GREEN}{Goal}{RESET}")
    print(f"{ITALIC}{BOLD}{YELLOW}90 days of visits broken down by browser for all sites:")
    for key, value in Goal.items():
      print(f"{BOLD}{BLUE}The Browser is {GREEN}{key}{BLUE} and visited {GREEN}{value} {BLUE}Times.{RESET}")
  else:
    print(f"{BOLD}{RED}Error in the request backagain when you can work..{GREEN}Failure man{RESET}")
