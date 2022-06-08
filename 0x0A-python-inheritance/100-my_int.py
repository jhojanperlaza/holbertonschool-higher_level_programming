#!/usr/bin/python3
"""
class BaseGeometry with one method

"""


class MyInt(int):
    """
    MyInt class
    """
    def __eq__(self, num_input):
        """ Method that returns != check """
        return int.__ne__(self, num_input)

    def __ne__(self, num_input):
        """ Method that returns == check """
        return int.__eq__(self, num_input)