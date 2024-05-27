#!/usr/bin/python3
"""Import JSON."""
import json

"""A function that returns the JSON representation of an object (string)."""


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
