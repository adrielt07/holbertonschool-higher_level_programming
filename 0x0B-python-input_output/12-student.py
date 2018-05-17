#!/usr/bin/python3
"""
Module has one class:
Student
"""


class Student:
    """Information that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializing variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            if isinstance(attrs, list) is True:
                for elem in attrs:
                    for key, val in self.__dict__.items():
                        if elem == key:
                            new_dict[elem] = val
            return new_dict
