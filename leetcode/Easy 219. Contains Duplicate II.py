# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/30
File:   Easy 219. Contains Duplicate II.py
"""
'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j 
in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        min_interval = dict()
        table = dict()
        for ind, num in enumerate(nums):
            if num not in table:
                table[num] = ind
            else:
                if num in min_interval:
                    min_interval[num] = min(ind - table[num], min_interval[num])
                else:
                    min_interval[num] = ind - table[num]
                table[num] = ind

        if not min_interval:
            return False
        for elem in min_interval.values():
            if elem > k:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
