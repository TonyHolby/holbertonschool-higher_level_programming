#!/usr/bin/python3
""" A module that defines geometric figures and their properties. """


class BaseGeometry:
    """ Defines a base class for geometric operations. """

    def area(self):
        """ Raises an Exception indicating that area() is not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Defines a class Rectangle that inherits from BaseGeometry. """

    def __init__(self, width, height):
        """ Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the rectangle. """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ Defines a class Square that inherits from Rectangle. """

    def __init__(self, size):
        """ Initialize a square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of the square. """
        return self.__size ** 2

    def __str__(self):
        """ Returns the string representation of the square. """
        return f"[Square] {self.__size}/{self.__size}"
