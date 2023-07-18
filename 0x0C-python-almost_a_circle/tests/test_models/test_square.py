#!/usr/bin/python3
"""A test script utilizing unittest module to test the feature of a class"""
import unittest
from models.square import Square


class Test_Square(unittest.TestCase):
    """tests the features of Square class"""
    def test_initialization(self):
        """testing the initialisation of the class"""
        s = Square(10, 1, 3, 7)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 7)
        with self.assertRaises(TypeError):
            s = Square()
            s = Square(10)
            s = Square(10, 1)
        with self.assertRaises(ValueError):
            s = Square(0, 1, 3, 7)
            s = Square(-1, 2, 3, 7)
            s = Square("1", 2, 4, 5)
            s = Square(1, -1, -2, 0)
            s = Square(2, "2", 4.5)
            s = Square(7, True, 6)
            s = Square(5, 3, "1")
            s = Square(4, 5, True)
            s = Square(3, 5, 2.5)

    def test_properties(self):
        """test getter and setter methods"""
        s = Square(10, 1, 3, 7)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 7)
        s = Square(11, 2, 5)
        self.assertEqual(s.size, 11)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 5)

    def test_update_square(self):
        """test update method"""
        s = Square(1, 2, 3, 4)
        s.update(2, 4, 6, 8)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)
        self.assertEqual(s.id, 8)
        s.update(10, 2, 4,)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 4)
        self.assertEqual(s.id, 8)
        s.update(50, 0)
        self.assertEqual(s.size, 50)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 4)
        s.update(2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 0)
        s.update()
        self.assertEqual(s.size, 2)

    def test2_update_square(self):
        """testing the update method with keyword arguments"""
        s = Square(1, 2, 3, 4)
        s.update(size=10, x=2, y=3, id=4)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)
        s.update(size=5, x=1, y=2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 4)
        s.update(x=1, y=2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test3_update_square(self):
        """testing the update method with none int values"""
        s = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            s.update("2", 4, 5)
            s.update(True, 5, 5)
            s.update(2, 4, 4.78)
        with self.assertRaises(ValueError):
            s.update(0, 2, 4)
            s.update(-2, 6)
            s.update(6, -1)
            s.update(4, 6, -8)
