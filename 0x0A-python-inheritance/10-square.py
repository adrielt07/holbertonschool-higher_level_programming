#!/usr/bin/python3
"""Import Rectangle from 9-rectnagle module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square - inherenting from Rectangle"""
    def __init__(self, size):
        """Overriding Parent Init"""
        self.integer_validator("size", size)
        super().__init__(size, size)
