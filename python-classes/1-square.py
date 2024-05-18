#!/usr/bin/python3

"""A class Square that defines a square by a private instance attribute size"""


class Square:
    """Define a Square"""

    def __init__(self, size):
        """Initialize a Square.

        Args:
            size : The size of the square.
        """
        self.__size = size
