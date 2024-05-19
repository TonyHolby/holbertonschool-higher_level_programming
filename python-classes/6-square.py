#!/usr/bin/python3
""" A class Square that defines a square by:
    A private instance attribute size and the handling of TypeError
    and ValueError.
    A public instance method that returns the current square area.
    A public instance method that prints in stdout the square with the
    character #.
"""


class Square:
    """ Define a Square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a Square and a position.

        Args:
            size : The size of the square.
            position: The position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ To retrieve the private instance attibute size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ To set the private instance attibute size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ To retrieve the private instance attibute position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ To set the private instance attibute position.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ To return the area of the square.
        """
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ To print the square with the character #.
        """
        if self.__size == 0:
            print()
            return
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
