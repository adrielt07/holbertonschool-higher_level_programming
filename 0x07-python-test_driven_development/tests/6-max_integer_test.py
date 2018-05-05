#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
my_list=[1, 2, 3, 4]

class mytest(unittest.TestCase):

    def test_output(self):
        self.assertAlmostEqual(max_integer(my_list), 4)
        self.assertAlmostEqual(max_integer(my_list), 4)
        self.assertAlmostEqual(max_integer([]), None)

    def test_listtype(self):
        self.assertNotIsInstance(max_integer(my_list), list, msg="Error")

    def test_numtype(self):
        self.assertRaises(TypeError, max_integer, "str")
        self.assertRaises(TypeError, max_integer, 3+5j)
        self.assertRaises(TypeError, max_integer, True)
