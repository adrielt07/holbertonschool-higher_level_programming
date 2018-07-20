#!/usr/bin/python3
"""
Defines class node
"""


class Node:
    """Creates a node"""
    def __init__(self, data, next_node=None):
        """Initialization"""
        if isinstance(data, int) is False:
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Return the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """change the value of data"""
        if isinstance(data, int) is False:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """return next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """change the value of next_node"""
        if isinstance(value, Node) is False:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList(Node):
    """Creates a node"""
    def __init__(self, head=None):
        """Initialization"""
        self.__head = head

    def size(self):
        """Return the size of node"""
        current = self.__head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def sorted_insert(self, value):
        """Insert new node in ascending order"""
        if self.__head is None or self.__head.data > value:
            new_node = Node(value)
            if self.__head is not None:
                new_node.next_node = self.__head
            self.__head = new_node
        else:
            runner = self.__head
            while runner.next_node and value > runner.next_node.data:
                runner = runner.next_node
            runner.next_node = Node(value, runner.next_node)

    def __str__(self):
        """Prints all the node value"""
        runner = self.__head
        if runner is None:
            return ""
        while runner.next_node:
            if runner is not None:
                print("{}".format(runner.data))
            runner = runner.next_node
        return "{}".format(runner.data)
