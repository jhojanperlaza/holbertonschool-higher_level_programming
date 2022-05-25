#!/usr/bin/python3
""" defines a square class"""


class Square():
    """thanks to init we can receive the arguments, in this case '3' """

    def __init__(self, size=0):
        self.__size = size
        if (type(self.__size) != int):
            raise NameError("size must be an integer")
        if (self.__size < 0):
            raise NameError("size must be >= 0")

    def area(self):
        self.area = self.__size * self.__size
        return (self.area)
