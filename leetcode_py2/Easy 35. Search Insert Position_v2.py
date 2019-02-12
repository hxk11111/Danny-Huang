# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/28
File:   Easy 35. Search Insert Position_v2.py
"""
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end and start >= 0:
            middle = (start + end + 1) / 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                start = middle + 1
            else:
                end = middle - 1
        return start


if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1, 3, 5, 6], 5)
