# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/27
File:   Medium 347. Top K Frequent Elements.py
"""
from typing import List

'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            if num in table:
                table[num] += 1
            else:
                table[num] = 1
        return list(map(lambda x: x[0], sorted(table.items(), key=lambda x: -x[1])[:k]))


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
