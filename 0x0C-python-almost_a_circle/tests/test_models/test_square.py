#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Square(unittest.TestCase):

    def test_docstring(self):
        self.assertTrue(len(Square.__doc__) > 1)
        self.assertTrue(len(Square.__init__.__doc__) > 1)
        self.assertTrue(len(Rectangle.width.__doc__) > 1)
        self.assertTrue(len(Square.height.__doc__) > 1)
        self.assertTrue(len(Square.x.__doc__) > 1)
        self.assertTrue(len(Square.y.__doc__) > 1)
        self.assertTrue(len(Square.checkatt.__doc__) > 1)
        self.assertTrue(len(Square.area.__doc__) > 1)
        self.assertTrue(len(Square.display.__doc__) > 1)
        self.assertTrue(len(Square.__str__.__doc__) > 1)
        self.assertTrue(len(Square.update.__doc__) > 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) > 1)

    def test_variables(self):
        s1 = Square(2, 6, 9, 10)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.x, 6)
        self.assertEqual(s1.y, 9)
        s1.width = 7
        self.assertEqual(s1.width, 7)
        s1.size = 11
        self.assertEqual(s1.size, 11)
        s1.x = 8
        self.assertEqual(s1.x, 8)
        s1.y = 5
        self.assertEqual(s1.y, 5)
        """Error"""
        self.assertRaises(TypeError, Square, "string", 3)
        self.assertRaises(TypeError, Square, 4, "string")
        self.assertRaises(TypeError, Square, 2, 4, "string")
        self.assertRaises(TypeError, Square)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 4, -2)
        self.assertRaises(ValueError, Square, 2, 4, -3)

    def test_area(self):
        s2 = Square(3, 4, 5, 20)
        self.assertEqual(s2.area(), 9)

    def test_update(self):
        s3 = Square(2, 1, 2, 30)
        s3.update(4, 3, 5, 14)
        self.assertEqual(s3.id, 4)
        self.assertEqual(s3.width, 3)
        self.assertEqual(s3.x, 5)
        self.assertEqual(s3.y, 14)
        s3.update(width=10, x=6, y=7)
        self.assertEqual(s3.width, 10)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 6)
        self.assertEqual(s3.y, 7)

    def test_str(self):
        s4 = Square(3, 5, 6, 8)
        self.assertEqual(s4.__str__(), "[Square] (8) 5/6 - 3")

    def test_to_dictionary_and_create(self):
        s4 = Square(5, 8, 9, 3)
        s4_dictionary = s4.to_dictionary()
        self.assertIsInstance(s4_dictionary, dict)
        s5 = s4.create(**s4_dictionary)
        self.assertIsInstance(s5, Square)
        self.assertEqual(s5.width, 5)
        dummy_dictionary = {}
        self.assertEqual(Base.create(**dummy_dictionary), None)
