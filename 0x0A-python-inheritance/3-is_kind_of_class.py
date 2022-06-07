#!/usr/bin/python3

"""
isinstance: caters for inheritance
(an instance of a derived class is an
instance of a base class, too), while
checking for equality of type does not

"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True
    if the object is an instance
    or the specified class
    otherwise False.
    """
    return isinstance(obj, a_class)
