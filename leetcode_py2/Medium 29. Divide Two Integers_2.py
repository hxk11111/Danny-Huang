# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111(hxk11111@baidu.com)
Date:	2018/12/26
File:   Medium 29. Divide Two Integers_2.py
"""
'''
    Divide two integers without using multiplication, division and mod operator.

    If it is overflow, return MAX_INT.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            i, tmp = 1, divisor
            while dividend >= tmp:
                res += i
                dividend -= tmp
                i <<= 1
                tmp <<= 1
        if not flag:
            res = -res
        return min(max(-2 ** 31, res), 2 ** 31 - 1)


if __name__ == '__main__':
    s = Solution()
    print s.divide(10, -10)
