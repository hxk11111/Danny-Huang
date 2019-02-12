# -*- coding: utf-8 -*-
# @File  : 42. Trapping Rain Water.py
# @Author: Huang_xk
# @Date  : 1/2/18


'''
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it is able to trap after raining.

    For example,
        Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
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
        if len(height) == 1:
            return 0

        step = 1
        while left < right:
            if height[left] <= height[right]:
                temp = height[left]
                next_to_temp = height[left + step]
                if next_to_temp >= temp:
                    left += step
                    step = 1
                else:
                    total_water = total_water + temp - next_to_temp
                    step += 1

            else:
                temp = height[right]
                next_to_temp = height[right - step]
                if next_to_temp >= temp:
                    right -= step
                    step = 1
                else:
                    total_water = total_water + temp - next_to_temp
                    step += 1
        return total_water


s = Solution()
print s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
