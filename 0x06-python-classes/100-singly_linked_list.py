#!/usr/bin/python3
""" module that defines a node of a singly linked list
"""


class Node():
    """The definition of a singly-linked list node
    """

    def __init__(self, data, next_node=None):
        """ Instantiates a node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """" to retrieve it
        """
        return (self.__data)

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
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """to set it
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """ The definition of a singly-linked list
    """

    def __init__(self):
        """ Instantiates a singly-linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a Node into a list sorted in ascending order
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """ Generate a visual representation of a list
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
