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
        r1 = Rectangle(2, 3, 4, 5)
        r2 = Rectangle(1, 3, 4)
        r3 = Rectangle(1, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r3.x, 0)
        with self.assertRaises(TypeError):
            """testing for none valid instantiation"""
            r1 = Rectangle()
            r2 = Rectangle(1)
            r3 = Rectangle("1", 3, 6)
            r4 = Rectangle(1.5, 2, 3)
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 0, 3)
            r6 = Rectangle(-1, 3, 5)
            r7 = Rectangle(2, 4, -1)
            r8 = Rectangle(6, 7, 8, -2)

    def test_for_int(self):
        obj = Rectangle(2, 3, 4, 5, 7)
        """testing if a none integer value is set to the attribute"""
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
            obj.height = [5, 6]

    def test_value(self):
        obj = Rectangle(2, 4, 5, 6, 7)
        """testing if the right type of obj but with improper value is
            passed
        """
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

    def test_3_update(self):
        """testing if the method raises an exception"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 10, 10, 10, 10)
            r.update(width=True, height=1)
            r.update(width="2", height=4, x=5)
            r.update(width=4.5, height=9)
            r.update(height=True)
            r.update(height="60")
            r.update(height=8.999)
            r.update(x=8.8)
            r.update(y=8.0)
            r.update(x=True)
            r.update(y=False)
            r.update(x="6")
            r.update(y="7")

    def test_to_dictionary(self):
        """testing the to_dictionary method that returns a dictionary
            of the instance attribute
        """
        r = Rectangle(10, 10, 10, 10, 10)
        dic = r.to_dictionary()
        self.assertEqual(dic, {
            "width": 10, "height": 10,
            "x": 10, "y": 10, "id": 10
            })
        r.update(1, 3, 4)
        dic = r.to_dictionary()
        self.assertEqual(dic, {
            "width": 1, "height": 3,
            "x": 4, "y": 10, "id": 10
            })
