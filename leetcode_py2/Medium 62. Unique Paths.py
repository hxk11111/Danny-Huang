# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Medium 62. Unique Paths.py
"""
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''


class Solution(object):
    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0, n):
            dp[0][i] = 1
        for j in range(1, m):
            dp[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n] * m
        row = 0
        col = 0
        while row < m:
            while col < n:
                if row >= 1:
                    if col >= 1:
                        dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
                    else:
                        dp[row][col] = dp[row - 1][col]
                col += 1
            row += 1
            col = 0
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(1, 1))
    print(s.uniquePaths2(1, 1))
    print(s.uniquePaths2(7, 3))
