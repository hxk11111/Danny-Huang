# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/10
File:   Medium 91. Decode Ways.py
"""
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        dp = [1] * (length + 1)
        if s[-1] == "0":
            dp[length - 1] = 0
        for i in range(length - 2, -1, -1):
            if s[i] == "0":
                if s[i - 1] > "2":
                    return 0
                else:
                    dp[i] = 0
            elif s[i] != "1" and s[i] != "2":
                dp[i] = dp[i + 1]
            elif s[i] == "1":
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                if s[i + 1] > "6":
                    dp[i] = dp[i + 1]
                else:
                    dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]

    def numDecodings2(self, s):
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * (length + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            elem = s[i - 1]
            if elem != "0":
                dp[i] += dp[i - 1]
            if i > 1 and s[i - 2:i] < "27" and s[i - 2:i] > "09":
                dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print s.numDecodings2("0")
