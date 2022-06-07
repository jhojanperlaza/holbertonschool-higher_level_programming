#!/usr/bin/python3

"""
Only sub class

"""


def inherits_from(obj, a_class):
    """
    function that returns True if
    the object is an instance
    of a class that inherited
    from the specified class
    """
    if type(obj) is  a_class:
        return False
    return isinstance(obj, a_class)

