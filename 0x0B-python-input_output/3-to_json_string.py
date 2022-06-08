#!/usr/bin/python3
"""

json.dumps() function 
converts a Python object 
into a Json string.

"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: is the object to be converted
    Returns:
        the Json string representation
    """
    return json.dumps(my_obj)
