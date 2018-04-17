#!/usr/bin/python3
def print_list_integer(my_list=[]):
    print("\n".join("{:d}".format(x) for x in my_list))
