#!/usr/bin/python3
""" Module that defines a 'Square'
"""


class Square():
    """An empty definition of a 'Square'
    """
    __size = True

    def __init__(self, size=0):

        """ Instantiates a 'Square'
        """
        self.size = size

    @property
    def size(self):
        """" to retrieve it
        """
        return self.__size

    @size.setter
    def size(self, size):
        """to set it
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns the current 'Square' area
        """
        return self.__size ** 2
