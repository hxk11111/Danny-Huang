# -*- coding: utf-8 -*-
# @File  : 1. Two Sum.py
# @Author: Huang_xk
# @Date  : 12/25/17

'''
Problem:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            residue = target - nums[i]
            for j in range(i + 1, len(nums)):
                if residue == nums[j]:
                    return (i, j)



# After review solution
class Solution2(object):
    def twoSum(self, nums, target):
        res_dict = {}
        for i in range(len(nums)):
            residue = target - nums[i]
            if res_dict.has_key(residue):
                return (res_dict[residue], i)
            else:
                res_dict[nums[i]] = i