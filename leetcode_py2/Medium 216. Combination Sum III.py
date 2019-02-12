# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/30
File:   Medium 216. Combination Sum III.py
"""
'''
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution(object):
    def k_sum(self, result, path, k, start, target):
        if target == 0:
            result.append(path[:])
            return

        if k == 0 and target != 0:
            return

        for num in range(start, 10):
            if target >= num * k:
                path.append(num)
                self.k_sum(result, path, k - 1, num + 1, target - num)
                path.pop()
            else:
                break

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.k_sum(result, [], k, 1, n)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(k=3, n=9)
