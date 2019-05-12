# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/6
File:   Medium 78. Subsets.py
"""
'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def dfs2(self, result, path, nums):
        result.append(path[:])
        for ind in range(len(nums)):
            path.append(nums[ind])
            self.dfs2(result, path, nums[ind + 1:])
            path.pop()

    def subsets2(self, nums):
        result = []
        self.dfs2(result, [], nums)
        return result

    def dfs(self, result, path, nums):
        result.append(path[:])
        for ind, num in enumerate(nums):
            path.append(num)
            self.dfs(result, path, nums[ind + 1:])
            path.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(result, [], nums)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.subsets2([1, 2, 3]))
