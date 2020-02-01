# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated 02/01/2020

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
@author: Xinyi Ye
"""

def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    The lengths of the triangle should >=0 and <= 200, and must be integers
    Then:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    if a < 0 or b < 0 or c < 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (b + a)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    elif (round(((a ** 2) + (b ** 2)), 2) == round((c ** 2), 2)) or (round(((b ** 2) + (c ** 2)), 2) == round((a ** 2), 2)) or(round(((a ** 2) + (c ** 2)), 2) == round((b ** 2), 2)):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'
