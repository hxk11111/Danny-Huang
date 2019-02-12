# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/1
File:   Hard 42. Trapping Rain Water.py
"""
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_water = 0
        left = 0
        right = len(height) - 1
        step = 1
        while left < right:
            if height[left] <= height[right]:
                tmp_height = height[left]
                if height[left + step] >= tmp_height:
                    left = left + step
                    step = 1
                else:
                    total_water += tmp_height - height[left + step]
                    step += 1
            else:
                tmp_height = height[right]
                if height[right - step] >= tmp_height:
                    right = right - step
                    step = 1
                else:
                    total_water += tmp_height - height[right - step]
                    step += 1
        return total_water


if __name__ == '__main__':
    s = Solution()
    print s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
