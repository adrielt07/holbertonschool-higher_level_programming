#!/usr/bin/python3
"""Module has one class: Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize using rectangle class"""
        self.__size = size
        self.__x = x
        self.__y = y
        super().__init__(self.__size, self.__size, self.__x, self.__y, id)

    def __str__(self):
        """print string"""
        return super().__str__(Square)

#        return "[Square] {} {}/{} - {}".format(self.id, self.__x, self.__y, self.__size)

    @property
    def size(self):
        """returns size"""
        return super().width

    @size.setter
    def size(self, value):
        super().checkattr(value, 1)
        self.__size = value

    def update(self, *args, **kwargs):
        if len(args) > 2 and len(args) != 0:
            a = list(args)
            a.insert(1, self.__size)
            a = tuple(a)
            super().update(a, kwargs)

        else:
            super().update(args, kwargs)
