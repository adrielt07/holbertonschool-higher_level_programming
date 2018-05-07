#!/usr/bin/python3
"""
Module with class Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """ Initializing variables width and height
        """
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ Retrieving width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting width
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieving height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting height
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """ Calculates the perimeter of a rectangle
        """
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Print rectanlge with character '#'
        """
        if self.__width is 0 or self.__height is 0:
            print()
        return "\n".join("".join("#" for w in range(self.__width))
                         for h in range(self.__height))

