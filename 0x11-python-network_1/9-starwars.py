#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
"""

import requests
import sys

if __name__ == "__main__":

    url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    r = requests.get(url)
    json_dict = r.json()
    print("Number of results: {}".format(json_dict['count']))

    for value in json_dict['results']:
        print(value['name'])
