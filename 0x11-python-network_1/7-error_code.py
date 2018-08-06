#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        if r.raise_for_status() == None:
            print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(r.status_code))
