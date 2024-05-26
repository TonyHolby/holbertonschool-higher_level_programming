#!/usr/bin/env python3
""" Import ABC from the package abc, abstractmethod and the package math. """
from abc import ABC, abstractmethod
import math

""" Defines an abstract class named Shape using the ABC package. """


class Shape(ABC):
    """ An abstract method to calculate the area of the shape. """
    @abstractmethod
    def area(self):
        """ An empty method. """
        pass

    """ An abstract method to calculate the perimeter of the shape. """
    @abstractmethod
    def perimeter(self):
        """ An empty method."""
        pass


""" A subclass representing a circle, inheriting from Shape. """


class Circle(Shape):
    """ Defines a class circle. """
    def __init__(self, radius):
        """ Initialize a circle. """
        self.radius = radius

    """ A method to calculate the area of the circle. """
    def area(self):
        """ Returns the area of the circle. """
        circle_area = math.pi * (self.radius ** 2)
        return circle_area

    """ A method to calculate the perimeter of the circle. """
    def perimeter(self):
        """ Returns the perimeter of the circle. """
        circle_perimeter = 2 * math.pi * self.radius
        return circle_perimeter


""" A subclass representing a rectangle, inheriting from Shape. """


class Rectangle(Shape):
    """ Defines a class rectangle. """
    def __init__(self, width, height):
        """ Initialize a rectangle. """
        self.width = width
        self.height = height

    """ A method to calculate the area of the rectangle. """
    def area(self):
        """ Returns the are of the rectangle. """
        rectangle_area = self.width * self.height
        return rectangle_area

    """ A method to calculate the perimeter of the rectangle. """
    def perimeter(self):
        """ Returns the perimeter of the rectangle. """
        rectangle_perimeter = 2 * (self.width + self.height)
        return rectangle_perimeter


""" A standalone function shape_info that accepts an object of type Shape. """
def shape_info(shape):
    """ Prints the area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
