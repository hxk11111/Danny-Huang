# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/13
File:   Easy 119. Pascal's Triangle II.py
"""
'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1, rowIndex + 1):
            row = [1] + [row[j - 1] + row[j] for j in range(1, i)] + [1]
        return row


if __name__ == '__main__':
    s = Solution()
    print s.getRow(3)
