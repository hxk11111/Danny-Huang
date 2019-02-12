# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/30
File:   Hard 41. First Missing Positive.py
"""
'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1
'''


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 1
        nums = sorted(nums)
        last_pos = -1
        for ind, num in enumerate(nums):
            if num > 0:
                if last_pos >= 0:
                    residual = num - nums[last_pos]
                    if residual > 1:
                        return nums[last_pos] + 1
                    else:
                        last_pos = ind
                else:
                    if num > 1:
                        return 1
                    else:
                        last_pos = ind
        return nums[-1] + 1


if __name__ == '__main__':
    s = Solution()
    print s.firstMissingPositive([4])
