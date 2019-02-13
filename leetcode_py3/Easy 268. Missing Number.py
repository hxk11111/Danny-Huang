# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/13
File:   Easy 268. Missing Number.py
"""
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant extra space complexity?
'''


class Solution:
    def missingNumber(self, nums: 'List[int]') -> 'int':
        s = set(nums)
        length = len(nums) + 1
        for num in range(length):
            if num not in s:
                return num


if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
