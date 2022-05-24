#!/usr/bin/python3

""" defines a square class"""


class Square():
    """ Private instance attribute """
    __size = 0

    def __init__(self, size):
        """thanks to init we can receive the arguments, in this case '3' """
        self.__size = size
