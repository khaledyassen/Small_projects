import socket
import sys
from datetime import datetime

# For connect to host and you can using nc as aserver for see the response 
# HOST = '127.0.0.1'
# PORT = 7777
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect((HOST,PORT))


if (len(sys.argv) == 2):
  target = socket.gethostbyname(sys.argv[1])
else:
  print("Invali input"+"\n")
  print("Syntax : python3 1.py <ip>")
print("-" * 50)
print(f"Scanning Target {sys.argv[1]}")
print(f"Result of scanning is {target}")
print(f"Time : {datetime.now()}")
print("-" * 50)

try:

  for port in range(50,85):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
      print(f"{port} Port is open")
    s.close()
except KeyboardInterrupt:
  print("\n Exiting program ")
  sys.exit()
except socket.gaierror:
  print("Host name could not be resolved")
  sys.exit()
except socket.error:
  print("Couldn't connect to server")
  sys.exit()