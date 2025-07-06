#!/usr/bin/env python3
# Packages Required
import re

# Style for the output
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"


def Validate_password(password):
  if len(password) < 8:
    return False
  if not re.search(r'[A-Z]', password):
    return False
  if not re.search(r'[a-z]', password):
    return False
  if not re.search(r'\d', password):
    return False
  if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    return False
  return True

if __name__=='__main__':
  # password = input(f"{BOLD}{GREEN}Enter the password to validate it: {YELLOW}")
  with open('Passwords_list.txt','r') as f:
    for i in f:
      if Validate_password(i):
        print(f'{BLUE}Good Work that is a Valid password')
      else:
        print(f"{RED}Not a Valid Password")







# Oldest and a bad way

  # if len(password) >= 8:
  #   special_chrs = False
  #   upper_chrs = False
  #   lower_chrs = False
  #   _Num = False
  #   for i in password:
  #     if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '&':
  #       special_chrs = True
  #     if i.isupper():
  #       upper_chrs = True
  #     if i.islower():
  #       lower_chrs = True
  #     if i.isnumeric():
  #       _Num = True
  #   if special_chrs is True and upper_chrs  is True and lower_chrs  is True and _Num  is True:
  #     print(f'{BLUE}Good Work that is a Valid password')
  #   else:
  #     print(f"{RED}Not a Valid Password")      
  # else:
  #   print(f"{RED}Not a Valid Password")
  