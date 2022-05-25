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

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            return (print())
        for x in range(self.__size):
            for y in range(self.__size):
                print('#', end='')
            print()
