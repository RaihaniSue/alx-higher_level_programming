#!/usr/bin/python3
""" The Majestic Square Inherits the Essence of Geometry """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Marvelous Square in the Realm of Shapes """

    def __init__(self, size, x=0, y=0, id=None):
        """ Unveiling the Square Constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Gazing into the Dimension of Size - Read Access """
        return self.width

    @size.setter
    def size(self, value):
        """ Reshaping the Square - Size Setter """
        self.width = value
        self.height = value

    def __str(self):
        """ The Square's Tale - String Representation """
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method to update instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ Weaving the Square's Destiny - Update Method """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ The Square's Chronicles - Dictionary Representation """
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["size"] = self.size
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
