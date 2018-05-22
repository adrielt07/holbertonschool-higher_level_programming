#!/usr/bin/python3
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
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

    """Testing all static methods"""
    def test_staticmethod(self):
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
