# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/2
File:   Medium 55. Jump Game.py
"""
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false

Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) == 1 and nums[0] >= 0) or len(nums) == 0:
            return True
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 1)[::-1]:
            furthest_jump = min(len(nums) - 1, i + nums[i])
            for s in range(i + 1, furthest_jump + 1)[::-1]:
                if s == len(nums) - 1 or dp[s]:
                    dp[i] = True
                    break
        return dp[0]


if __name__ == '__main__':
    s = Solution()
    print s.canJump([2, 5, 0, 0])
