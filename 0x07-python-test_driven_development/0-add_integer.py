#!/usr/bin/python3
"""
add_integer adds two integers
Return:
Sum of a and b
"""


def add_integer(a, b=98):
    """
    Adds two int or float types only. Else, raise a Type Error
    """
    if isinstance(a, (float, int)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (float, int)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
