# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/28
File:   Medium 416. Partition Equal Subset Sum.py
"""
from typing import List

'''
Given a non-empty array containing only positive integers, find if the array can be 
partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
 
Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        dp = [[False] * (half + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        for i in range(1, len(nums)):
            for j in range(1, half + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))
