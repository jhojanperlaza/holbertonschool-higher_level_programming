#!/usr/bin/python3

"""
isinstance: caters for inheritance
(an instance of a derived class is an
instance of a base class, too), while
checking for equality of type does not

"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object
    is exactly an instance of the specified class
    otherwise False.
    """
    return type(obj) is a_class
