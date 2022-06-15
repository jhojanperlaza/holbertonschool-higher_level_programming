#!/usr/bin/python3
"""
This module contains the class square
that inherits from Rectangle class
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor that initialize instance attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation"""
        string_str = "[Square] "
        string_str += "({}) {}/{}".format(self.id, self.x, self.y)
        string_str += " - {}".format(self.width)
        return string_str
