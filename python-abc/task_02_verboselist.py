#!/usr/bin/env python3
""" A class VerboseList that extends the Python list class. """


class VerboseList(list):
    """ A method append that adds an item to the list. """
    def append(self, item):
        """ Appends an item to the list and prints a notification. """
        super().append(item)
        print(f"Added {item} to the list.")

    """ A method extend that extends the list. """
    def extend(self, iterable):
        """ Extends the list with elements from the iterable and prints
            a notification.
        """
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    """ A method remove that removes an item to the list. """
    def remove(self, item):
        """ Removes the first occurrence of an item from the list and prints
            a notification.
        """
        print(f"Removed {item} from the list.")
        super().remove(item)

    """ A method pop that removes and returns an item to the list. """
    def pop(self, index=-1):
        """ Removes and returns an item and prints a notification. """
        item = super().pop(index)
        print(f"Popped {item} from the list.")
        return item
