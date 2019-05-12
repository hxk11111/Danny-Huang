# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/20
File:   Medium 151. Reverse Words in a String.py
"""
'''
Given an input string, reverse the string word by word.

Example:  
Input: "the sky is blue",
Output: "blue is sky the".

Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, 
your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up: For C programmers, try to solve it in-place in O(1) space.
'''


class Solution(object):
    def reverse(self, word):
        return word[::-1]

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        s_reverse = []
        start = 0
        end = 0
        while end < len(s):
            if s[end] == " " and s[start: end].strip():
                word = self.reverse(s[start: end].strip())
                s_reverse.append(word)
                start = end + 1
            end += 1
        if start != end and s[start: end].strip():
            s_reverse.append(self.reverse(s[start: end].strip()))
        return self.reverse(" ".join(s_reverse)) if s_reverse else ""


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords(" 1"))
