#!/usr/bin/python3
"""

    this module prints My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name and last_name
    Returns:
        My name is <first name> <last name>
    Raises:
        TypeError: first_name/last_name must be a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is" + " " + first_name + " " + last_name)
