#!/usr/bin/python3
"""
This module contains the class square
that inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor that initialize instance attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ return size of the square """
        return self.width
    
    @size.setter
    def size(self, value):
        """ set size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a string representation"""
        string_str = "[Square] "
        string_str += "({}) {}/{}".format(self.id, self.x, self.y)
        string_str += " - {}".format(self.width)
        return string_str
