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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
