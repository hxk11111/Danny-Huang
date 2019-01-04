# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/2
File:   Medium 50. Pow(x, n).py
"""
'''
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000

Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        neg_flag = True if n < 0 else False
        n = abs(n)
        final_result = 1
        multiplier = x
        mul = 1
        while n > 0:
            if n >= mul:
                final_result *= multiplier
                multiplier *= multiplier
                n -= mul
                mul *= 2
            else:
                mul = 1
                multiplier = x

        if neg_flag:
            final_result = 1 / final_result
        return final_result


if __name__ == '__main__':
    s = Solution()
    print s.myPow(2.10000, 3)
