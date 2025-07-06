#!/usr/bin/env python3
import requests
import argparse , textwrap
import requests
import sys

RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

def help_Function():
  parser = argparse.ArgumentParser(description='Give us the URL and page then we\'ll download the file',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent('''Example: pyhon3 found_Page.py -u URL -p page '''))
  parser.add_argument('-u', '--Url', help='Take the URL')
  parser.add_argument('-p', '--Page', help='Page to check')
  args = parser.parse_args()
  print(args) 

def send_Request(url, page):
  response = requests.get(url+page)
  status = response.status_code
  if status==200:
    print("\n")
    print(f"{BOLD}{BLUE}Congratulations {RESET}page {GREEN}Found on the server.")
    print("\n")
    print(f"{GREEN}{BOLD}Start Downloading the file...{BLUE}")
    print(response.content.decode('UTF-8'))
  # print(response.textwrap)
  else:
    print("\n")
    print(f"{BOLD}{RED}Unfortunatly {RESET}page {YELLOW} not found on the server.")
  sys.exit()

if __name__=='__main__':
  help_Function()
  send_Request(sys.argv[2], sys.argv[4])