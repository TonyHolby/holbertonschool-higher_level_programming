#!/usr/bin/python3
"""A function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """ Open a file and appends a string at the end of a text file (UTF8) and
        returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        characters_added = f.write(text)
    return characters_added
