# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/21
File:   Easy 326. Power of Three.py
"""
'''
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
'''


class Solution:
    def isPowerOfThree(self, n: 'int') -> 'bool':
        if n <= 1:
            return False
        divider = 3
        while n > 1:
            if n % divider == 0:
                n //= divider
                divider *= divider
            else:
                divider = 3
                if n % divider == 0:
                    n //= divider
                    divider *= divider
                else:
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(9))
