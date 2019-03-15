# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/27
File:   Easy 349. Intersection of Two Arrays.py
"""
from typing import List

'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.
'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        for num in nums1:
            if num in nums2 and num not in intersect:
                intersect.append(num)
        return intersect