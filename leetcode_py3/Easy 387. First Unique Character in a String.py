# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/16
File:   Easy 387. First Unique Character in a String.py
"""
'''
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        f = len(s)
        for k, v in c.items():
            if v == 1:
                f = min(s.find(k), f)
        if f == len(s):
            return -1
        return f


if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("leetcode"))
