import random

def generate_password(file):
  with open(file, 'r') as f:
    word = f.read().splitlines()
  password = random.sample(word,4)
  password = '-'.join(password)
  return password

if __name__=='__main__':
  file = 'password_ran.txt'
  print(generate_password(file))
