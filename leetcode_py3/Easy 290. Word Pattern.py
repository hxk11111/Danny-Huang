# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/14
File:   Easy 290. Word Pattern.py
"""
'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern 
and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated 
by a single space.
'''


class Solution:
    def wordPattern(self, pattern: 'str', str: 'str') -> 'bool':
        str_list = str.split(" ")
        table = dict()
        if len(pattern) != len(str_list):
            return False
        for ind, s in enumerate(str_list):
            if s in table:
                if table[s] != pattern[ind]:
                    return False
            else:
                if pattern[ind] in set(table.values()):
                    return False
                else:
                    table[s] = pattern[ind]
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern(pattern="abba", str="dog cat cat fish"))
