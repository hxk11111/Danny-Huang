# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/9
File:   Medium 90. Subsets II.py
"""
'''
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = [[]]
        ind = 0
        while ind < len(nums):
            num = nums[ind]
            same_ind = ind
            while same_ind + 1 < len(nums) and nums[same_ind + 1] == num:
                same_ind += 1
            one_pass_result = []
            for end in range(ind, same_ind + 1):
                item = nums[ind:end + 1]
                one_pass_result.extend([elem + item for elem in result])
            result.extend(one_pass_result)
            ind = same_ind + 1
        return result


if __name__ == '__main__':
    s = Solution()
    print s.subsetsWithDup([1])
