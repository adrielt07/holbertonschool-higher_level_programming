#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0

    for elem in list(set(my_list)):
        result = result + elem
    return result
