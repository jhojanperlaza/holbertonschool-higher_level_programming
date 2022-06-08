#!/usr/bin/python3
"""

fuction that write in a file

"""


def write_file(filename="", text=""):
    """
    Args:
        filename: is the txt file
        text: is the text to write
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
