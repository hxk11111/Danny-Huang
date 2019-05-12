# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/20
File:   Medium 152. Maximum Product Subarray.py
"""
'''
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        max_result = largest = least = nums[0]
        for num in nums[1:]:
            largest, least = max(largest * num, least * num, num), min(largest * num, least * num,
                                                                       num)
            max_result = max(max_result, largest)
        return max_result


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([0, 2]))
