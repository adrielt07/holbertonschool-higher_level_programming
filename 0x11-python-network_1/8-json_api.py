#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
"""

import requests
import sys

if __name__ == "__main__":
    try:
        value = {'q': sys.argv[1]}
    except IndexError:
        value = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', value)
    try:
        res = r.json()
        if len(res) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
    except:
        print("Not a valid JSON")
