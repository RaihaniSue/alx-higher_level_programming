#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """ Convert object to a dictionary using simple data types
    (list, dict, str, int, bool) for JSON serialization """
    return obj.__dict__
