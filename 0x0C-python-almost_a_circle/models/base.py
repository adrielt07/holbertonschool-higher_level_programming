#!/usr/bin/python3
"""
Module only has one Class: Base
"""
import json


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
            try:
                for inst in list_objs:
                    if issubclass(type(inst), Base):
                        new_list.append(inst.to_dictionary())
                s = cls.to_json_string(new_list)
                f.write(s)
            except:
                f.write("[]")

    @classmethod
    def create(cls, **dictionary):
        """
        converts dictionary to instance
        """
        try:
            if cls.__name__ == "Square":
                tmp = cls(1)
            if cls.__name__ == "Rectangle":
                tmp = cls(1, 1)
            tmp.update(**dictionary)
            return tmp
        except:
            return None

    @classmethod
    def load_from_file(cls):
        """
        creates new instance(s) from file
        """
        new_list = []
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                for line in f:
                    old_list = []
                    s = ""
                    s = line
                    old_list = cls.from_json_string(s)
                    for elem in old_list:
                        new_list.append(cls.create(**elem))
                return new_list
        except:
            return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        import csv

        try:
            table_elem = [x.to_dictionary() for x in list_objs]
        except:
            table_elem = '[]'
        with open("{}.csv".format(cls.__name__), "w") as csvfile:
            elemwriter = csv.DictWriter(csvfile, table_elem[0].keys())
            elemwriter.writeheader()
            elemwriter.writerows(table_elem)

    @classmethod
    def load_from_file_csv(cls):
        import csv

        try:
            with open("{}.csv".format(cls.__name__), "r") as csvfile:
                reader = csv.DictReader(csvfile)
                elem = [row for row in reader]
                for row in elem:
                    for key, val in row.items():
                        try:
                            row[key] = int(val)
                        except:
                            pass
            return [cls.create(**elems) for elems in elem]
        except:
            return []

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
        return loader

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
