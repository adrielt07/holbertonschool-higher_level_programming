#!/usr/bin/python3
import sys
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
   header = response.info()
header = dict(header)
print(header['X-Request-Id'])
