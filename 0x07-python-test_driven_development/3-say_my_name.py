#!/usr/bin/python3
"""
3-say_my_name - has one def
def(s):
1) say_my_name - prints 'My name is first_name Last_name'
"""


def say_my_name(first_name, last_name=""):
     """
     Prints - My name is first_name last_name

     args:

     first_name
     Requirements:
     1) Must be a string

     last_name
     Requirements:
     1) Must be a string
     2) Default value is ""

     Failure to meet the requirements will raise an exception
     """
     if isinstance(first_name, str) is False:
          raise TypeError("first_name must be a string")
     if isinstance(last_name, str) is False:
          raise TypeError("last_name must be a string")

     print("My name is {} {}".format(first_name, last_name))
