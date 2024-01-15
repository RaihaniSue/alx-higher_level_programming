#!/usr/bin/python3
'''Unleash the Infinite - Module for the Mighty Base class.'''
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries to JSON string."""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list of objects to a JSON file."""
        jlist = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                jlist.append(i.to_dictionary())

        st = cls.to_json_string(jlist)
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(st)

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string to a list of dictionaries."""
        if not json_string or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Creates an object based on the provided dic.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Loads objects from a JSON file."""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves list of objects to a CSV file."""
        filename = cls.__name__ + ".csv"
        csvlist = []
        if list_objs:
            for i in list_objs:
                dic = i.to_dictionary()
                if cls.__name__ == "Rectangle":
                    csvlist.append([dic["id"], dic["width"],
                                    dic["height"], dic["x"], dic["y"]])
                elif cls.__name__ == "Square":
                    csvlist.append([dic["id"], dic["size"],
                                    dic["x"], dic["y"]])

        with open(filename, "w", encoding="utf-8") as myfile:
            w = csv.writer(myfile)
            w.writerows(csvlist)

    @classmethod
    def load_from_file_csv(cls):
        """Loads objects from a CSV file."""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, encoding="utf-8") as myfile:
                r = csv.reader(myfile)
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    attr = ["id", "size", "x", "y"]
                inslist = []
                for row in r:
                    ct, dic = 0, {}
                    for i in row:
                        dic[attr[ct]] = int(i)
                        ct += 1
                    inslist.append(cls.create(**dic))
                return inslist
        except IOError:
            return []
