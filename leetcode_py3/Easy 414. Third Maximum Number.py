# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/28
File:   Easy 414. Third Maximum Number.py
"""
from typing import List

'''
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = [-float("inf"), -float("inf"), -float("inf")]
        for num in nums:
            if num not in result:
                if num > result[0]:
                    result = [num, result[0], result[1]]
                elif num > result[1]:
                    result = [result[0], num, result[1]]
                elif num > result[2]:
                    result = [result[0], result[1], num]
        return result[-1] if -float("inf") not in result else max(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.thirdMax([2, 2, 3, 1]))
