# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/23
File:   Medium 334. Increasing Triplet Subsequence.py
"""
'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
'''


class Solution:
    def increasingTriplet(self, nums) -> bool:
        length = len(nums)
        if length <= 2:
            return False

        has_smallest = [False for _ in range(length)]
        smallest = nums[0]
        for i in range(1, length):
            if nums[i] > smallest:
                has_smallest[i] = True
            smallest = min(smallest, nums[i])

        biggest = nums[-1]
        for j in range(length - 1, -1, -1):
            if has_smallest[j] and nums[j] < biggest:
                return True
            biggest = max(biggest, nums[j])
        return False


    def increasingTriplet2(self, nums) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet([5, 4, 3, 2, 1]))
