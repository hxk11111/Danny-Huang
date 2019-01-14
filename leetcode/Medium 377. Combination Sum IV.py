# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/14
File:   Medium 377. Combination Sum IV.py
"""
'''
Given an integer array with all positive numbers and no duplicates, 
find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        dp = [0 for _ in range(target + 1)]
        for i in range(length + 1):
            dp[0] = 1
        for i in range(1, target + 1):
            for j in range(1, length + 1):
                if nums[j - 1] <= i:
                    dp[i] += dp[i - nums[j - 1]]

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum4(nums=[1, 2, 3, 5], target=10)
