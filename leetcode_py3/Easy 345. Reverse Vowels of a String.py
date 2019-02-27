# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/26
File:   Easy 345. Reverse Vowels of a String.py
"""
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        start = 0
        end = len(s) - 1
        chs = [ch for ch in s]
        while start <= end:
            if chs[start] in vowels and chs[end] in vowels:
                chs[start], chs[end] = chs[end], chs[start]
                start += 1
                end -= 1
            elif chs[start] not in vowels:
                start += 1
            else:
                end -= 1
        return "".join(chs)


if __name__ == '__main__':
    s = Solution()
    input_str = "leetcode"
    print(s.reverseVowels(input_str))
