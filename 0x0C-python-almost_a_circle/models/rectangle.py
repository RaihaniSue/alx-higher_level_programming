#!/usr/bin/python3
"""Unleashing the Powers of Rectangles - A Rectangular Tale"""
from models.base import Base


class Rectangle(Base):
    """Embarking on the Rectangular Odyssey"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Crafting the Dimensions - Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """The Enigma of Width in this Rectangular Saga"""
        return self.__width

    @width.setter
    def width(self, value):
        """Channeling the Essence of Width - Setter"""
        if type(value) is not int:
            raise TypeError("integer, please")
        elif value <= 0:
            raise ValueError("is it positive?")
        else:
            self.__width = value

    @property
    def height(self):
        """The Ascension of Height in the Rectangular Tapestry"""
        return self.__height

    @height.setter
    def height(self, value):
        """Elevating the Heights - Setter"""
        if type(value) is not int:
            raise TypeError("is it integer?")
        elif value <= 0:
            raise ValueError("note if height is pos")
        else:
            self.__height = value

    @property
    def x(self):
        """The Mystical x-coordinate in the Rectangle's Journey"""
        return self.__x

    @x.setter
    def x(self, value):
        """Unveiling the Secrets of x - Setter"""
        if type(value) is not int:
            raise TypeError("note if x is integer")
        elif value < 0:
            raise ValueError("note if x is positive")
        else:
            self.__x = value

    @property
    def y(self):
        """The Enchanted y-coordinate in the Rectangle's Odyssey"""
        return self.__y

    @y.setter
    def y(self, value):
        """Unleashing the Force of y - Setter"""
        if type(value) is not int:
            raise TypeError("note if y is integer")
        elif value < 0:
            raise ValueError("note if y is positive")
        else:
            self.__y = value
