#!/usr/bin/python3
""" Module providing a class tat inherits from a list
"""


class myList(list):
    """ Defines the class MyList that inherits from list.
    """
    def print_sorted(self):
        """Prints list elements(int) in ascending order"""

        sortedList = sorted(self)
        print(sortedList)
