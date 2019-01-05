# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Medium 63. Unique Paths II.py
"""
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [[0] * col] * row
        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0 and obstacleGrid[r][c] == 0:
                    dp[r][c] = 1
                elif obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                elif r == 0 and c > 0:
                    dp[r][c] = dp[r][c - 1]
                elif c == 0 and r > 0:
                    dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.uniquePathsWithObstacles([[1, 0]])
