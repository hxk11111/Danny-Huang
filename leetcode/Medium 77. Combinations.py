# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/6
File:   Medium 77. Combinations.py
"""
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution(object):
    def combine_k_nums(self, result, path, nums, k):
        if k == 2:
            for ind, num1 in enumerate(nums[:-1]):
                for num2 in nums[ind + 1:]:
                    result.append(path + [num1, num2])
        else:
            for ind, num1 in enumerate(nums[:-(k - 1)]):
                path.append(num1)
                self.combine_k_nums(result, path, nums[ind + 1:], k - 1)
                path.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[elem + 1] for elem in range(n)]
        else:
            result = []
            self.combine_k_nums(result, [], [elem + 1 for elem in range(n)], k)
            return result


if __name__ == '__main__':
    s = Solution()
    print s.combine(5, 3)
