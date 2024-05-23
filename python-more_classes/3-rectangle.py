#!/usr/bin/python3

""" A class Rectangle that defines a rectangle
    by a private instance attribute width
    and a private instance attribute height.
    A public instance method that returns
    the rectangle area.
    A public instance method that returns
    the rectangle perimeter.
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

    def area(self):
        """ Returns the area of the rectangle. """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """ Returns the perimeter of the rectangle. """
        if self.__height != 0 or self.__width != 0:
            perimeter = (self.__height * 2) + (self.__width * 2)
        else:
            perimeter == 0
        return perimeter

    def __str__(self):
        """ Returns a string representation of the rectangle. """
        if self.__height == 0 or self.__width == 0:
            return
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def my_print(self):
        """ Prints the rectangle with the character #. """
        print(self)
