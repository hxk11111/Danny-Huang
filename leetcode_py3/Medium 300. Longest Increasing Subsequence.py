# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/17
File:   Medium 300. Longest Increasing Subsequence.py
"""
'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
 
Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n^2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        sorted_nums = sorted(list(set(nums)))
        length = len(nums)
        length2 = len(sorted_nums)
        dp = [[0 for _ in range(length + 1)] for _ in range(length2 + 1)]
        for i in range(1, length2 + 1):
            for j in range(1, length + 1):
                if nums[j - 1] == sorted_nums[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def lengthOfLIS2(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        length = len(nums)
        dp = [0 for _ in range(length)]
        max_ans = 1
        for i in range(length):
            max_length = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_length = max(max_length, dp[j])
            dp[i] = max_length + 1
            max_ans = max(max_ans, dp[i])
        return max_ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS2([1, 3, 6, 7, 9, 4, 10, 5, 6]))
