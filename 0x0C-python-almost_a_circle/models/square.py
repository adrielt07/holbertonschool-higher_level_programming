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

    def to_dictionary(self):
        """
        prints the following in dictionary:
        id, size, x, y
        """
        new_dict = {}
        keys = ['id', 'size', 'x', 'y']

        for elem in keys:
            new_dict[elem] =  getattr(self, elem)
        return new_dict
        super().to_dictionary
