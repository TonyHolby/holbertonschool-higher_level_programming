#!/usr/bin/python3

""" A class Rectangle that defines a rectangle
    by a private instance attribute width
    and a private instance attribute height.
    A public instance method that returns
    the rectangle area.
    A public instance method that returns
    the rectangle perimeter.
"""


class Rectangle:
    """ Defines a rectangle. """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ Retrieves the private instance attibute height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the private instance attibute height. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Retrieves the private instance attibute width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the private instance attibute width. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Returns the area of the rectangle. """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """ Returns the perimeter of the rectangle. """
        if self.__height != 0 or self.__width != 0:
            perimeter = (self.__height * 2) + (self.__width * 2)
        else:
            perimeter == 0
        return perimeter

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of the new rectangle.
        """
        return cls(size, size)

    def __str__(self):
        """ Returns a string representation of the rectangle. """
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join(str(self.print_symbol) * self.__width for i in range(self.__height))

    def __repr__(self):
        """ Returns a string representation that can recreate the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Prints a message when an instance of Rectangle is deleted. """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def my_print(self):
        """ Prints the rectangle with the character #. """
        print(self)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger area, or rect_1 if they are equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
