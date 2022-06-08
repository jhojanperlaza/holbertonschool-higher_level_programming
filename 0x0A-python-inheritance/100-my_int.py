#!/usr/bin/python3
"""
class BaseGeometry with one method

"""


class MyInt(int):
    """
    MyInt class
    """
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return "{}".format(self.num)
