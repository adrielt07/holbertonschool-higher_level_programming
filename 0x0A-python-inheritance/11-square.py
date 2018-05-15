#!/usr/bin/python3
"""Import Rectangle from 9-rectnagle module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square - inherenting from Rectangle"""
    def __init__(self, size):
        """Overriding Parent Init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """print string"""
        return super().__str__()
