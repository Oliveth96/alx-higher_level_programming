#!/usr/bin/python3
""" Module providing  the list of available attributes and methods of an object
"""


def lookup(obj):
    """ Defines the list of available attributes and methods of an object
    """
    return (dir(obj))
