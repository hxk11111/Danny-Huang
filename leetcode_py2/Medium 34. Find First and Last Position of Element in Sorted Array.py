# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/28
File:   Medium 34. Find First and Last Position of Element in Sorted Array.py
"""
'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        while start <= end and start >= 0:
            middle = (start + end + 1) / 2
            if nums[middle] == target:
                from_ind = middle
                to_ind = middle
                while from_ind >= 1 and nums[from_ind - 1] == nums[middle]:
                    from_ind -= 1
                while to_ind < len(nums) - 1 and nums[to_ind + 1] == nums[to_ind]:
                    to_ind += 1
                return [from_ind, to_ind]
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print s.searchRange([2, 2], 6)
