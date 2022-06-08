#!/usr/bin/python3
"""
class BaseGeometry with one method

"""


class BaseGeometry:
    """  BaseGeometry class """
    def area(self):
        """Method to calculate  the area of the rectangle"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """  method integer_validator """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
