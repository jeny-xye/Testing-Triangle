# -*- coding: utf-8 -*-
"""
Updated 02/01/2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Xinyi Ye
"""

import unittest
from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # Equilateral testing
    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')
    
    def testEquilateralTrianglesB(self):   
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')

    def testEquiateralTrianglesC(self):
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral')

    # Right testing
    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 3, 5), 'Right')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right')

    def testRightTriangleE(self):
        self.assertEqual(classifyTriangle(5, 4, 3), 'Right')

    def testRightTriangleF(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    # Isosceles testing
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isosceles')

    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isosceles')

    # Scalene testing
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(2, 4, 3), 'Scalene')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(4, 3, 2), 'Scalene')

    def testScaleneTriangleD(self):
        self.assertEqual(classifyTriangle(4, 2, 3), 'Scalene')

    def testScaleneTriangleE(self):
        self.assertEqual(classifyTriangle(3, 2, 4), 'Scalene')

    def testScaleneTriangleF(self):
        self.assertEqual(classifyTriangle(3, 4, 2), 'Scalene')

    # NotATriangle testing
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 5), 'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(2, 5, 2), 'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(5, 2, 2), 'NotATriangle')

    def testNotATriangleD(self):
        self.assertEqual(classifyTriangle(5, 10, 15), 'NotATriangle')

    def testNotATriangleE(self):
        self.assertEqual(classifyTriangle(5, 15, 10), 'NotATriangle')

    def testNotATriangleF(self):
        self.assertEqual(classifyTriangle(10, 5, 15), 'NotATriangle')

    def testNotATriangleG(self):
        self.assertEqual(classifyTriangle(10, 15, 5), 'NotATriangle')

    def testNotATriangleH(self):
        self.assertEqual(classifyTriangle(15, 5, 10), 'NotATriangle')

    def testNotATriangleI(self):
        self.assertEqual(classifyTriangle(15, 10, 5), 'NotATriangle')

    def testNotATriangleJ(self):
        self.assertEqual(classifyTriangle(15, 10, 0), 'NotATriangle')


    # InvalidInput testing
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1, -3, -4), 'InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-1, -4, -3), 'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(-4, -1, -3), 'InvalidInput')

    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(-4, -3, -1), 'InvalidInput')

    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle(-3, -1, -4), 'InvalidInput')

    def testInvalidInputF(self):
        self.assertEqual(classifyTriangle(-3, -4, -1), 'InvalidInput')
    
    def testInvalidInputG(self):
        self.assertEqual(classifyTriangle('l', 3, 4), 'InvalidInput')

    def testInvalidInputH(self):
        self.assertEqual(classifyTriangle('l', 4, 3), 'InvalidInput')

    def testInvalidInputI(self):
        self.assertEqual(classifyTriangle('?', 3, 4), 'InvalidInput')

    def testInvalidInputJ(self):
        self.assertEqual(classifyTriangle(' ', 3, 4), 'InvalidInput')

    def testInvalidInputK(self):
        self.assertEqual(classifyTriangle('', 3, 4), 'InvalidInput')

    def testInvalidInputL(self):
        self.assertEqual(classifyTriangle(201, 9, 9), 'InvalidInput')

    def testInvalidInputM(self):
        self.assertEqual(classifyTriangle(3.03, 4, 5), 'InvalidInput')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
