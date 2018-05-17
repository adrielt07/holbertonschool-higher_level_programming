#!/usr/bin/python3
"""Module pascal_triangle"""


def pascal_triangle(n):
    """
    Returns a list of list of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    my_list = []

    for i in range(n):
        my_list.append([])
        my_list[i].append(1)
        for j in range(1, i):
            my_list[i].append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        if(n != 0):
            my_list[i].append(1)
    return (my_list)
