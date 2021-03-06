#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    def test_doc(self):
        self.assertTrue(len(Base.__doc__) > 1)
        self.assertTrue(len(Base.__init__.__doc__) > 1)
        self.assertTrue(len(Base.save_to_file.__doc__) > 1)
        self.assertTrue(len(Base.create.__doc__) > 1)
        self.assertTrue(len(Base.load_from_file.__doc__) > 1)
        self.assertTrue(len(Base.to_json_string.__doc__) > 1)
        self.assertTrue(len(Base.from_json_string.__doc__) > 1)
        self.assertTrue(len(Base.checkattr.__doc__) > 1)

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(22)
        self.assertEqual(b3.id, 22)

    def test_inheritance(self):
        r1 = Rectangle(2, 3)
        s1 = Square(4)
        self.assertTrue(issubclass(type(r1), Base))
        self.assertTrue(issubclass(type(s1), Base))

    def test_save_to_file(self):
        self.assertEqual(Base.save_to_file(None), None)

    """Testing all static methods"""
    def test_checkattr(self):
        """Test value error"""
        self.assertRaises(ValueError, Base.checkattr, -1, 1)
        self.assertRaises(ValueError, Base.checkattr, -1, 2)
        self.assertRaises(ValueError, Base.checkattr, -1, 3)
        self.assertRaises(ValueError, Base.checkattr, -1, 4)
        """Test Type passed"""
        self.assertRaises(TypeError, Base.checkattr, "str", 1)
        self.assertRaises(TypeError, Base.checkattr, "str", 2)
        self.assertRaises(TypeError, Base.checkattr, "str", 3)
        self.assertRaises(TypeError, Base.checkattr, "str", 4)
        self.assertRaises(TypeError, Base.checkattr, None, 4)
        self.assertRaises(TypeError, Base.checkattr, None)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        empty = {}
        self.assertEqual(Base.to_json_string(empty), "[]")
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        result = Base.to_json_string(dictionary)
        self.assertEqual(result, str(result))
        string = "testing"
        self.assertEqual(Base.to_json_string(string), '"testing"')
        self.assertEqual(Base.to_json_string([12, 42, 32]), '[12, 42, 32]')
        """Exceptions"""
        self.assertRaises(TypeError, Base.to_json_string, -1)
        self.assertRaises(TypeError, Base.to_json_string, 1234)
        self.assertRaises(TypeError, Base.to_json_string, 13.24)

    def test_from_json_string(self):
        string = '[{"height": 4, "width": 10, "id": 89}, \
        {"height": 7, "width": 1, "id": 7}]'
        self.assertEqual(Base.from_json_string(string),
                         [{'height': 4, 'width': 10, 'id': 89},
                          {'height': 7, 'width': 1, 'id': 7}])
        self.assertEqual(Base.from_json_string(None), [])
        """Exceptions"""
        self.assertRaises(TypeError, Base.from_json_string, 123)
        self.assertRaises(ValueError, Base.from_json_string, "sada")
