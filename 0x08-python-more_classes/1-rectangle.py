#!/usr/bin/python3
"""
Module with Class Rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """ Initialize variables width and height
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
