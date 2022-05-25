#!/usr/bin/python3
""" defines a square class"""




class Square():
    """thanks to init we can receive the arguments, in this case '3' """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if (type(self.__size) != int):
            raise NameError("size must be an integer")
        if (self.__size < 0):
            raise NameError("size must be >= 0")
        if (type(position[0]) != int or type(position[1]) != int):
            raise NameError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise NameError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return (self.__size)
    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @position.setter
    def position(self, value):
        if (type(value[0]) != int or type(value[1]) != int):
            raise NameError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise NameError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            return (print())
        for i in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end='')
            for y in range(self.__size):
                print('#', end='')
            print()
