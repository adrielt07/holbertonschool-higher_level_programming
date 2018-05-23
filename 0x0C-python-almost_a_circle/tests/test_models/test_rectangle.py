#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Rectangle(unittest.TestCase):

    def test_docstring(self):
        self.assertTrue(len(Rectangle.__doc__) > 1)
        self.assertTrue(len(Rectangle.__init__.__doc__) > 1)
        self.assertTrue(len(Rectangle.width.__doc__) > 1)
        self.assertTrue(len(Rectangle.height.__doc__) > 1)
        self.assertTrue(len(Rectangle.x.__doc__) > 1)
        self.assertTrue(len(Rectangle.y.__doc__) > 1)
        self.assertTrue(len(Rectangle.checkatt.__doc__) > 1)
        self.assertTrue(len(Rectangle.area.__doc__) > 1)
        self.assertTrue(len(Rectangle.display.__doc__) > 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) > 1)
        self.assertTrue(len(Rectangle.update.__doc__) > 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 1)

    def test_variables(self):
        r1 = Rectangle(2, 4, 6, 9, 10)
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 9)
        r1.width = 7
        self.assertEqual(r1.width, 7)
        r1.height = 11
        self.assertEqual(r1.height, 11)
        r1.x = 8
        self.assertEqual(r1.x, 8)
        r1.y = 5
        self.assertEqual(r1.y, 5)
        """Error"""
        self.assertRaises(TypeError, Rectangle, "string", 3)
        self.assertRaises(TypeError, Rectangle, 4, "string")
        self.assertRaises(TypeError, Rectangle, 2, 4, "string")
        self.assertRaises(TypeError, Rectangle, 2, 4, 3, "string")
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 2)
        self.assertRaises(ValueError, Rectangle, -1, 3)
        self.assertRaises(ValueError, Rectangle, 4, -2)
        self.assertRaises(ValueError, Rectangle, 2, 4, -3)
        self.assertRaises(ValueError, Rectangle, 2, 4, 3, -4)

    def test_area(self):
        r2 = Rectangle(2, 3, 4, 5, 20)
        self.assertEqual(r2.area(), 6)

    def test_update(self):
        r3 = Rectangle(2, 5, 1, 2, 30)
        r3.update(4, 2, 3, 5, 14)
        self.assertEqual(r3.id, 4)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 3)
        self.assertEqual(r3.x, 5)
        self.assertEqual(r3.y, 14)
        r3.update(width=10, height=12, x=6, y=7)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 12)
        self.assertEqual(r3.x, 6)
        self.assertEqual(r3.y, 7)

    def test_str(self):
        r4 = Rectangle(3, 3, 5, 6, 8)
        self.assertEqual(r4.__str__(), "[Rectangle] (8) 5/6 - 3/3")
