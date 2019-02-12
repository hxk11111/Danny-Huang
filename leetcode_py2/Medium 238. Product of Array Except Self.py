# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/11
File:   Medium 238. Product of Array Except Self.py
"""

'''
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
'''


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        mul = 1
        for i in range(len(nums)):
            result.append(mul)
            mul *= nums[i]

        mul = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] = result[j] * mul
            mul *= nums[j]

        return result


if __name__ == '__main__':
    s = Solution()
    print s.productExceptSelf([1, 2, 3, 4])
