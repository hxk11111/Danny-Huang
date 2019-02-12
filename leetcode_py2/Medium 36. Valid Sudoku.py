# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/28
File:   Medium 36. Valid Sudoku.py
"""
'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    if self.valid_part(board, row, col):
                        continue
                    return False
        return True

    def valid_part(self, board, row, col):
        # Judge col direction
        for i in range(len(board)):
            if row != i and board[row][col] == board[i][col]:
                return False
        # Judge row direction
        for j in range(len(board[0])):
            if col != j and board[row][col] == board[row][j]:
                return False
        # Judge 3*3 part
        for i in range(3 * (row / 3), 3 * (row / 3 + 1)):
            for j in range(3 * (col / 3), 3 * (col / 3 + 1)):
                try:
                    if (row != i or col != j) and board[row][col] == board[i][j]:
                        return False
                except Exception as e:
                    print e
                    print row, col
                    print i, j
        return True


if __name__ == '__main__':
    s = Solution()
    print s.isValidSudoku([
        [".", ".", "5", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "8", ".", ".", ".", "3", "."],
        [".", "5", ".", ".", "2", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "9"],
        [".", ".", ".", ".", ".", ".", "4", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "7"],
        [".", "1", ".", ".", ".", ".", ".", ".", "."],
        ["2", "4", ".", ".", ".", ".", "9", ".", "."]
    ])
