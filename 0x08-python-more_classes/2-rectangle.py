#!/usr/bin/python3
"""

    width (int): horizontal dimension of rectangle, defaults to 0
    height (int): vertical dimension of rectangle, defaults to 0
"""


class Rectangle:
    """
    This class initializes with private attributes for width and
    height, using setters and getters to manage and validate them.
    It also computes area and perimeter of the rectangle.
    """
    def __init__(self, width=0, height=0):
        # attribute assignment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the private attribute __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the private attribute __width."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for the private attribute __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the private attribute __height."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns area of a rectangle of given `width` and `height`."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of a rec of given `width` n `height`."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
