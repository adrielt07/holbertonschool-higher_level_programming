#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class mytest(unittest.TestCase):

    def test_output(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([-1, -4, -3, -2]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 00]), 2)

    def test_mathop(self):
        self.assertEqual(max_integer([5+5, 1, 3, 5]), 10)
        self.assertEqual(max_integer([10-2, 1, 3, 5]), 8)
        self.assertEqual(max_integer([5*5, 1, 3, 5]), 25)

    def test_string(self):
        self.assertEqual(max_integer(["a", "str", "hi", "hello"]), "str")

    def test_float(self):
        self.assertEqual(max_integer([1.1, 2.3, 4.6]), 4.6)
        self.assertEqual(max_integer([-1.1, -2.3, -4.6]), -1.1)
        self.assertEqual(max_integer([-1.1, -2.3, 5]), 5)

    def test_list(self):
        self.assertIs(list, list)

    def test_none(self):
        self.assertRaises(TypeError, max_integer, None,
                          msg="object of type 'NoneType' has no len()")
        self.assertRaises(TypeError, max_integer, [1, 3, None],
                          msg="unorderable types: NoneType() > int()")

    def test_Error(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "str"],
                          msg="unorderable types: str() > int()")
        self.assertRaises(TypeError, max_integer, [1, 2, 3+5j],
                          msg="unorderable types: str() > complex()")
