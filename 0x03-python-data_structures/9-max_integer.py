#!/usr/bin/python3
def max_integer(my_list=[]):

    a = len(my_list)
    if a == 0:
        return None
    my_list.sort()
    return my_list[a-1]
