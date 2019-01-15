# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/15
File:   Medium 130. Surrounded Regions.py
"""
'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board 
are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the 
border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally 
or vertically.
'''


class Solution(object):
    def could_continue(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != "O":
            return False
        return True

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        stack = []
        for i in range(rows):
            if board[i][0] == "O":
                stack.append((i, 0))
                board[i][0] = "."
            if board[i][cols - 1] == "O":
                stack.append((i, cols - 1))
                board[i][cols - 1] = "."

        for j in range(1, cols - 1):
            if board[0][j] == "O":
                stack.append((0, j))
                board[0][j] = "."
            if board[rows - 1][j] == "O":
                stack.append((rows - 1, j))
                board[rows - 1][j] = "."

        while stack:
            i, j = stack.pop()
            points = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
            for x, y in points:
                if self.could_continue(board, x, y):
                    stack.append((x, y))
                    board[x][y] = "."

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"


if __name__ == '__main__':
    s = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s.solve(board)
    print board
