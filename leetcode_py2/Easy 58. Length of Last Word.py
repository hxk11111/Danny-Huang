# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/4
File:   Easy 58. Length of Last Word.py
"""
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in range(len(s))[::-1]:
            if s[i] != " ":
                length += 1
            elif s[i] == " " and length:
                return length
            else:
                length = 0
        return length


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLastWord("a ")

