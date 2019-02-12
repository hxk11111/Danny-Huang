# -*- coding: utf-8 -*-
# @File  : 5. Longest Palindromic Substring.py
# @Author: Huang_xk
# @Date  : 12/27/17


'''
    Problem:
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        longest = 0
        start = 0
        if length == 1:
            return s

        # if the length of longest Palindrome string is odd
        for i in range(1, length):
            low = i - 1
            high = i + 1
            while low >= 0 and high <= length - 1 and s[low] == s[high]:
                low -= 1
                high += 1
            if high - low - 1 > longest:
                longest = high - low - 1
                start = low + 1

        # if the length of longest Palindrome string is even
        for i in range(1, length):
            low = i - 1
            high = i
            while low >= 0 and high <= length - 1 and s[low] == s[high]:
                low -= 1
                high += 1
            if high - low - 1 > longest:
                longest = high - low - 1
                start = low + 1
        return s[start:start + longest]