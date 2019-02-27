# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/25
File:   Easy 342. Power of Four.py
"""
'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
Input: 16
Output: true

Example 2:
Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        mul = 4
        while num >= 4:
            if num % mul == 0:
                num //= mul
                mul *= mul
            else:
                mul = 4
                if num % mul == 0:
                    num //= mul
                    mul *= mul
                else:
                    return False
        if num == 1:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(5))
