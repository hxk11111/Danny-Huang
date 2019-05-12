# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Easy 66. Plus One.py
"""
'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ten = 0
        for i in range(len(digits))[::-1]:
            if i == len(digits) - 1:
                res = digits[i] + 1
                digits[i] = res % 10
                ten = res / 10
                if not ten:
                    break
            else:
                res = digits[i] + ten
                ten = res / 10
                digits[i] = res % 10
                if not ten:
                    break
        if ten:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([8, 9, 9, 9]))
