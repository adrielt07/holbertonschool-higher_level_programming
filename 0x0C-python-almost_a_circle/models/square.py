#!/usr/bin/python3
"""Module has one class: Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize using rectangle class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print string"""
        return super().__str__(Square)

    @property
    def size(self):
        """returns size"""
        return self.width

    @size.setter
    def size(self, value):
        super().checkattr(value, 1)
        self.width = value

    def update(self, *args, **kwargs):
        """updates the attributes"""
        if len(args) != 0:
            a = list(args)
            super().update(a, kwargs)

        else:
            for key, val in kwargs.items():
                if hasattr(self, key) is True:
                        setattr(self, key, val)

        """
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]

        """
