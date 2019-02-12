# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/12
File:   Easy 242. Valid Anagram.py
"""
'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.


Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


class Solution:
    def isAnagram(self, s: 'str', t: 'str') -> 'bool':
        c_dict1 = {}
        for ch in s:
            if ch in c_dict1:
                c_dict1[ch] += 1
            else:
                c_dict1[ch] = 1
        c_dict2 = {}
        for ch in t:
            if ch in c_dict2:
                c_dict2[ch] += 1
            else:
                c_dict2[ch] = 1
        if len(c_dict1) != len(c_dict2):
            return False
        else:
            for k, v in c_dict1.items():
                if k in c_dict2 and v == c_dict2[k]:
                    continue
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram(s="anagram", t="nagaram"))
