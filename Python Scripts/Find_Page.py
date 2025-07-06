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

# def help_Function():
#   parser = argparse.ArgumentParser(description='Give us the URL and page and we know if valid or not',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent('''Example: pyhon3 found_Page.py -u URL -p page '''))
#   parser.add_argument('-u', '--Url', default='http://127.0.0.1', help='Take the URL')
#   parser.add_argument('-p', '--Page',required=True, help='Page to check')
#   args = parser.parse_args()
#   print(args) 

def send_Request(url, page):
  response = requests.get(url+page)
  status = response.status_code
  if status==200:
    print("\n")
    print(f"{BOLD}{BLUE}Congratulations {RESET}page {GREEN}Found on the server.")
  else:
    print("\n")
    print(f"{BOLD}{RED}Unfortunatly {RESET}page{YELLOW} not found on the server.")
  sys.exit()

if __name__=='__main__':
  parser = argparse.ArgumentParser(description='Give us the URL and page and we know if valid or not',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent('''Example: pyhon3 found_Page.py -u URL -p page '''))
  parser.add_argument('-u', '--Url', default='http://127.0.0.1', help='Take the URL')
  parser.add_argument('-p', '--Page',required=True, help='Page to check')
  args = parser.parse_args()
  print(f"Here is your full inputs {args}")
  send_Request(args.Url, args.Page)
