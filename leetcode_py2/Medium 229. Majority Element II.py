# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/1
File:   Medium 229. Majority Element II.py
"""
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        length = len(nums)
        times = length / 3
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        result = []
        for k, v in table.items():
            if v > times:
                result.append(k)
        return result

    def majorityElement2(self, nums):
        if not nums:
            return []
        candidate1 = count1 = count2 = 0
        candidate2 = 1
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement2([0, 0, 0])
