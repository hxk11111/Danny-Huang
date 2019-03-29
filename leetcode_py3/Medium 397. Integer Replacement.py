# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/18
File:   Medium 397. Integer Replacement.py
"""
'''
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:
Input:
8
Output:
3
Explanation:
8 -> 4 -> 2 -> 1

Example 2:
Input:
7
Output:
4
Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
'''


class Solution:
    def integerReplacement(self, n: int) -> int:
        if n <= 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

    def integerReplacement2(self, n: int) -> int:
        demo = {1: 0}
        return self.recRep(n, demo)

    def recRep(self, n, memo):
        if n in memo:
            return memo[n]
        if n % 2 != 0:
            memo[n] = 1 + min(self.recRep(n + 1, memo), self.recRep(n - 1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recRep(n / 2, memo)
            return memo[n]


if __name__ == '__main__':
    s = Solution()
    print(s.integerReplacement2(7))
