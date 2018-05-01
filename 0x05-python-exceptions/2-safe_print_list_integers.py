#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int) is True:
                print("{:d}".format(my_list[i]), end="")
                num += 1
    except (TypeError, ValueError):
        pass
    print()
    return num
