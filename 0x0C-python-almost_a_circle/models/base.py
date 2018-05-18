#!/usr/bin/python3

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def checkattr(value, num):
        """
        1 = width
        2 = height
        3 = x
        4 = y
        """
        if num == 1:
            if isinstance(value, int) is False:
                raise TypeError("width must be an integer")
            if value < 1:
                raise ValueError("width must be > 0")
        elif num == 2:
            if isinstance(value, int) is False:
                raise TypeError("height must be an integer")
            if value < 1:
                raise ValueError("height must be > 0")
        elif num == 3:
            if isinstance(value, int) is False:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
        elif num == 4:
            if isinstance(value, int) is False:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
