#!/usr/bin/python3
""" Generate an object from a JSON file """
import json


def load_from_json_file(filename):
    """ Reads a JSON file to create an object """
    with open(filename, 'r') as f:
        return json.load(f)
