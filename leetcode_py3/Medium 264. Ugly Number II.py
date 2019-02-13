# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/13
File:   Medium 264. Ugly Number II.py
"""
'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.
'''
import heapq


class Solution:
    def nthUglyNumber(self, n: 'int') -> 'int':
        heap = [1]
        visited = {1}
        s = None
        for i in range(n):
            s = heapq.heappop(heap)
            for elem in [2, 3, 5]:
                num = s * elem
                if num not in visited:
                    visited.add(num)
                    heapq.heappush(heap, num)
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))