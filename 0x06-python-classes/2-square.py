#!/usr/bin/python3

""" defines a square class"""


class Square():
    def __init__(self, size=0):
        """thanks to init we can receive the arguments, in this case '3' """
        self.__size = size
        if (type(self.__size) != int):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
