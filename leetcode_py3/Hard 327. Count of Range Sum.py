# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/21
File:   Hard 327. Count of Range Sum.py
"""
'''
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n^2) is trivial. You MUST do better than that.

Example:
Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
'''


class Solution:
    def countRangeSum(self, nums: 'List[int]', lower: 'int', upper: 'int') -> 'int':
        sums = [0]
        total = 0
        for num in nums:
            total += num
            sums.append(total)

        ans = 0
        for i in range(len(sums) - 1):
            for j in range(i + 1, len(sums)):
                if lower <= sums[j] - sums[i] <= upper:
                    ans += 1
        return ans

    def countRangeSum2(self, nums: 'List[int]', lower: 'int', upper: 'int') -> 'int':
        count_sum = {0: 1}
        pre_sum = 0
        ans = 0
        for num in nums:
            pre_sum += num
            for item in range(lower, upper + 1):
                if pre_sum - item in count_sum:
                    ans += count_sum[pre_sum - item]
            count_sum[pre_sum] = count_sum.get(pre_sum, 0) + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countRangeSum2(nums=[-2, 5, -1], lower=-2, upper=2))
