# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/27
File:   Medium 33. Search in Rotated Sorted Array_v2.py
"""
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (start + end + 1) / 2
            if nums[middle] == target:
                return middle
            if nums[middle] > nums[start]:  # means, from start to middle is ascending order
                if nums[start] <= target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if nums[middle] < target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print s.search([3, 1], 3)
