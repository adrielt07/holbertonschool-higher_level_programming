#!/usr/bin/python3
import sys
import json



"""my_list = []
for arg in sys.argv[1:]:
my_list.append(arg)
"""

with open('add_item.json', 'r+') as f:
    my_list = json.load('add_item.json')
    for elem in sys.argv[1:]:
        my_list.append(elem)

    json.dump(my_list, f)
