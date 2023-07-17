#!/usr/bin/python3
"""A script that performs unit testing using the unittest module"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_instatiation(self):
        """testing if the init method, getters and setters works"""
        obj = Rectangle(2, 3, 4, 5, 7)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)
        self.assertEqual(obj.id, 7)
        obj.width = 10
        obj.height = 10
        obj.x = 10
        obj.y = 10
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 10)
        self.assertEqual(obj.x, 10)
        self.assertEqual(obj.y, 10)
        with self.assertRaises(TypeError):
            obj = Rectangle()
            obj = Rectangle(1)
            obj = Rectangle(1, 3)
            obj = Rectangle(1, 2, 3)
    def test_for_int(self):
        obj = Rectangle(2, 3, 4, 5, 7)
        """testing if a none integer value is passed"""
        with self.assertRaises(TypeError):
            obj.width = "2"
            obj.height = "5"
            obj.x = "1"
            obj.y = "2"
            obj.width = True
            obj.width = 5.78
            obj.height = False
            obj.height = 5.6
            obj.x = True
            obj.y = True
            obj.x = 6.8
            obj.y = 6.7
            obj.width = [33.6]
            obj.height = [5,6]
    def test_value(self):
        obj = Rectangle(2, 4, 5, 6, 7)
        """testing if the right type of obj but with improper value is passed"""
        with self.assertRaises(ValueError):
            obj.width = -1
            obj.width = 0
            obj.height = -2
            obj.height = 0
            obj.x = -1
            obj.y = -10 
    def test_area(self):
        """testing the area method"""
        obj = Rectangle(10, 10)
        self.assertEqual(obj.area(), 100)
        obj = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(obj.area(), 20)
    def test_update(self):
        """testing the update method"""
        obj = Rectangle(1, 2, 3, 4, 5)
        obj.update(10, 10, 10, 10, 10)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 10)
        self.assertEqual(obj.x, 10)
        self.assertEqual(obj.y, 10)
        self.assertEqual(obj.id, 10)
        obj.update(1, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 10)
        self.assertEqual(obj.y, 10)
        obj.update(1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        with self.assertRaises(TypeError):
            obj = Rectangle(True, 2, 4, 5, 7)
            obj = Rectangle(1, True, 3, 4, 5)
            obj = Rectangle("2", "3", 6, 7)
            obj = Rectangle(2.4, 6.8, 3.5, 4.5)
        with self.assertRaises(ValueError):
            obj = Rectangle(0, 1, 3)
            obj = Rectangle(1, 0, 0, 0)
            obj = Rectangle(-1, 2, 4, 6)
            obj = Rectangle(-2, 4, 6, 7)
            obj = Rectangle(1, 2, -1, -2)
    def test_2_update(self):
        """testing update method with keyword arguments"""
        obj = Rectangle(10, 2, 4, 5, 7)
        obj.update(width=2, height=3, x=2, y=2, id=7)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 2)
        self.assertEqual(obj.id, 7)
        obj.update(width=1, height=2, x=2, y=2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 2)
        obj.update(width=3, height=4, x=2)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 2)
        obj.update(width=10, height=4)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 4)
        obj.update(height=3)
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 2)
