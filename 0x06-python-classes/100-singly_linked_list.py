#!/usr/bin/python3
"""
Defines class node
"""

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

class Node:
    def __init__(self, data, next_node=None):
        if isinstance(data, int) is False:
            raise TypeError("data must be an integer")
        self.data = data
        self.next_node = next_node

    def data(self):
        return self.data

    def next_node(self):
        return self.next_node
