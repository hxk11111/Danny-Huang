# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/12
File:   Medium 279. Perfect Squares.py
"""
'''
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''


class Solution:
    def numSquares(self, n: 'int') -> 'int':
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(13))
