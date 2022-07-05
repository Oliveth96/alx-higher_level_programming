#!/usr/bin/python3
"""Module that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.
    """
    with open(filename, 'r+') as x:
        lines = [
            line + new_string * (search_string in line)
            for line in x.readlines()
        ]
        x.seek(0)
        x.writelines(lines)
