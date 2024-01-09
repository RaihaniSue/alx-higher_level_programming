#!/usr/bin/python3
"""
To JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Args:
    my_obj: The object to be converted to a JSON string.
    Returns:
    str: The JSON representation of the input object.
    """
    return json.dumps(my_obj)
