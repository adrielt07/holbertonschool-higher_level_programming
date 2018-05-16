#!/usr/bin/python3
import sys
import json
import os


my_list = []

if os.path.exists("add_item.json") == True:
    with open("add_item.json", "r") as f:
        words = f.readline()
        my_list = json.loads(words)

for elem in sys.argv[1:]:
    my_list.append(elem)

with open("add_item.json", "w") as f:
    json.dump(my_list, f)
