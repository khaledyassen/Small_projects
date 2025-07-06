#!/usr/bin/python3
from socket import *
import sys

if len(sys.argv) != 3:
  print("Use: ./SMTP_connect.py <IP> <User>")
  exit(0)

IP = sys.argv()
User = sys.argv(2)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect = s.connect((IP,25))
banner = s.recv(1024)
print(banner)
message = s.send('VRFY '+ User +'\r\n')
result = s.recv(1024)
print(result)
s.close()

print(banner)




