#!/usr/bin/python3
""" A function that checks if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """ Returns True or False after checking.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance of a_class : True.
        Otherwise : False.
    """
    if isinstance(obj, a_class):
        return True
    return False
