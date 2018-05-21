#!/usr/bin/python3
import json
import copy
"""Module only has one Class: Base"""

class Base:
    """Class for Shapes Class to inherent from"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize instance variables

        Purpose: Assigned an id for each instance
        Usages:
        b1 = Base(12)
        b1 will have id of 12 (b1.id)

        if no id specified, id will automatically get assigned
        starting from 1 and increments by 1 each call
        b2 = Base()
        b2 will ahve id of 1 (b2.id)
        b3 = Base()
        b3 will have id of 2 (b2.id)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        with open("{}.json".format(cls.__name__), "w") as f:
            new_list = []
            s = ""
            for inst in list_objs:
                new_list.append(inst.to_dictionary())
            s = cls.to_json_string(new_list)
            f.write(s)

    @classmethod
    def create(cls, **dictionary):
        """
        converts dictionary to instance
        """
        tmp = cls(1, 1)
        tmp.update(**dictionary)
        return tmp


    @classmethod
    def load_from_file(cls):
        """
        creates new instance(s) from file
        s = ""
        open("{}.json".format(cls.__name__, "r")) as f:
             for line in f.readline():
                 pass
        """
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts list to string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts string to list
        """
        if json_string is None or len(json_string) == 0:
            return []
        loader = json.loads(json_string)
        new_list = []
        new_list.append(loader)
        return new_list

    @staticmethod
    def checkattr(value, num):
        """
        Validates the follow attributes
        1 = width
        2 = height
        3 = x
        4 = y
        """
        if num == 1:
            if isinstance(value, int) is False:
                raise TypeError("width must be an integer")
            if value < 1:
                raise ValueError("width must be > 0")
        elif num == 2:
            if isinstance(value, int) is False:
                raise TypeError("height must be an integer")
            if value < 1:
                raise ValueError("height must be > 0")
        elif num == 3:
            if isinstance(value, int) is False:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
        elif num == 4:
            if isinstance(value, int) is False:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
        else:
            return None
