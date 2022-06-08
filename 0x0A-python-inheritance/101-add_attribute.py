#!/usr/bin/python3
"""
class BaseGeometry with one method

"""

def add_attribute(MyClass, atribute, value):
    """ Method that returns != check """
    if (hasattr(MyClass, "__dict__")) == False:
        raise TypeError("can't add new attribute")
    return setattr(MyClass, atribute, value)
