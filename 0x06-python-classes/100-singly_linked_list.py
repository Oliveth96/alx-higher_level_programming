#!/usr/bin/python3
""" module that defines a node of a singly linked list
"""


class Node():
    """The definition of a singly-linked list node
    """

    def __init__(self, data, next_node=None):
        """ Instantiates a node
        """
        self.data, self.next_node = data, next_node

    @property
    def data(self):
        """" to retrieve it
        """
        return self.__data

    @data.setter
    def data(self, data):
        """to set it
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """" to retrieve it
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """to set it
        """
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList():
    """ The definition of a singly-linked list
    """
    def __init__(self):
        """ Instantiates a singly-linked list
        """
        self.__head = None

    def __str__(self):
        """ Generate a visual representation of a list
        """

    def sorted_insert(self, value):
        """ Inserts a Node into a list sorted in ascending order
        """
