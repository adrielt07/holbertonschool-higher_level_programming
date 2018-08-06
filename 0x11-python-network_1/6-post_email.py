#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    value = {'email': argv[2]}
    r = requests.post(sys.argv[1], value)
    r.text
