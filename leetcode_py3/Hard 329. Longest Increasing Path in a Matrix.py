# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/22
File:   Hard 329. Longest Increasing Path in a Matrix.py
"""
'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        sequence = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sequence.append((matrix[i][j], i, j))
        sequence.sort()

        check = {}
        for h, x, y in sequence:
            cur_pos = (x, y)
            if cur_pos not in check:
                check[cur_pos] = 1
            cur_path = 0
            for dx, dy in DIRECTIONS:
                if self.is_valid(x + dx, y + dy, matrix, h):
                    cur_path = max(cur_path, check[(x + dx, y + dy)])
            check[cur_pos] += cur_path

        vals = check.values()
        return max(vals)

    def is_valid(self, x, y, matrix, h):
        row, col = len(matrix), len(matrix[0])
        return x >= 0 and x < row and y >= 0 and y < col and matrix[x][y] < h


if __name__ == '__main__':
    s = Solution()
    print(s.longestIncreasingPath(
        [
            [3, 4, 5],
            [3, 2, 6],
            [2, 2, 1]
        ]))
