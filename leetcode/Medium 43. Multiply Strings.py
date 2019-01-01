# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/1
File:   Medium 43. Multiply Strings.py
"""
'''
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        pos = len(result) - 1
        for elem1 in num1[::-1]:
            tmp_pos = pos
            for elem2 in num2[::-1]:
                result[tmp_pos] += int(elem1) * int(elem2)
                result[tmp_pos - 1] += result[tmp_pos] / 10
                result[tmp_pos] = result[tmp_pos] % 10
                tmp_pos -= 1
            pos -= 1
        pt = 0
        while pt < len(result) and not result[pt]:
            pt += 1

        return "".join(map(str, result[pt:]))


if __name__ == '__main__':
    s = Solution()
    print s.multiply("123", "456")
