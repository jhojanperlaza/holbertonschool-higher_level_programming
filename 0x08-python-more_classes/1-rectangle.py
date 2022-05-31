#!/usr/bin/python3

"""

built a class Rectangle empty

"""


class Rectangle:
    """
    Args:
        width: the width of the rectangle
        height: the height of the rectangle
    Returns:
        nothing
    Raises:
        TypeError: width must be an integer
        ValueError: "width must be >= 0"
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property  # -> getter height
    def height(self):
        return self.__height

    @property  # -> getter width
    def width(self):
        return self.__width

    @height.setter  # -> setter height
    def height(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @width.setter  # -> setter width
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
