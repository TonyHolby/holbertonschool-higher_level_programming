#!/usr/bin/python3
""" A function that checks if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """ Returns True or False after checking.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True: if obj is an instance of a class that inherited.
        False: Otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
