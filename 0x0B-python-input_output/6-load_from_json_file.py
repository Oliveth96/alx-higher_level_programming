#!/usr/bin/python3
"""Module that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """ Creates an object using with statement
    """
    with open(filename) as x:
        return json.load(x)
