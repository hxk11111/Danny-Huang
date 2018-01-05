# -*- coding: utf-8 -*-
# @File  : Medium 15. 3Sum.py
# @Author: Huang_xk
# @Date  : 1/4/18

'''
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Note: The solution set must not contain duplicate triplets.

    For example, given array S = [-1, 0, 1, 2, -1, -4],

    A solution set is:
        [[-1, 0, 1],[-1, -1, 2]]
'''


# Self-writting
class Solution(object):
    def quick_sort(self, nums):
        if len(nums) == 0:
            return []
        large = []
        small = []
        length = len(nums)
        target = nums[0]
        count = 1
        for i in range(1, length):
            if nums[i] < target:
                small.append(nums[i])
            elif nums[i] == target:
                count += 1
            else:
                large.append(nums[i])
        return self.quick_sort(small) + [target] * count + self.quick_sort(large)

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        # sorted_nums = self.quick_sort(nums)
        sorted_nums = sorted(nums)
        res = []

        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and sorted_nums[i] != sorted_nums[i - 1]):
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    if sorted_nums[i] + sorted_nums[start] + sorted_nums[end] == 0:
                        res.append([sorted_nums[i], sorted_nums[start], sorted_nums[end]])
                        while start < end and sorted_nums[start] == sorted_nums[start + 1]:
                            start += 1
                        while start < end and sorted_nums[end] == sorted_nums[end - 1]:
                            end -= 1
                        start += 1
                        end -= 1
                    elif sorted_nums[i] + sorted_nums[start] + sorted_nums[end] > 0:
                        end -= 1
                    else:
                        start += 1
        return res


# Self-writting after solution
class Solution2(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        result = []
        # unique_num = dic.keys()
        if 0 in dic and dic[0] > 2:
            result.append([0, 0, 0])

        pos = [elem for elem in dic if elem > 0]
        neg = [elem for elem in dic if elem < 0]

        for p in pos:
            for n in neg:
                residual = - p - n
                if residual in dic:
                    if (residual == p or residual == n) and dic[residual] > 1:
                        result.append([n, residual, p])
                    elif residual > p:
                        result.append([n, p, residual])
                    elif residual < n:
                        result.append([residual, n, p])
                    elif residual == 0:
                        result.append([n, 0, p])

        return result


s = Solution2()
print s.threeSum([-1, 0, 1, -2, 1, 2, -1, -4])
