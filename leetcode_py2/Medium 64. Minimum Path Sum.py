# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Medium 64. Minimum Path Sum.py
"""
'''
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7

Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        dp = grid[:]
        for r in range(row):
            for c in range(col):
                if r == 0 and c == 0:
                    continue
                elif r == 0 and c > 0:
                    dp[r][c] = dp[r][c] + dp[r][c - 1]
                elif c == 0 and r > 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c]
                else:
                    dp[r][c] = min(dp[r][c] + dp[r][c - 1], dp[r - 1][c] + dp[r][c])
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ])
