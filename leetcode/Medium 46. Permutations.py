# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/1
File:   Medium 46. Permutations.py
"""
'''
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permutation(self, result, nums, from_ind, to_ind):
        if from_ind == to_ind:
            result.append(nums[:])
            return
        for i in range(from_ind, to_ind):
                nums[i], nums[from_ind] = nums[from_ind], nums[i]
                self.permutation(result, nums, from_ind + 1, to_ind)
                nums[i], nums[from_ind] = nums[from_ind], nums[i]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permutation(result, nums, 0, len(nums))
        return result


if __name__ == '__main__':
    s = Solution()
    print s.permute([1, 2, 3])
