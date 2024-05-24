#!/usr/bin/python3
""" A class MyList that inherits from list. """


class MyList(list):
    """ A public instance method that prints the sorted list. """

    def print_sorted(self):
        """ Prints the list in sorted ascending order. """
        sorted_list = sorted(self)
        print(sorted_list)
