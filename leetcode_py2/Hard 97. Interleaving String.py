# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/11
File:   Hard 97. Interleaving String.py
"""
'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if ((i - 1 >= 0 and s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (
                        j - 1 >= 0 and s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])):
                    dp[i][j] = True
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
