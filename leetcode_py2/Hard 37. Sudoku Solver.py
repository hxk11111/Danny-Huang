# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111(hxk11111@baidu.com)
Date:	2018/12/29
File:   Hard 37. Sudoku Solver.py
"""
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
'''


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)

    def dfs(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    for i in range(1, 10):
                        board[row][col] = str(i)
                        if self.is_valid(board, row, col) and self.dfs(board):
                            return True
                        board[row][col] = "."
                    return False
        return True

    def is_valid(self, board, row, col):
        # Judge col direction
        for i in range(len(board)):
            if row != i and board[i][col] == board[row][col]:
                return False
        # Judge row direction
        for j in range(len(board[0])):
            if col != j and board[row][j] == board[row][col]:
                return False
        # Judge 3*3 part
        for i in range(3 * (row / 3), 3 * (row / 3 + 1)):
            for j in range(3 * (col / 3), 3 * (col / 3 + 1)):
                if (row != i or col != j) and (board[row][col] == board[i][j]):
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    l = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(l)
    print l
