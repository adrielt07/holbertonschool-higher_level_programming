#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.checkattr(width, 1)
        self.__width = width
        Base.checkattr(height, 2)
        self.__height = height
        Base.checkattr(x, 3)
        self.__x = x
        Base.checkattr(y, 4)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting width"""
        Base.checkattr(value, 1)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height"""
        Base.checkattr(value, 2)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting x"""
        Base.checkattr(value, 3)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting y"""
        Base.checkattr(value, 4)
        self.__y = value

    def area(self):
        """returns the area"""
        return self.__height * self.__width

    def display(self):
        """image of rectangle"""
        for n in range(self.__y):
            print()
        for i in range(self.__height):
            for beg in range(self.__x):
                print(" ", end="")
            for k in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """prints string"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)
