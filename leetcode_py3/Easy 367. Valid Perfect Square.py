# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/2
File:   Easy 367. Valid Perfect Square.py
"""
'''
Given a positive integer num, write a function which returns True 
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0
        end = num
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                start = mid + 1
            else:
                end = mid - 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPerfectSquare(14))
