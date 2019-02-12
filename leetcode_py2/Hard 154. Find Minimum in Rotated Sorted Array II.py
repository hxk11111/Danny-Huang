# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/21
File:   Hard 154. Find Minimum in Rotated Sorted Array II.py
"""
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        while start <= end:
            while start + 1 <= end and nums[start] == nums[start + 1]:
                start += 1

            while end - 1 >= start and nums[end] == nums[end - 1]:
                end -= 1

            mid = (start + end) / 2
            if mid + 1 <= end and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid - 1 >= start and nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return nums[start]


if __name__ == '__main__':
    s = Solution()
    print s.findMin([3, 3])
