#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class mytest(unittest.TestCase):

    def test_output(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertAlmostEqual(max_integer([-1, -4, -3, -2]), -1)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 2, 00]), 2)

    def test_list(self):
        self.assertIs(list, list)

    def test_none(self):
        self.assertRaises(TypeError, max_integer, None,
                          msg="object of type 'NoneType' has no len()")

    def test_type(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "str"],
                          msg="unorderable types: str() > int()")
        self.assertRaises(TypeError, max_integer, [1, 2, 3+5j],
                          msg="unorderable types: str() > complex()")
