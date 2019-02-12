# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/25
File:   Medium 166. Fraction to Recurring Decimal.py
"""
'''
Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if numerator / denominator < 0:
            result += "-"
        if numerator % denominator == 0:
            return str(numerator / denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        result += str(numerator / denominator)
        result += "."
        numerator %= denominator
        table = {}
        i = len(result)
        while numerator != 0:
            if numerator not in table:
                table[numerator] = i
            else:
                result = result[:table[numerator]] + "(" + result[table[numerator]:i] + ")"
                return result
            result += str(numerator * 10 / denominator)
            numerator = numerator * 10 % denominator
            i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print s.fractionToDecimal(numerator=4, denominator=333)
