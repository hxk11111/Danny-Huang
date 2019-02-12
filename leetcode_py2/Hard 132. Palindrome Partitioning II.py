# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/15
File:   Hard 132. Palindrome Partitioning II.py
"""
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [length - 1 - i for i in range(length)]
        flag_dp = [[False for _ in range(length)] for _ in range(length)]

        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                if s[i] == s[j] and (j - i < 2 or flag_dp[i + 1][j - 1]):
                    flag_dp[i][j] = True
                    if j == length - 1:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j + 1] + 1)
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print s.minCut("aabaa")
