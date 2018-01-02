# -*- coding: utf-8 -*-
# @File  : 516. Longest Palindromic Subsequence.py
# @Author: Huang_xk
# @Date  : 12/29/17

'''
    Given a string s, find the longest palindromic subsequence's length in s.
    You may assume that the maximum length of s is 1000.

    Example 1:
    Input:
        "bbbab"
    Output:
        4

'''


# Self-writting: Brute Force
class Solution(object):
    def find_longest(self, str_p, start, end):
        if start == end:
            return 1
        elif start < end:
            if str_p[start] == str_p[end]:
                maxlen = 2 + self.find_longest(str_p, start + 1, end - 1)
            else:
                maxlen = max(self.find_longest(str_p, start + 1, end), self.find_longest(str_p, start, end - 1))
            return maxlen
        else:
            return 0

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        return self.find_longest(s, 0, length - 1)


# Self-writting: Dynamic Programming
class Solution_2(object):
    def find_longest(self, str_p, start, end, res_matrix):
        if res_matrix[start][end] != 0:
            return res_matrix[start][end]
        if start == end:
            return 1
        elif start < end:
            if str_p[start] == str_p[end]:
                res_matrix[start][end] = 2 + self.find_longest(str_p, start + 1, end - 1, res_matrix)
            else:
                res_matrix[start][end] = max(self.find_longest(str_p, start + 1, end, res_matrix),
                                             self.find_longest(str_p, start, end - 1, res_matrix))
            return res_matrix[start][end]
        else:
            return 0

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        res_matrix = [[0] * length for _ in range(length)]

        return self.find_longest(s, 0, length - 1, res_matrix)


# Solution:
class Solution_3(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if s == s[::-1]:
            return len(s)
        dp = [0] * length
        for i in range(length - 2, -1, -1):
            newdp = dp[:]
            # print i, dp
            newdp[i] = 1
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    # dp[i][j] = dp[i + 1][j - 1] + 2
                    newdp[j] = dp[j - 1] + 2
                else:
                    # dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    newdp[j] = max(dp[j], newdp[j - 1])
            # print newdp
            dp = newdp
        return dp[-1]
