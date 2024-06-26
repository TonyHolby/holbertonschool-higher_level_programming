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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
