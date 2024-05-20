#!/usr/bin/python3
""" A function that adds two integers. """


def add_integer(a, b=98):
    """ Returns a + b """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(a, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
