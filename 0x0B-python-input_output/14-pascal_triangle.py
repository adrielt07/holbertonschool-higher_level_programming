#!/usr/bin/python3
"""Module pascal_triangle"""


def pascal_triangle(n):
    """
    Returns a list of list of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    my_list = []
    temp = []

    for i in range(1, n):
        temp = []
        for k in range(i):
            temp.append(k ** k)
        my_list.append(temp)

    print(my_list)

print(pascal_triangle(5))
