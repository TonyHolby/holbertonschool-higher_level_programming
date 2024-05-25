#!/usr/bin/python3
""" A class BaseGeometry that defines a geometric figure
    by a public instance method that raises an Exception
    and a public instance method that validates a parameter as an integer.
"""

class BaseGeometry:
    """ Defines a class BaseGeometry. """

    def area(self):
        """ Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


""" A class Rectangle that inherits from BaseGeometry.
    Instantiation with width and height.
    
"""


class Rectangle(BaseGeometry):
    """ Defines a class Rectangle. """

    def __init__(self, width, height):
        """ Intialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """ Returns the area of the rectangle. """
        rectangle_area = self.__width * self.__height
        return rectangle_area

    def __str__(self):
        """ Returns the string representation of the rectangle. """
        rectangle_description = f"[Rectangle] {self.__width}/{self.__height}"
        return rectangle_description


""" A class Square that inherits from Rectangle. """


class Square(Rectangle):
    """Square class inheriting from Rectangle."""
    
    def __init__(self, size):
        """ Initialize Square.
        
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of the square. """
        square_area = self.__size ** 2
        return square_area
