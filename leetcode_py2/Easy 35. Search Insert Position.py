# -*- coding: utf-8 -*-
# @Time    : 07/01/2018 12:04 AM
# @Author  : Huang_xk
# @FileName: Easy 35. Search Insert Position.py
"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            middle = (end + start) / 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        if nums[start] < target:
            return start + 1
        else:
            return start


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 2))
