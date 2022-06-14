#!/usr/bin/python3
""" This module contains the class Rectangle """
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property  # -> getter
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        for y_rows in range(self.__y):
            print()
        for columns in range(self.__height):
            for x_column in range(self.__x):
                print(" ", end='')
            for row in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        cont = 0

    def __str__(self):
        string_str = "[Rectangle] "
        string_str += "({}) {}/{}".format(self.id, self.__x, self.__y)
        string_str += " - {}/{}".format(self.__width, self.__height)
        return string_str
