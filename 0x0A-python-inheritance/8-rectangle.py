#!/usr/bin/python3
"""
import class BaseGeometry

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

""" 
Rectangle class inherited from Rectangle
"""

class Rectangle(BaseGeometry):
    """ 
    Rectangle class 
    """

    def __init__(self, width, height):
        """ 
        Constructor Rectangle  init
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
