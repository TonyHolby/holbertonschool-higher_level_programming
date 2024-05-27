#!/usr/bin/python3
""" A function that reads a text file."""


def read_file(filename=""):
    """Open a file, read a text (UTF8) and print it to stdout."""
    with open(filename, 'r', encoding="utf-8") as f:
        read_file = f.read()
        print(read_file, end='')
