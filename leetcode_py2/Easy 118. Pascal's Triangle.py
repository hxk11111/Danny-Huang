# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/12
File:   Easy 118. Pascal's Triangle.py
"""
'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        result = [[1]]
        for i in range(1, numRows):
            single_row = [1]
            for j in range(1, i):
                single_row.append(result[i - 1][j - 1] + result[i - 1][j])
            single_row.append(1)
            result.append(single_row)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
