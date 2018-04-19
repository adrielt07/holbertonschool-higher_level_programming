#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for elem in a_dictionary:
        if elem == key:
            a_dictionary[elem] = value
            return a_dictionary

    a_dictionary[key] = value
    return a_dictionary
