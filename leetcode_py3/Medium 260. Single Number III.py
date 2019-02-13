# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/13
File:   Medium 260. Single Number III.py
"""
'''
Given an array of numbers nums, in which exactly two elements appear only once and 
all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''


class Solution:
    def singleNumber(self, nums: 'List[int]') -> 'List[int]':
        result = set()
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)
        return list(result)


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 1, 3, 2, 5]))
