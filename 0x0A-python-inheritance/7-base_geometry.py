#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """Base Geometry Class"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.__value = value
        self.__name = name
