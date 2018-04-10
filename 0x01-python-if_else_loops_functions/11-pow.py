#!/usr/bin/python3
def pow(a, b):
    num = a
    b_cp = b
    if b < 0:
        b = b * -1

    for i in range(b - 1):
        num = num * a
    if b_cp < 0:
        num = 1 / num
    return num
