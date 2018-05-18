#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """setting width"""
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """setting height"""
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """setting x"""
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """setting y"""
        self.__y = value
