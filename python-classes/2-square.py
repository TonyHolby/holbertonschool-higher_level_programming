#!/usr/bin/python3

""" A class Square that defines a square by
    a private instance attribute size
    and the handling of TypeError and ValueError
"""


class Square:
    """ Define a Square
    """

    def __init__(self, size=0):
        """ Initialize a Square.

        Args:
            size : The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
