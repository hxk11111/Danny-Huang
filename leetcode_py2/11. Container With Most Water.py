# -*- coding: utf-8 -*-
# @File  : 11. Container With Most Water.py
# @Author: Huang_xk
# @Date  : 1/2/18

'''
    Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.
'''


class Solution(object):

    # Brute Force(Self-writting)
    # def maxArea(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     max_area = 0
    #     for i in range(len(height) - 1):
    #         for j in range(i + 1, len(height)):
    #             area = min(height[i], height[j]) * (j - i)
    #             if area > max_area:
    #                 max_area = area
    #     return max_area


    # Self-writting after solution
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                area = height[left] * (right - left)
                if area > max_area:
                    max_area = area
                left += 1
            else:
                area = height[right] * (right - left)
                if area > max_area:
                    max_area = area
                right -= 1
        return max_area

