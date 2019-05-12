# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/4/1
File:   Medium 424. Longest Repeating Character Replacement.py
"""
from collections import defaultdict

'''
Given a string that consists of only uppercase English letters, 
you can replace any letter in the string with another letter at most k times. 
Find the length of a longest substring containing all repeating letters you can 
get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:
Input:
s = "ABAB", k = 2
Output:
4
Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input:
s = "AABABBA", k = 1
Output:
4
Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        char2count = defaultdict(int)
        max_count = maxLen = 0
        start = 0
        for end in range(n):
            char2count[s[end]] += 1
            max_count = max(max_count, char2count[s[end]])
            while end - start + 1 - max_count > k:
                char2count[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, end - start + 1)
        return maxLen


if __name__ == '__main__':
    s = Solution()
    print(s.characterReplacement("ABABCCBB", 2))
