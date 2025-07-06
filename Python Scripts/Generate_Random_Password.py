import random
import string

def randomm_(length):
  # Define the chacters sets
  lower_case_letters = string.ascii_lowercase
  capital_case_letters = string.ascii_uppercase
  digits = string.digits
  special_char = string.punctuation
  all_characters = lower_case_letters + capital_case_letters + digits + special_char
  print(all_characters)
  password = ''.join(random.choice(all_characters) for i in range(length))
  print(password)
  

def random_Password(Length__):
  print(Length__)
  lower_case_letters_ = string.ascii_lowercase
  upper_case_letters_ = string.ascii_letters
  numb = string.digits
  all_chars = lower_case_letters_ + upper_case_letters_ + numb
  return all_chars

if __name__=='__main__':
  length  = input("Enter the length of the generated value? ")
  print(random_Password(5))
  if length:
    randomm_(int(length))
  else:
    length=8
    randomm_(int(length))