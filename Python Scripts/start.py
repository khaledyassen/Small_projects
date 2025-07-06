# ===========================================================>sockt basics<========================================================================

# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1',7777))
# s.send("Hello user")
# s.recv()
# s.recvmsg(bufsize)
# s.close()

# ===========================================================>port scanning<========================================================================

# import socket
# import sys
# import datetime

# def scanner(host):
#   for i in range(80,444):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     c = s.connect_ex((host,i))
#     socket.setdefaulttimeout(1)
#     if c == 0:
#       print(f"{i} port is open")
#       s.close()

# # s.connect((host,81))
# try :
#   start = datetime.datetime.now()
#   host = socket.gethostbyname(input("Enter The host to scanning? "))
#   scanner(host)
# except socket.gaierror:
#   print("Enter valid host y broo")
#   host = socket.gethostbyname(input("Enter The host to scanning? "))
#   scanner(host)
# finally:
#   print("Task is done")
# end = datetime.datetime.now()
# print(f"Startded at {start} \nEnded at {end}")

# ===========================================================>HTTP request<========================================================================

# import requests
# Method_list = ['GET','POST','HEAD','DELETE','UPDATE','TRACE','OPTIONS']
# URL = input("Enter Target URL ? ")
# for method in Method_list:
#   rqst = requests.request(method, URL)
#   print(method,rqst.status_code,rqst.reason)
#   if method == 'TRACE' and rqst.text == 'TRACE / HTTP/1.1':
#     print('XST cross site tracing')

# ===========================================================> Http Headers <========================================================================

# import requests
# header_list = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code','Connection', 'Content-Length']
# url = input("Enter taregt url ? ")
# rqst = requests.post(url)
# print(rqst.headers)

# ===========================================================> mechanize <========================================================================


import mechanize

url = input("Enter the full url")
attack_no = 1