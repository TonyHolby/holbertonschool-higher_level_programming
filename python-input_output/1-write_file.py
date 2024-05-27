#!/usr/bin/python3
"""A function that writes a string to a text file."""


def write_file(filename="", text=""):
    """ Open a file and writes a string to a text file (UTF8) and returns the
        number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        characters_written = f.write(text)
    return characters_written
