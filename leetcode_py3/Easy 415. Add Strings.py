# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/28
File:   Easy 415. Add Strings.py
"""
'''
Given two non-negative integers num1 and num2 represented as string, 
return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) >= len(num2):
            long = len(num1)
            short = len(num2)
            long_num = num1
        else:
            long = len(num2)
            short = len(num1)
            long_num = num2
        result = ""
        ten = 0
        for i in range(short):
            total = int(num1[-(i + 1)]) + int(num2[-(i + 1)]) + ten
            result = str(total % 10) + result
            ten = total // 10
        for j in range(long - short):
            total = int(long_num[:long - short][-(j + 1)]) + ten
            result = str(total % 10) + result
            ten = total // 10
        if ten:
            result = "1" + result
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.addStrings("9133", "0"))
