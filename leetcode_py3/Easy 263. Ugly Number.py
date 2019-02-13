# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/13
File:   Easy 263. Ugly Number.py
"""
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:
Input: 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2

Example 3:
Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.

Note:
1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
'''


class Solution:
    def isUgly(self, num: 'int') -> 'bool':
        if num < 1:
            return False
        while num > 1:
            flag = False
            for div in [2, 3, 5]:
                if num % div == 0:
                    num /= div
                    flag = True
            if not flag:
                return False
        return True

    def isUgly2(self, num: 'int') -> 'bool':
        for div in [2, 3, 5]:
            while num % div == 0 and num > 1:
                num /= div
        return num == 1


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly2(8))
