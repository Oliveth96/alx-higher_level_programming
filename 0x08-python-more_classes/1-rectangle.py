#!/usr/bin/python3
""" Module that defines a 'Rectangle'
"""


class Rectangle():
    """An empty definition of a 'Rectangle'
    """
    width = True
    height = True

    def __init__(self, width=0, height=0):

        """ Instantiates a 'Rectangle'
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ to retrieve it
        """
        return self.width

    @width.setter
    def width(self, width):
        """ to set it
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be an integer")
        self.width = width

    @property
    def height(self):
        """ to retrieve it
        """
        return self.height

    @height.setter
    def height(self, height):
        """ to set it
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
