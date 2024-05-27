#!/usr/bin/python3
""" A function that returns an object (Python data structure)
    represented by a JSON string.
"""


def class_to_json(obj):
    """Returns an object represented by a JSON ."""
    return obj.__dict__
