# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/13
File:   Medium 120. Triangle.py
"""
'''
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        path_length = [triangle[0][0]]
        for r in range(1, len(triangle)):
            tmp = []
            for i in range(r + 1):
                if i == 0:
                    tmp.append(path_length[i] + triangle[r][i])
                elif 1 <= i < len(path_length):
                    tmp.append(min(path_length[i - 1], path_length[i]) + triangle[r][i])
                else:
                    tmp.append(path_length[i - 1] + triangle[r][i])
            path_length = tmp
        return min(path_length)


if __name__ == '__main__':
    s = Solution()
    print s.minimumTotal(
        [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]
    )
