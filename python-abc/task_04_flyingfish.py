#!/usr/bin/env python3
""" A parent class named Fish. """


class Fish:
    """ A swim method. """
    def swim(self):
        """ Prints : The fish is swimming """
        print("The fish is swimming")

    """ A habitat method. """
    def habitat(self):
        """ Prints : The fish lives in water """
        print("The fish lives in water")


""" A parent class named Bird. """


class Bird:
    """ A fly method. """
    def fly(self):
        """ Prints : The bird is flying """
        print("The bird is flying")

    """ A habitat method. """
    def habitat(self):
        """ Prints : The bird lives in the sky """
        print("The bird lives in the sky")


""" A FlyingFish class that inherits from both Fish and Bird. """


class FlyingFish(Fish, Bird):
    """ A fly method. """
    def fly(self):
        """ Prints : The flying fish is soaring! """
        print("The flying fish is soaring!")

    """ A swim method. """
    def swim(self):
        """ Prints : The flying fish is swimming! """
        print("The flying fish is swimming!")

    """ A habitat method. """
    def habitat(self):
        """ Prints : The flying fish lives both in water and the sky! """
        print("The flying fish lives both in water and the sky!")
