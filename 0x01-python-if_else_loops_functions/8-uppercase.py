#!/usr/bin/python3
def uppercase(str):
    print("".join(["{:c}".format(ord(i)-32) if ord(i) in range(97, 123) else
                   "{:c}".format(ord(i)) for i in str]))
