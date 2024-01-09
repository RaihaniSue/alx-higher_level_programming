#!/usr/bin/python3
""" Load, add, save  """
from sys import argv
# Importing functions from other files
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""
Script that adds all arguments to a Python list,
and then saves them to a file
"""
try:
    # Load existing list from a JSON file
    add_i = load_from_json_file('add_item.json')
    # Concatenate loaded list with new arguments and save
    save_to_json_file(add_i + argv[1:], 'add_item.json')
except Exception:
    # If file loading fails, create a new file with arguments
    save_to_json_file(argv[1:], 'add_item.json')
