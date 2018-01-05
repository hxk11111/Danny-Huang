# -*- coding: utf-8 -*-
# @File  : Medium 16. 3Sum Closest.py
# @Author: Huang_xk
# @Date  : 1/5/18


'''
    Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        min_diff = nums[length - 3] + nums[length - 2] + nums[length - 1]
        for i in range(length - 2):
            j, k = (i + 1), (length - 1)
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res == target:
                    return res
                if abs(target - res) < abs(target - min_diff):
                    min_diff = res

                if res > target:
                    k -= 1
                if res < target:
                    j += 1
        return min_diff


s = Solution()
print s.threeSumClosest([-1, 2, 1, -4], 1)