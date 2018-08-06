#!/usr/bin/python3
import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode(encoding="utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
