#!/usr/bin/python3
"""Importing from 7-base_geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class - Inhereting from BaseGeometery"""
    def __init__(self, width, height):
        """Checking if width or height is int greater than 0"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
