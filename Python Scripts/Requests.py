import requests
from requests.auth import HTTPBasicAuth
import sys

proxy_settings = {
  'http':'http://127.0.0.1:8080',
  'https':'https://127.0.0.1:8080'
}

URL = sys.argv[1]
auth = HTTPBasicAuth('username','password')
headers = {"User-Agent":"Firefox Khaled yassen","X-Forwarded-For":"127.0.0.1"}
parms = {'username':'khaled','password':'password'}

response = requests.post(URL,proxies=proxy_settings,headers=headers,params=parms,auth = HTTPBasicAuth('username','password'))

print(response.text)
