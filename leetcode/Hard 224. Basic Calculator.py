# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/31
File:   Hard 224. Basic Calculator.py
"""
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        total = 0
        sign = [1, 1]
        while i < len(s):
            if s[i].isdigit():
                start = i
                i += 1
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += sign.pop() * int(s[start: i])
                continue
            elif s[i] in "+-(":
                sign.append(sign[-1] * (1, -1)[s[i] == "-"])
            elif s[i] == ")":
                sign.pop()
            i += 1
        return total


if __name__ == '__main__':
    s = Solution()
    print s.calculate("2147483647")
