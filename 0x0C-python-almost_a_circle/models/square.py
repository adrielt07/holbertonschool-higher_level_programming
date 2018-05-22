#!/usr/bin/python3
"""
Module has one class: Square
Inhereted from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class that defines a square

    Usage:
    Square(size, x, y, id)
    size are required

    s1 = size(4)
    s2 = size(5, 3, 2, 22)

    size - sides of square
    x - axis number front spaces when displaying square
    y - axis number of above newline when displaying square
    id - id assigned for each instance
    """
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
            if len(args) > 2:
                a = list(args)
                a.insert(1, self.width)
                args = tuple(a)
            super().update(*args)
        else:
            super().update(**kwargs)

    def to_dictionary(self):
        """
        prints the following in dictionary:
        id, size, x, y
        """
        new_dict = {}
        keys = ['id', 'size', 'x', 'y']

        for elem in keys:
            new_dict[elem] = getattr(self, elem)
        return new_dict
        super().to_dictionary
