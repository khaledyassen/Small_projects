#!/usr/bin/env python3
# Packages Required
import requests
from bs4 import BeautifulSoup
import argparse , textwrap
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

def Check_Title(Target_url):
  re = requests.get(Target_url)
  if re.status_code==200:
    response = re.text
    HTML_Soup = BeautifulSoup(response,'html.parser')
    soup = HTML_Soup.find('h1')
    if soup:
      print(f"Title is {BLUE}{soup.text}")
    else:
      print(f"Title is {RED}None{RESET}")

def is_valid_file(parser, arg):
    if not os.path.isfile(arg):
        parser.error(f"{BOLD}{RED}The file {GREEN}{arg}{RED} does not exist.")
    else:
        return arg


# Start main function
if __name__=='__main__':  
  parser = argparse.ArgumentParser(description=f'{BOLD}{GREEN}Check if the target contain title or not..{RESET}',formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent(f'''
  {BOLD}{YELLOW}Example: {RESET}{BOLD}python3 Check_Domain_Title.py (-tf targets.txt | -t https://target.com) {BLUE}# give it the target file or URL..'''))
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('-tf', '--TargetsFile', help=f'{BOLD}{BLUE}Target file to check{RESET}', type=lambda x: is_valid_file(parser, x))
  group.add_argument('-t', '--Target', help=f'{BOLD}{BLUE}Target URL to check{RESET}')
  args = parser.parse_args()

  if args.TargetsFile:
    with open(args.TargetsFile, 'r') as f:
      for i in f:
        print(i.strip())
        Check_Title(i.strip())

  if args.Target:
    Check_Title(args.Target)


  