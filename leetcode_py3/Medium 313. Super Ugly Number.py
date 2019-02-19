# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/19
File:   Medium 313. Super Ugly Number.py
"""
'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:
Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
             
Note:
1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: 'int', primes: 'List[int]') -> 'int':
        if n == 1:
            return 1
        heap = [1]
        visited = {1}
        num = None
        for i in range(n):
            num = heapq.heappop(heap)
            for prime in primes:
                res = num * prime
                if res not in visited:
                    visited.add(res)
                    heapq.heappush(heap, res)
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.nthSuperUglyNumber(n=15, primes=[3, 5, 7, 11, 19, 23, 29, 41, 43, 47]))
