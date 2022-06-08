#!/usr/bin/python3
"""

fuction that read a file
and print it to stdout

"""


def read_file(filename=""):
    """
    Args:
        filename: is the txt file
    Returns:
        nothing
    """
    with open(filename, "r", encoding="utf-8") as file:
        file_r = file.read()
        print(file_r, end="")
