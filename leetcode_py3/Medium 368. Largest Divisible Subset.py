# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/2
File:   Medium 368. Largest Divisible Subset.py
"""
from typing import List

'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) 
of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]
'''


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        length = len(nums)
        dp = [1] * length
        father = [-1] * length
        max_length, ind = 0, -1

        nums = sorted(nums)
        for i in range(length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        father[i] = j
            if dp[i] > max_length:
                max_length = dp[i]
                ind = i

        result = []
        for elem in range(max_length):
            result.append(nums[ind])
            ind = father[ind]

        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.largestDivisibleSubset([3, 4, 16, 8]))
