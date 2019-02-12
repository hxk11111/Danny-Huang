# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/30
File:   Medium 220. Contains Duplicate III.py
"""
'''
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference 
between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        bucket = {}
        width = t + 1
        for i in range(len(nums)):
            if nums[i] / width in bucket:
                return True
            if nums[i] / width + 1 in bucket and abs(bucket[nums[i] / width + 1] - nums[i]) <= t:
                return True
            if nums[i] / width - 1 in bucket and abs(bucket[nums[i] / width - 1] - nums[i]) <= t:
                return True
            bucket[nums[i] / width] = nums[i]
            if i >= k:
                del bucket[nums[i - k] / width]
        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyAlmostDuplicate(nums=[-1, -1], k=1, t=-1)
