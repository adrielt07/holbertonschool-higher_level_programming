#!/usr/bin/python3
"""Module has one def - number_of_lines()"""


def number_of_lines(filename=""):
    """Funtion that returns the number of lines of a test"""
    n = 0
    with open(filename) as f:
        for line in f:
            n += 1
    return n
