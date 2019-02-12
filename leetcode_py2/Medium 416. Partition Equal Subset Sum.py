# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/13
File:   Medium 416. Partition Equal Subset Sum.py
"""
'''
Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

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


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        total_num = sum(nums)
        target = total_num / 2
        if total_num % 2 == 1:
            return False
        dp = [[False for _ in range(len(nums) + 1)] for _ in range(target + 1)]
        for i in range(len(nums) + 1):
            dp[0][i] = True
        for i in range(1, target + 1):
            for j in range(1, len(nums) + 1):
                dp[i][j] = dp[i][j - 1]
                if i >= nums[j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - nums[j - 1]][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.canPartition([1, 2, 3, 5, 1, 10])
