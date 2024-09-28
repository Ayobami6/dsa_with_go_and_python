#!/usr/bin/python3

from typing import List

"""
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

needs: rows, cols, inner 3 X 3 sub matrix

[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

"""


def valid_sudoku(board: List[List[str]]) -> bool:
    # setup rows, cols, and sub matric
    rows: List[list] = [list() for _ in range(9)]
    cols: List[list] = [list() for _ in range(9)]
    sub_matrix: List[list] = [list() for _ in range(9)]

    # traverse the rows
    for i in range(9):
        # traverse cols
        for j in range(9):
            item = board[i][j]
            if item != ".":
                sub_index = (i // 3) * 3 + (j // 3)
                if item in rows[i] or item in cols[j] or item in sub_matrix[sub_index]:
                    return False
                rows[i].append(item)
                cols[j].append(item)
                sub_matrix[sub_index].append(item)
    return True
