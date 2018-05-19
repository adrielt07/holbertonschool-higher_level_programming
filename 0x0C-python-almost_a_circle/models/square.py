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
        return super().__str__()
