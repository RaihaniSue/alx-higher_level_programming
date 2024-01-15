#!/usr/bin/python3
'''Unleash the Infinite - Module for the Mighty Base class.'''


class Base:
    '''The Epicenter of OOP - A base echoing through eternity.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''The Genesis - Constructor that sets the cosmic identifier.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # The Orb of Countless Identities
