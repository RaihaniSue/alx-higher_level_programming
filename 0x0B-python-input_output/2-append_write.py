#!/usr/bin/python3
"""
Append to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and
    returns the number of characters added.
    Args:
    filename (str): The path to the file.
    text (str): The text to be appended to the file.

    Returns:
    int: The number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
