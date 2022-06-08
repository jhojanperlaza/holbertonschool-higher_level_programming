#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
import class BaseGeometry

"""


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Constructor Rectangle  init"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
