# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Medium 74. Search a 2D Matrix.py
"""
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''


class Solution(object):
    def binary_search(self, line, target):
        start = 0
        end = len(line)
        while start <= end:
            mid = (start + end) / 2
            if line[mid] == target:
                return True
            if line[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for line in matrix:
            if not line:
                return False
            start = line[0]
            end = line[-1]
            if start <= target <= end:
                return self.binary_search(line, target)
        return False


if __name__ == '__main__':
    s = Solution()
    print s.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 0)
