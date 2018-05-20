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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.__size)
        return super().__str__(Square)

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        super().checkattr(value, 1)
        self.__size = value

    def update(self, *args, **kwargs):
        """updates the attributes"""
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.__size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.__size = args[1]
                self.__x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.__size = args[1]
                self.__x = args[2]
                self.__y = args[3]

        else:
            for key, val in kwargs.items():
                if hasattr(self, key) is True:
                        setattr(self, key, val)
