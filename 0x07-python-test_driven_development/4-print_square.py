#!/usr/bin/python3
"""
    this module prints a square with the character #
"""


def print_square(size):
    """
    Args:
        size: is the size of the square
    Returns:
        prints a square with the character
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if (type(size) != int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (size == 0):
        return
    for x in range(size):
        for y in range(size):
            print('#', end='')
        print()
