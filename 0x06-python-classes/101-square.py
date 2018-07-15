#!/usr/bin/python3
"""
Square is a Class:
defines a square by size
"""


class Square:
    """
    Create a private instance attribute size and position
    size must be an int and can't be negative
    position must be a tuple with two elements and value can't be negative
    """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if isinstance(position, tuple) is False or len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for elem in position:
            if isinstance(elem, int) is False or elem < 0:
                raise TypeError("position must be a tuple of "
                                "2 positive integers")
        self.__position = position

    """
    Calculates the area of the square
    """
    def area(self):
        return self.__size * self.__size

    """
    property for self to retrieve it
    """
    @property
    def size(self):
        return self.__size

    """
    setter for self to set it
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
    property for position to retrieve it
    """
    @property
    def position(self):
        return self.__position

    """
    setter for position to set it
    """
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for elem in value:
            if isinstance(elem, int) is False or elem < 0:
                raise TypeError("position must be a tuple of "
                                "2 positive integers")
        self.__position = value

    """
    prints stdout the square with character '#'
    """
    def my_print(self):
        if self.__size == 0:
            print ()

        for k in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for front_space in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print ()

    def __str__(self):
        s = ""

        for k in range(self.__position[1]):
            s += "\n"
        for i in range(self.__size):
            for front_space in range(self.__position[0]):
                s += " "
            for j in range(self.__size):
                s += "#"
            if i == self.__size - 1:
                break
            else:
                s += "\n"
        return s
