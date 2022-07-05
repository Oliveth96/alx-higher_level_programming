#!/usr/bin/python3
"""Module that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """

    newText = ""
    with open(filename) as r:
        for line in r:
            newText += line
            if search_string in line:
                newText += new_string
    with open(filename, "x") as x:
        x.write(newText)
