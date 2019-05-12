# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Medium 73. Set Matrix Zeroes.py
"""
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    for i in range(row):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "."
                    for j in range(col):
                        if matrix[r][j] != 0:
                            matrix[r][j] = "."

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == ".":
                    matrix[r][c] = 0


if __name__ == '__main__':
    s = Solution()
    l = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    s.setZeroes(l)
    print(l)
