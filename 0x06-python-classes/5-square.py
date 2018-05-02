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

    """
    Calculates the area of the square
    """
    def area(self):
        return self.__size * self.__size

    """
    setting up property
    """
    @property
    def size(self):
        return self.__size

    """
    setting up setter
    """
    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """
    prints stdout the square with character '#'
    """
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
