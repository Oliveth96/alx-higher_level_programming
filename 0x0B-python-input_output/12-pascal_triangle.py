#!/usr/bin/python3
"""
Module that returns a list of lists of integers representing
the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """ Represents Pascal's Triangle of size n.

        Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        newTriangle = triangle[-1]
        temp = [1]
        for i in range(len(newTriangle) - 1):
            temp.append(newTriangle[i] + newTriangle[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
