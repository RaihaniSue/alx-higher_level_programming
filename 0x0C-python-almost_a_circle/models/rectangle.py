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

    def area(self):
        """Unveiling the Mathematical Realm - Calculating the Grand Area"""
        return (self.__height * self.__width)

    def display(self):
        """Summoning the Rectangular Display - Unveiling the Majesty"""
        myhash = "#"
        if self.width == 0 or self.height == 0:
            return
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x, end='')
            print(myhash * self.width)

    def update(self, *args, **kwargs):
        """Bridging Realities - Updating the Rectangle with Args and Kwargs"""
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.width = j
                elif i == 3:
                    self.x = j
                elif i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """Unveiling the Rectangular Essence - String Format Revelation"""
        st = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        st = st.format(self.id, self.x, self.y, self.width, self.height)
        return st

    def to_dictionary(self):
        """Summoning the Rectangular Dictionary - A Chronicle of Attributes"""
        recdic = {"id": self.id, "width": self.width, "height": self.height,
                  "x": self.x, "y": self.y}
        return recdic
