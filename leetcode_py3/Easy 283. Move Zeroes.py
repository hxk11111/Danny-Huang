# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/13
File:   Easy 283. Move Zeroes.py
"""
'''
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for num in nums:
            if num != 0:
                nums[non_zero] = num
                non_zero += 1
        for i in range(non_zero, len(nums)):
            nums[i] = 0

    def moveZeros(self, nums: 'List[int]') -> 'None':
        non_zero = 0
        for ind, num in enumerate(nums):
            if num != 0:
                nums[ind], nums[non_zero] = nums[non_zero], nums[ind]
                non_zero += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    s.moveZeros(nums)
    print(nums)
