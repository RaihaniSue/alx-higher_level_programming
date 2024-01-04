#!/usr/bin/python3
"""
Rectangle module.

Contains a class defining a captivating rectangle.
"""


class Rectangle():
    """Defines a geometric wonder."""

    def __init__(self, width=0, height=0):
        """Initiates the magic of the Rectangle.

        Args:
            width (int): width of the enchanting shape.
            height (int): height of the mystical form.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Creates an ethereal representation."""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.__width + '\n'
        return rectangle[:-1]

    def __repr__(self):
        """Defines the essence of the Rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """Unveils the width of the mystical form."""
        return self.__width

    @width.setter
    def width(self, value):
        """Reshapes the width of the magical entity."""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Discloses the height of the mysterious form."""
        return self.__height

    @height.setter
    def height(self, value):
        """Transmutes the height of the arcane figure."""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Calculates the enchanting area."""
        return self.__width * self.__height

    def perimeter(self):
        """Reveals the mystical perimeter."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __del__(self):
        """Concludes the spellbinding Rectangle."""
        print("Bye rectangle...")
