#!/usr/bin/python3
import sys
import urllib.request
import urllib.parse

url = sys.argv[1]
value = {'email': sys.argv[2]}

data = urllib.parse.urlencode(value)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   print(response.read().decode(encoding='utf-8'))
