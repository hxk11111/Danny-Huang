# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Easy 69. Sqrt(x)_v2.py
"""
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

if __name__ == '__main__':
    s = Solution()
    print s.mySqrt(5)
