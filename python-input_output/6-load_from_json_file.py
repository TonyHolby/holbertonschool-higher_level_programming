#!/usr/bin/python3
"""Import JSON."""
import json

"""A function that creates an Object from a JSON file."""


def load_from_json_file(file_name):
    """Creates an Object from a JSON file."""
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)
