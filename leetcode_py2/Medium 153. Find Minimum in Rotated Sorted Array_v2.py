# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/21
File:   Medium 153. Find Minimum in Rotated Sorted Array_v2.py
"""
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2] 
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]    [6,7,0,1,2,4,5]
Output: 0
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] > nums[start] and nums[mid] > nums[end]:
                start = mid + 1
            elif nums[start] < nums[mid] < nums[end]:
                return nums[start]
            elif nums[end] < nums[mid] < nums[start]:
                return nums[end]
            elif nums[mid] < nums[start] and nums[mid] < nums[end]:
                end = mid
            else:
                return min(nums[start], nums[end])
        return nums[start]


if __name__ == '__main__':
    s = Solution()
    print s.findMin([0, 1])
