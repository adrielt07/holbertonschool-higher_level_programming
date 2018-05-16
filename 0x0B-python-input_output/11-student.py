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

    def to_json(self):
        """
        retrieves a dictionaru representation of a student instance
        """
        return self.__dict__
