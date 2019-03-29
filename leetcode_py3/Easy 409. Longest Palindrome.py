# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/23
File:   Easy 409. Longest Palindrome.py
"""
import collections

'''
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        max_length = 0
        for _, cnt in counter.items():
            max_length += cnt // 2 * 2
            if max_length % 2 == 0 and cnt % 2 != 0:
                max_length += 1
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("bananas"))
