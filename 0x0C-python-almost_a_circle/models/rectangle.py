#!/usr/bin/python3
"""
This module contains the class Rectangle
that inherits from Base class
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a Recatangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor that initialize instance attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property  # -> getter
    def width(self):
        """ method getter of width"""
        return self.__width

    @property
    def height(self):
        """ method getter of height"""
        return self.__height

    @property
    def x(self):
        """ method getter of x"""
        return self.__x

    @property
    def y(self):
        """ method getter of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """ method setter the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ method setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Seted value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ this method return the area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """ this method print the rectangle """
        for y_rows in range(self.__y):
            print()
        for columns in range(self.__height):
            for x_column in range(self.__x):
                print(" ", end='')
            for row in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """ Updates the currents instances """
        cont = 0
        for arg in args:
            if cont == 0:
                self.id = arg
            if cont == 1:
                self.__width = arg
            if cont == 2:
                self.__height = arg
            if cont == 3:
                self.__x = arg
            if cont == 4:
                self.__y = arg
            cont += 1

    def __str__(self):
        """ Returns a string representation"""
        string_str = "[Rectangle] "
        string_str += "({}) {}/{}".format(self.id, self.__x, self.__y)
        string_str += " - {}/{}".format(self.__width, self.__height)
        return string_str
