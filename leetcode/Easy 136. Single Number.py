# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/16
File:   Easy 136. Single Number.py
"""
'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber2(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a


if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([2, 2, 1])
    print s.singleNumber2([2, 2, 1])
