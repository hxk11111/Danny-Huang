# -*- coding: utf-8 -*-
# @File  : 214. Shortest Palindrome.py
# @Author: Huang_xk
# @Date  : 12/28/17

'''
    Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

    For example:

    Given "aacecaaa", return "aaacecaaa".

    Given "abcd", return "dcbabcd".
'''


# Self writted， timeout error
class Solution(object):
    # Firstly, we need to find the longest palindrome substring in this given string
    def longestPalindrome(self, str_p):
        length = len(str_p)
        longest = 1
        # If the length of the longest palindrome is odd
        for i in range(1, length):
            low = i - 1
            high = i + 1
            while low >= 0 and high <= length - 1 and str_p[low] == str_p[high]:
                low -= 1
                high += 1
            if low + 1 == 0 and high - low - 1 > longest:
                longest = high - low - 1

        # If the length of the longest palindrome is even
        for i in range(1, length):
            low = i - 1
            high = i
            while low >= 0 and high <= length - 1 and str_p[low] == str_p[high]:
                low -= 1
                high += 1
            if low + 1 == 0 and high - low - 1 > longest:
                longest = high - low - 1

        return longest

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(set(s)) == 1:
            return s
        longest = self.longestPalindrome(s)
        length = len(s)
        if longest == length:
            return s
        else:
            residual = length - longest
            added = ""
            for i in range(length - 1, length - residual - 1, -1):
                added += s[i]
            return added + s

        # todo: 错误 待修改