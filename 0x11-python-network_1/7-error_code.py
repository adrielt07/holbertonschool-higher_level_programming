#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.raise_for_status() == None:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
