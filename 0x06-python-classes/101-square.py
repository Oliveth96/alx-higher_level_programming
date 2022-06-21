#!/usr/bin/python3
""" Module that defines a class 'Square'
"""


class Square():
    """ The definition of a 'Square'
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiates a 'Square'
        """
        self.size, self.position = size, position

    def __str__(self):
        """ Create a visual representation of a square
        """
        if self.size:
            return '\n' * self.position[1] + '\n'.join(
                [' ' * self.position[0] + '#' * self.size] * self.size
            )
        return str()

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

    @property
    def position(self):
        """" to retrieve it
        """
        return self.__position

    @position.setter
    def position(self, position):
        """to set it
        """
        if not (isinstance(position, tuple) and
                len(position) == 2 and
                isinstance(position[0], int) and
                isinstance(position[1], int) and
                position[0] >= 0 and
                position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ returns the current 'Square' area
        """
        return self.size ** 2

    def my_print(self):
        """ that prints in stdout the 'Square' 
        """
        print(self)
