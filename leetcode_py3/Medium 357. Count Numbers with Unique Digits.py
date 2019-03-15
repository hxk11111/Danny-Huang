# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/28
File:   Medium 357. Count Numbers with Unique Digits.py
"""
'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
'''


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        dp = [1 for _ in range(n + 1)]
        dp[1] = 9
        total = 10
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (11 - i)
            total += dp[i]
        return total
