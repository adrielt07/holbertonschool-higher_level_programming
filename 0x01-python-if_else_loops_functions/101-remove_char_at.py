#!/usr/bin/python3
def remove_char_at(str, n):
    if (n == 0):
        print("{}".format(str[1:]))
    else:
        str = str[0:n] + str[n+1:]
        return str
