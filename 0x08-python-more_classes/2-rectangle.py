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
    Rectangle.area() - returns the area of rectangle
    Rectangle.perimeter() - returns the perimeter of rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializing variables width and height
        """
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height

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

    def area(self):
        """Calculates the area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of a rectangle
        """
        return (self.__height + self.__width) * 2
