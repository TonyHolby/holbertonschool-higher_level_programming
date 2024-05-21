#!/usr/bin/python3
"""
    A function that says my name
    
    Parameters:
        first_name (str): the first name.
        last_name (str): the last name.

    Raises:
        TypeError: If first_name and last_name are not strings.
"""


def say_my_name(first_name, last_name=""):
    """ Returns my name. """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is", f"{first_name} {last_name}")
    print("My name is", first_name)

