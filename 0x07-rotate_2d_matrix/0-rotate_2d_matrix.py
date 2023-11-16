#!/usr/bin/python3
"""
2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a n by n 2D matrix in place.
    """
    i = 0
    for v in list(zip(*matrix)):
        matrix[i][:] = v[::-1]
        i += 1
