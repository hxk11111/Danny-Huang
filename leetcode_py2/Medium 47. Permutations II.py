# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/1
File:   Medium 47. Permutations II.py
"""
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def is_swap(self, nums, from_ind, i):
        elem = nums[i]
        for item in nums[from_ind:i]:
            if elem == item:
                return False
        return True

    def permutation(self, result, nums, from_ind):
        if from_ind == len(nums) - 1:
            result.append(nums[:])
            return
        for i in range(from_ind, len(nums)):
            if self.is_swap(nums, from_ind, i):
                nums[from_ind], nums[i] = nums[i], nums[from_ind]
                self.permutation(result, nums, from_ind + 1)
                nums[from_ind], nums[i] = nums[i], nums[from_ind]

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        self.permutation(result, nums, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.permuteUnique([2, 2, 1, 1])
