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

    for i in range(n):
        temp = []
        temp.append(1)
        if i > 0:
            for j in range(1, i):
                temp.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
            temp.append(1)
        my_list.append(temp)
    return (my_list)
