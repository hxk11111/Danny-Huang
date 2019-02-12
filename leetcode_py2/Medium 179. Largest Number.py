# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/26
File:   Medium 179. Largest Number.py
"""
'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''


class Solution(object):
    def compare_func(self, x, y):
        if x + y > y + x:
            return -1
        else:
            return 1

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_nums = map(str, nums)
        str_nums = sorted(str_nums, cmp=self.compare_func)
        return "".join(str_nums) if str_nums[0] != "0" else "0"


if __name__ == '__main__':
    s = Solution()
    print s.largestNumber([10, 2])
