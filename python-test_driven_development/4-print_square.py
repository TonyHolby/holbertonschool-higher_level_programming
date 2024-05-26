#!/usr/bin/python3
"""
    Prints a square with the character #.

    Parameters:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is not positive.
"""


def print_square(size):
    """ Prints a square with the character #. """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for index in range(size):
        print("#" * size)
