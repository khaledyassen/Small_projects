#!/usr/bin/env python3
# Packages Required
import requests
from bs4 import BeautifulSoup
import hashlib

# Style for the output
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

# Start Coding
if __name__=='__main__':
  hash_object = hashlib.md5()
  print(hash_object)
  password = input(f"{BOLD}{GREEN}Enter the password you need to hash it: {BLUE}")
  hash_object.update(password.encode('UTF-8'))
  hashed_password = hash_object.hexdigest()
  print(f"{GREEN}The hashed password is: {YELLOW}{hashed_password}")
