#!/usr/bin/python3

"""
Square is a Class:
defines a square by size
"""

class Square:
    """
    Create a private instance attribute size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        self._size = size
