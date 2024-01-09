#!/usr/bin/python3
"""
Defines a function that reads a text file (UTF-8) and prints
its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content.

    Args:
    filename (str): The path to the file. Defaults to an empty
    string.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
