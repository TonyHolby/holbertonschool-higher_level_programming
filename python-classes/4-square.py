#!/usr/bin/python3

""" A class Square that defines a square by:
    A private instance attribute size
    and the handling of TypeError and ValueError.
    A Public instance method that returns the current square area.
"""


class Square:
    """ Define a Square. """

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size : The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """ To retrieve the private instance attibute size. """
        return self.__size

    @size.setter
    def size(self, value):
        """ To set the private instance attibute size. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Define the area of the square. """
        area = self.__size * self.__size
        return area
