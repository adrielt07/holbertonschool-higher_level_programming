#!/usr/bin/python3
"""
Module that defines a rectangle
Class is: Rectangle
"""


class Rectangle:
    """
    Rectangle Class: takes two arguments - width and height
    width and height has to be an int and can't a negative value

    Example Usage:
    Rectangle(4, 2)

    Functions:
    Rectangle.width() - returns value of width
    Rectangle.height() - returns value of height
    Rectangle.area() - returns the area of rectangle
    Rectangle.perimeter() - returns the perimeter of rectangle
    Rectangle.__str__() - return an image of rectangle made of '#' symbols
    Rectangle.__repr__() - returns a string Rectangle(<size>, <height>)
    Rectangle.__del__() - deletes rectangle
    Rectangle.bigger_or_equal() - compare two rectangle and returns bigger area
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing variables width and height
        """
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if isinstance(height, int) is False:
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Print rectanlge with character '#'
        """
        if self.__width is 0 or self.__height is 0:
            print()
        return "\n".join("".join("{}".format(self.print_symbol) for w in
                                 range(self.__width))
                         for h in range(self.__height))

    def __repr__(self):
        """Prints width and height of rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes a rectangle
        """
        Rectangle.number_of_instances -= 1
        return print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns rectangle with bigger area
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1.area()
        else:
            return rect_2.area()
