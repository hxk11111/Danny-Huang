# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/17
File:   Medium 395. Longest Substring with At Least K Repeating Characters.py
"""
'''
Find the length of the longest substring T of a given string 
(consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:
Input:
s = "aaabb", k = 3
Output:
3
The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input:
s = "ababbc", k = 2
Output:
5
The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k or k < 1:
            return 0
        for ch in set(s):
            if s.count(ch) < k:
                return max(self.longestSubstring(t, k) for t in s.split(ch))
        return len(s)


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring(s="ababbc", k=2))
