#!/usr/bin/python3
'''Unlocking the Rectangle Realms - Module for the Rectangular Marvel.'''
from models.base import Base


class Rectangle(Base):
    '''A Dimensional Marvel - The Rectangle Class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Crafting the Dimensions - Constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''The Enigma of Width in this Rectangular Saga.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''The Ascension of Height in the Rectangular Tapestry.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''The Mystical x-coordinate in the Rectangle's Journey.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''The Enchanted y-coordinate in the Rectangle's Odyssey.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value
