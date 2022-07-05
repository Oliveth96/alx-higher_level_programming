#!/usr/bin/python3
""" Module that writes a string and returns the number of characters written
"""


def write_file(filename="", text=""):
    """write_file writes a string to a text file.
    Args:
        filename: name of the file.
        text: text to be written.
    Returns: The number of bytes written.
    """
    with open(filename, mode="w", encoding="UTF-8") as x:
        return (x.write(text))
