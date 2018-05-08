#!/usr/bin/python3
"""
Module that defines a rectangle
Class is: Rectangle
"""


class Rectangle:
    """Rectangle Class: takes two arguments - width and height
    width and height has to be an int and can't a negative value

    Example Usage:
    Rectangle(4, 2)

    Functions:
    Rectangle.width() - returns value of width
    Rectangle.height() - returns value of height
    """
    def __init__(self, width=0, height=0):
        """Initialize variables width and height
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Retrieving height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Retrieving width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
