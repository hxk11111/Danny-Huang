# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/28
File:   Medium 209. Minimum Size Subarray Sum.py
"""
'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, 
return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time 
complexity is O(n log n). 
'''


class Solution(object):
    def minSubArrayLen3(self, s, nums):
        left = 0
        right = 0
        total = 0
        length = len(nums) + 1
        while right < len(nums):
            if total < s:
                total += nums[right]
            while total >= s:
                length = min(length, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        if length == len(nums) + 1:
            return 0
        return length

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return -1
        end = 0
        length = len(nums) + 1
        total = 0
        for i in range(len(nums)):
            while end < len(nums) and total < s:
                total += nums[end]
                end += 1
            if total >= s:
                length = min(length, end - i)

            total = total - nums[i]
        if length == len(nums) + 1:
            return 0
        return length

    def minSubArrayLen2(self, s, nums):
        if nums is None:
            return -1
        left = 0
        length = len(nums) + 1
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                length = min(length, i - left + 1)
                total -= nums[left]
                left += 1
        if length == len(nums) + 1:
            return 0
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen3(s=7, nums=[2, 3, 1, 2, 4, 3]))
