#!/usr/bin/python3
def weight_average(my_list=[]):
    mult = 0
    ave = 0
    if not my_list:
        return 0

    for w, a in my_list:
        mult += w * a
        ave += a

    result = mult / ave
    return result
