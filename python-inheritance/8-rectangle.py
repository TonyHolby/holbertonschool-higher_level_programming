#!/usr/bin/python3
""" A class BaseGeometry that defines a geometric figure
    by a public instance method that raises an Exception
    and a public instance method that validates a parameter as an integer.
"""

class BaseGeometry:
    """ Defines a class BaseGeometry. """

    def area(self):
        """ Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


""" A class Rectangle that inherits from BaseGeometry.
    Instantiation with width and height.
"""


class Rectangle(BaseGeometry):
    """ Defines a class Rectangle. """

    def __init__(self, width, height):
        """ Intialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
