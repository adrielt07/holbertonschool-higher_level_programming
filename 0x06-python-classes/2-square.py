#!/usr/bin/python3
"""
Square is a Class:
defines a square by size
"""


class Square:
    """
    Create a private instance attribute size
    size must be an int
    size must can't be negative
    """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
