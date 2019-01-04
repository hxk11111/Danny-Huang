# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/2
File:   Medium 54. Spiral Matrix.py
"""
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        total_row = len(matrix)
        total_col = len(matrix[0])
        visit_flag = [[False] * total_col for _ in range(total_row)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(total_row * total_col):
            result.append(matrix[r][c])
            visit_flag[r][c] = True
            rr, cc = r + dr[di], c + dc[di]
            if 0 <= rr < total_row and 0 <= cc < total_col and not visit_flag[rr][cc]:
                r, c = rr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return result


if __name__ == '__main__':
    s = Solution()
    print s.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
