# -*- coding: utf-8 -*-
# @File  : 91. Decode Ways.py
# @Author: Huang_xk
# @Date  : 1/3/18

'''
    A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Given an encoded message containing digits, determine the total number of ways to decode it.

    For example,
        Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
        The number of ways decoding "12" is 2.
'''


# Self-wrtting
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


# Solution
class Solution2(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        count = [0] * (len(s) + 1)
        count[0] = 1
        count[1] = 1
        for i in xrange(2, len(s) + 1):
            if s[i - 1] > '0':
                count[i] = count[i - 1]
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7'):
                count[i] += count[i - 2]
        return count[len(s)]


s = Solution()
print s.numDecodings("22136")
