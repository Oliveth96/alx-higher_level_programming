#!/usr/bin/python3
"""Module that writes an Object to a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Returns the object using JSON representation.
    """
    with open(filename, 'w') as x:
        json.dump(my_obj, x)
