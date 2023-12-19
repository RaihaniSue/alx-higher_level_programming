#!/usr/bin/python3
"""
Class for representing a Node and a Singly Linked List.
"""


class Node:
    """ Node class for a singly linked list.

    Attributes:
        data (int): Data stored in the node.
        next_node (Node, optional): Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initialize a Node object.

        Args:
            data (int): Data stored in the node.
            next_node (Node): Reference to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for retrieving node data.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for setting node data.

        Args:
            value (int): The value to set as node data.

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method for retrieving the next node reference.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for setting the next node reference.

        Args:
            value (Node): The node to set as the next node.

        Returns:
            None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node in the correct sorted position.

        Args:
            value (int): Value for the new node.
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
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
