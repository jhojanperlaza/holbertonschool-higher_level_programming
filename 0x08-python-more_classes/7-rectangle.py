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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property  # -> getter height
    def height(self):
        return self.__height

    @property  # -> getter width
    def width(self):
        return self.__width

    @height.setter  # -> setter height
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @width.setter  # -> setter width
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Method to calculate  the area of the rectangle"""
        return self.__height * self.width

    def perimeter(self):
        """Method to calculate  the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        string_result = ''
        cont = 0
        for columns in range(self.__height):
            for row in range(self.__width):
                string_result += str(self.print_symbol)
                cont += 1
            if cont != self.__width * self.__height:
                string_result += '\n'
        return string_result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
