# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/4/11
File:   Medium 647. Palindromic Substrings.py
"""
'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different 
substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Note:
The input string length won't exceed 1000.
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        cnt = 0
        dp = [[0 for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
            cnt += 1
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                if s[i] == s[j] and (dp[i + 1][j - 1] or i + 1 > j - 1):
                    dp[i][j] = 1
                    cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.countSubstrings("aaa"))
