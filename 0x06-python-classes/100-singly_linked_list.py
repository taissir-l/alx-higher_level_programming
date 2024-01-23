#!/usr/bin/python3
"""singly linked list in python"""


class Node:
    """nodecof s linked list"""

    def __init__(self, data, next_node=None):
        """data nd next_node

        Args:
            data: one element(int)
            next_node: pointer to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """gives value of data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """nze value of data

        Args:
            value: to replace value
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """go to next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """next_node value
        Args:
            value:replacement
        """
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly Linked List"""

    def __init__(self):
        """init of sLL"""
        self.__head = None

    def sorted_insert(self, value):
        """the node in sorted linked list

        Args:
            value: to insert
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None
                   and current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """what to print ed when SSL use print"""
        value = []
        cur = self.__head
        while cur is not None:
            value.append(str(cur.data))
            cur = cur.next_node
        return ('\n'.join(value))

