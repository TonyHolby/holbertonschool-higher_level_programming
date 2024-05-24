#!/usr/bin/python3
""" Defines a class BaseGeometry. """


class BaseGeometry:
        """ A public instance method that raises an Exception. """

    def area(self):
        """ Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
