#!/usr/bin/python3
"""
From JSON string to Object.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented
    by a JSON string.
    Args:
    my_str (str): The JSON string to convert.
    Returns:
    object: The Python data structure represented by the
    input JSON string.
    """
    return json.loads(my_str)
