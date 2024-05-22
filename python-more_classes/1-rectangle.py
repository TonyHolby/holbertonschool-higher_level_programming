#!/usr/bin/python3

""" A class Rectangle that defines a rectangle
    by a private instance attribute width
    and a private instance attribute height
"""


class Rectangle:
    """ Defines a rectangle. """

    def __init__(self, width=0, height=0):
        """ Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ Retrieves the private instance attibute height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the private instance attibute height. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Retrieves the private instance attibute width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the private instance attibute width. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
