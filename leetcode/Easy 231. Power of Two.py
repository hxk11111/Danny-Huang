# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/1
File:   Easy 231. Power of Two.py
"""
'''
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 2^0 = 1

Example 2:
Input: 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: 218
Output: false
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        mul = 2
        while n >= 2:
            if n / mul > 0 and n % 2 != 0:
                return False
            elif n / mul > 0 and n % mul == 0:
                n /= mul
                mul *= mul
            else:
                mul = 2
        return True

if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfTwo(12)

