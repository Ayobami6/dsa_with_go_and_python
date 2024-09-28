#!/usr/bin/python3
from typing import List
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Requires:
    - nested loops
    - traverse and swap the col position of elements in the rows except the first
    - after traversal and swap, reverse each rows in the matrix
    """

    mat_len = len(matrix)
    for i in range(mat_len):
        for j in range(i, mat_len):
            # swap
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(rotate_matrix(matrix))
