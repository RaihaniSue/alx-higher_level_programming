#!/usr/bin/python3
"""
The Rectangle class at this stage involves the creation of private
instance attributes through the acceptance of two arguments: width
and height.

Args:
    width (int): Represents the horizontal dimension of the
                 rectangle, defaults to 0.
    height (int): Represents the vertical dimension of the
                  rectangle, defaults to 0.

Attributes:
    __width (int): Private attribute denoting the horizontal
                   dimension of the rectangle.
    __height (int): Private attribute denoting the vertical
                    dimension of the rectangle.

The class implements getter and setter methods for width and
height to ensure appropriate manipulation and validation of these
attributes.
"""


class Rectangle:

    """
    This class initializes with private attributes for width and
    height, using setters and getters to manage and validate them.
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
        """Setter method for the private attribute __width.

        Args:
            value (int): Represents the horizontal dimension of
                         the rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
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
        """Setter method for the private attribute __height.

        Args:
            value (int): Represents the vertical dimension of the
                         rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
