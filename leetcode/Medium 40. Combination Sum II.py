# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/30
File:   Medium 40. Combination Sum II.py
"""
'''
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
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
            result = sorted([elem for elem in path])
            if result not in final_result:
                final_result.append(result)
            return

        for i, num in enumerate(candidates[ind:]):
            tmp_sum = sum(path) if path else 0
            if tmp_sum + num <= target:
                path.append(num)
                self.dfs(final_result, path, ind + 1 + i, candidates, target)
                path.pop()


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum2([10], 10)
