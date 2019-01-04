# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/2
File:   Easy 53. Maximum Subarray.py
"""
'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        cur_sum = max_sum = nums[0]
        for ind, num in enumerate(nums[1:]):
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum


if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([-2])
