#!/usr/bin/python3
""" Module that appends a string and returns the number of characters
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns ..
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as x:
        return x.write(text)
