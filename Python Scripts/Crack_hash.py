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

def hash_func(hash_object_value, password_hashed):
  with open('fuzz.txt', 'r') as f:
    for password_plain_text in f:
      print(f"{YELLOW}{BOLD}Hash the password {GREEN}{password_plain_text.strip()}")
      hash_object_value_reset = hashlib.new(hash_object_value.name)
      hash_object_value_reset.update(password_plain_text.strip().encode('UTF-8'))
      hash_value = hash_object_value_reset.hexdigest()
      if hash_value == password_hashed:
        return f"{BOLD}{BLUE}Congratulation, We cracked the password. The value is {YELLOW}{password_plain_text}"
        exit()
      else:
        print(f"{GREEN}{BOLD}{password_plain_text.strip()} {RED}incorrect\n")
        continue
    print(f"{BOLD}{RED}We are very sorry for you")


# Start Coding
if __name__=='__main__':
  password_hashed = input(f"{GREEN}Give me the password hashed that need to crack: {BLUE}")
  if len(password_hashed)==32:
    hash_object = hashlib.md5()
    print("Hash type is md5")
  elif len(password_hashed)==40:
    hash_object = hashlib.sha1()
    print("Hash type is sha1")
  elif len(password_hashed)==64:
    hash_object = hashlib.sha256()
    print("Hash type is sha256")
  elif len(password_hashed)==128:
    hash_object = hashlib.sha512()
    print("Hash type is sha512")
  else:
    print(f"{BOLD}{RED}Unknown hash alogrthim Try again with valid value{RESET}..")
    exit()
  print(hash_func(hash_object, password_hashed))
  