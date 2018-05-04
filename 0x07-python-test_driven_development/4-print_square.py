#!/usr/bin/python3
"""
4-print_square - prints square with # sign
def(s)
1. def print_square(size)
"""


def print_square(size):
    """
    print_square - prints a square with # sign size x size
    args:
    size - takes an int or float
    Requirements:
    1) Must be a positive value
    2) Must be a number
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for i in range(size):
            print("#", end="")
        print()
