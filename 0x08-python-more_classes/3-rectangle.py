#!/usr/bin/python3
"""
Rectangle module.

This module contains a class that defines a rectangle.
"""


class Rectangle():
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Sets attributes for Rectangle object.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Sets the print behavior of the Rectangle object."""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.__width + '\n'
        return rectangle[:-1]

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Returns the current rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the current rectangle perimeter."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2
