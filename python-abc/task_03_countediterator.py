#!/usr/bin/env python3
""" A class CuntedIterator that extends the built-in iterator obtained from
    the iter function.
"""


class CountedIterator:
    """ Initilize an iterator object and a counter. """
    def __init__(self, some_iterable):
        """Initialize with an iterable and set up the iterator and counter."""
        self.iterator = iter(some_iterable)
        self.count = 0

    """ A method iter that returns an iterator object. """
    def __iter__(self):
        """ Return the iterator object itself. """
        return self

    """ The method next that increments a counter. """
    def __next__(self):
        """ Returns the next item and increment the counter. """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    """ The method get_count that retrieve and print the number of items
        that have been fetched.
    """
    def get_count(self):
        """ Returns the current count of iterated items. """
        return self.count
