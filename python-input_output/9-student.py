#!/usr/bin/python3
""" A class Student that defines a student by
    public instance attributes :
    first_name, last_name and age.
"""


class Student:
    """ Initializes the attributes. """
    def __init__(self, first_name, last_name, age):
        """ Initialization with first_name, last_name and age. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ A public method that retrieves a dictionary representation
        of a Student instance.
    """
    def to_json(self):
        """ Returns a dictionnary. """
        return self.__dict__
