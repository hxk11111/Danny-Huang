# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/14
File:   Hard 128. Longest Consecutive Sequence.py
"""
'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        max_consecutive = 0
        current_length = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                while num + 1 in nums_set:
                    num += 1
                    current_length += 1
                max_consecutive = max(max_consecutive, current_length)
                current_length = 1
        return max_consecutive


if __name__ == '__main__':
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])
