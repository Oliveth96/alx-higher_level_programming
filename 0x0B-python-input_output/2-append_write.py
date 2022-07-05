#!/usr/bin/python3
""" Module that appends a string and returns the number of characters
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns ..
    Args:
        filename: The name of the file to append
        text: The string to apple to the file.
    Returns: The number of characters added.
    """
    with open(filename, mode="w", encoding="UTF-8") as x:
        return x.write(text)
