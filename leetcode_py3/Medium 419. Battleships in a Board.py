# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/5/9
File:   Medium 419. Battleships in a Board.py
"""
from typing import List

'''
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, 
empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of 
the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent 
battleships.

Example:
X..X
...X
...X
In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships will always have a cell 
separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
'''


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if (board[i][j] == "X" and (i == 0 or board[i - 1][j] == ".")
                        and (j == 0 or board[i][j - 1] == ".")):
                    ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countBattleships([["X", ".", ".", "X"], ["X", "X", "X", "X"], [".", ".", ".", "X"]]))
