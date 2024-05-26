#!/usr/bin/env python3
""" A parent class named SwimMixin. """


class SwimMixin:
    """ A swim method. """
    def swim(self):
        """ Prints : The creature swims! """
        print("The creature swims!")


""" A parent class named FlyMixin. """


class FlyMixin:
    """ A fly method. """
    def fly(self):
        """ Prints : The creature flies! """
        print("The creature flies!")


""" A Dragon class that inherits from both SwimMixin and FlyMixin. """


class Dragon(SwimMixin, FlyMixin):
    """ A fly method. """
    def fly(self):
        """ Prints : The creature flies! """
        print("The creature flies!")

    """ A swim method. """
    def swim(self):
        """ Prints : The creature swims! """
        print("The creature swims!")

    """ A roar method. """
    def roar(self):
        """ Prints : The dragon roars! """
        print("The dragon roars!")
