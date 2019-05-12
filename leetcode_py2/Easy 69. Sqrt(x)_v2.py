# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Easy 69. Sqrt(x)_v2.py
"""
import math

'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''


class Solution(object):
    def mySqrt4(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp = x / 2
        while abs(tmp * tmp - x) > 0.0001:
            tmp = (tmp + x / tmp) / 2
        return tmp

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x
        ans = 0
        if x <= 1:
            return x
        while start <= end:
            mid = (start + end) / 2
            if mid * mid == x:
                return mid
            if mid <= x / mid:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans

    def mySqrt2(self, x):
        start = 0
        end = x
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
                ans = mid
            else:
                end = mid - 1
        return ans

    def mySqrt3(self, x):
        y = x * 1.0 / 2
        while abs(y * y - x) > 0.00001:
            y = (1.0 * y + 1.0 * x / y) / 2
            print(y, math.sqrt(x))
        return y


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt3(87))
    print(s.mySqrt4(87))
    print(math.sqrt(87))
