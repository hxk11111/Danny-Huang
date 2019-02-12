# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/29
File:   Medium 215. Kth Largest Element in an Array.py
"""
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(start, end):
            if start == end:
                return start
            pivot = start
            nums[pivot], nums[end] = nums[end], nums[pivot]
            for i in range(start, end):
                if nums[i] < nums[end]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    pivot += 1
            nums[pivot], nums[end] = nums[end], nums[pivot]
            return pivot

        def select(start, end, least):
            if start == end:
                return nums[start]
            pivot_index = partition(start, end)
            if pivot_index == least:
                return nums[pivot_index]
            elif pivot_index < least:
                return select(pivot_index + 1, end, least)
            else:
                return select(start, pivot_index - 1, least)

        return select(0, len(nums) - 1, len(nums) - k)


if __name__ == '__main__':
    s = Solution()
    print s.findKthLargest([2, 1], k=2)
