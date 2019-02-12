# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/31
File:   Medium 227. Basic Calculator II.py
"""
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.

Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5

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
        length = len(s)
        i = 0
        queue = []
        sign = "+"
        while i < length:
            if s[i].isdigit():
                start = i
                i += 1
                while i < length and s[i].isdigit():
                    i += 1
                if sign == "+":
                    queue.append(int(s[start:i]))
                elif sign == "-":
                    queue.append(-int(s[start:i]))
                elif sign == "*":
                    queue.append(queue.pop() * int(s[start:i]))
                else:
                    num = queue.pop()
                    if num / int(s[start:i]) < 0 and num % int(s[start:i]) != 0:
                        queue.append(num / int(s[start:i]) + 1)
                    else:
                        queue.append(num / int(s[start:i]))
            elif s[i].isspace():
                i += 1
            else:
                sign = s[i]
                i += 1
        return sum(queue)


if __name__ == '__main__':
    s = Solution()
    print s.calculate("-3/2")
