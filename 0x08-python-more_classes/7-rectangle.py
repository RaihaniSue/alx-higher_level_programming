#!/usr/bin/python3
"""
Rectangle module.

Contains a class defining an intriguing rectangle.
"""


class Rectangle():
    """Shapes a captivating rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initiates attributes for the Rectangle object.

        Args:
            width (int): width of the mesmerizing rectangle.
            height (int): height of the fascinating rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Creates a visual of the breathtaking Rectangle."""
        rectangle = ""
        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'
        return rectangle[:-1]

    def __repr__(self):
        """Defines the essence of the Rectangle's allure."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """Reveals the width of the enchanting rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Adjusts the width of the mesmerizing entity."""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Unveils the height of the fascinating rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Adjusts the height of the fascinating figure."""
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
        """Reveals the magical perimeter."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __del__(self):
        """Concludes the mesmerizing Rectangle experience."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
