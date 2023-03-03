#!/usr/bin/env python3
import abc

import unittest

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z

class PointTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(2, 2, 2)
        self.p2 = Point(2, 2, 2)
        self.test = Point(2,2,2)
        
    def test_Equality(self):
        self.assertEqual(self.p1, self.p2)

    def test_FalseEquivalence(self):
        self.assertNotEqual(self.p1, (2, 2, 2))

if __name__ == "__main__":
    unittest.main()