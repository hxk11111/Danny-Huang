# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/17
File:   Medium 394. Decode String.py
"""
'''
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets 
are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits 
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''


class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        word_stack = []
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                if num > 0:
                    num_stack.append(num)
                    num = 0
                if ch == "]":
                    chars = []
                    single_char = word_stack.pop()
                    while single_char != "[":
                        chars.append(single_char)
                        single_char = word_stack.pop()
                    word_stack.append("".join(chars[::-1]) * num_stack.pop())
                else:
                    word_stack.append(ch)
        return "".join(word_stack)


if __name__ == '__main__':
    s = Solution()
    print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
