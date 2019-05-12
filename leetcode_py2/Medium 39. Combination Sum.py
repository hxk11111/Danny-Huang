# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/30
File:   Medium 39. Combination Sum.py
"""
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        final_result = []
        self.dfs(final_result, [], 0, candidates, target)
        return final_result

    def dfs(self, final_result, path, ind, candidates, target):
        if sum(path) == target:
            result = [elem for elem in path]
            final_result.append(result)
            return
        for i, num in enumerate(candidates[ind:]):
            tmp_sum = sum(path) if path else 0
            if tmp_sum + num <= target:
                path.append(num)
                self.dfs(final_result, path, ind + i, candidates, target)
                path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 10))
