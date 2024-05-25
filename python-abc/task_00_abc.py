#!/usr/bin/env python3
""" Import ABC from the package abc and abstractmethod. """
from abc import ABC, abstractmethod

""" Defines an abstract class named Animal using the ABC package. """


class Animal(ABC):
    """ An abstract method that produces sound. """
    @abstractmethod
    def sound(self):
        """ An empty method. """
        pass


""" A subclass representing a dog, inheriting from Animal. """


class Dog(Animal):
    """ Implement the sound method for the sound that makes a dog. """
    def sound(self):
        """ Returns the string Bark. """
        return "Bark"


""" A subclass representing a cat, inheriting from Animal. """


class Cat(Animal):
    """ Implement the sound method for the sound that makes a cat. """
    def sound(self):
        """ Returns the string Meow. """
        return "Meow"
