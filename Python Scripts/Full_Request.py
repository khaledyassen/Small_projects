import socket
import requests
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  host = input("Enter the domain ? ")  
except:
  print("Error happen try again ..")
s.connect((host,443))
print("connected Succefully")
url = 'https://'+host
method_list = ['GET','POST','HEAD','DELETE','TRACE','OPTIONS']
for method in method_list:
  rqst = requests.request(method, url)
  print(method,rqst.status_code,rqst.reason)
header_method = input("Enter method for geting the header ? ")
rgst = requests.request(header_method, url)
print(rgst.headers)