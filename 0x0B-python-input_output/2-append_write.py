#!/usr/bin/python3
"""

fuction that open file
and write in the end

"""


def append_write(filename="", text=""):
    """
    Args:
        filename: is the txt file
        text: is the text to write
    Returns:
        number of characters written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
