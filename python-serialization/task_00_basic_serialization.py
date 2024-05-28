#!/usr/bin/env python3
import json


""" Defines a function that serializes a Python dictionary to a JSON file. """


def serialize_and_save_to_file(data, filename):
    """ Writes the dictionary to the JSON file. """
    with open(filename, 'w') as file:
        json.dump(data, file)


""" Defines a function that deserializes the JSON file to recreate the Python
    Dictionary.
"""


def load_and_deserialize(filename):
    """ Returns a Python Dictionary with the deserialized JSON data from the
        file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
