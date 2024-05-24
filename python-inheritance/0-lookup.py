#!/usr/bin/python3
""" A function that returns the list of available
    attributes and methods of an object.
"""


def lookup(obj):
    """ Returns a list object. """
    list = dir(obj)
    return list
