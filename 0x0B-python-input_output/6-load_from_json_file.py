#!/usr/bin/python3
"""

function that creates
an Object from a “JSON file”

"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename: is the txt file
    Returns:
        string of the JSON representation
    """
    with open(filename, "r", encoding="utf-8") as file:
        object_json = file.read()
        return json.loads(object_json)
