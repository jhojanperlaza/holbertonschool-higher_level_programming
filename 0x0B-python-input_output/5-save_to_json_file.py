#!/usr/bin/python3
"""

fuction that writes an Object
to a text file, using a JSON
representation:

"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        filename: is the txt file
        my_onj: is the object to convert
        and write to a json file
    Returns:
        nothing
    """
    str_json = json.dumps(my_obj)

    with open(filename, "a", encoding="utf-8") as file:
        file.write(str_json)
