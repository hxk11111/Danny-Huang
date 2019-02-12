# -*- coding: utf-8 -*-
# @File  : Medium 18. 4Sum.py
# @Author: Huang_xk
# @Date  : 1/5/18

'''
    Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
    Find all unique quadruplets in the array which gives the sum of target.

    Note: The solution set must not contain duplicate quadruplets.

    For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

    A solution set is:
        [
          [-1,  0, 0, 1],
          [-2, -1, 1, 2],
          [-2,  0, 0, 2]
        ]
'''


# Self-writting, modified by solution
class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        length = len(nums)
        for i in range(length - 3):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                for j in range(i + 1, length - 2):
                    if j == i + 1 or ((j > i + 1) and nums[j] != nums[j - 1]):
                        p = j + 1
                        q = length - 1
                        while p < q:
                            sum_res = nums[i] + nums[j] + nums[p] + nums[q]
                            if sum_res == target:
                                res.append([nums[i], nums[j], nums[p], nums[q]])
                                while p < q and nums[p + 1] == nums[p]:
                                    p += 1
                                while p < q and nums[q - 1] == nums[q]:
                                    q -= 1
                                p += 1
                                q -= 1
                            elif sum_res > target:
                                q -= 1
                            else:
                                p += 1
        return res


# Solution
class Solution2(object):
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:  # early termination
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results



s = Solution()
print s.fourSum([1, 0, -1, 0, -2, 2], 0)

