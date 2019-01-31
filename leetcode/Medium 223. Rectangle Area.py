# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/31
File:   Medium 223. Rectangle Area.py
"""
'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
'''


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left_top = (max(A, E), min(D, H))
        right_bottom = (min(C, G), max(B, F))

        width = right_bottom[0] - left_top[0]
        height = left_top[1] - right_bottom[1]
        if width < 0 or height < 0:
            area = 0
        else:
            area = width * height

        total_area = (C - A) * (D - B) + (G - E) * (H - F) - area
        return total_area


if __name__ == '__main__':
    s = Solution()
    print s.computeArea(A=-3, B=0, C=3, D=4, E=0, F=-1, G=9, H=2)
    print s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4)
