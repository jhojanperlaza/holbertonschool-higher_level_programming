#!/usr/bin/python3
"""

json.load() method can be used to parse
a valid JSON string and convert it into
a Python Dictionary.

json.lod() takes a file object and
returns the json object

"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str: is the string to be converted
    Returns:
        an object (Python data structure)
        represented by a JSON string
    """
    return json.loads(my_str)
