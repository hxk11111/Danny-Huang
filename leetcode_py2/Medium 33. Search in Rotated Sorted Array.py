# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 11:14 AM
# @Author  : Huang_xk
# @FileName: Medium 33. Search in Rotated Sorted Array.py


'''
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.
'''


# Self-writting
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        idx = -1

        while start <= end:
            if end - start == 1:
                if nums[start] == target:
                    idx = start
                elif nums[end] == target:
                    idx = end
                else:
                    break
            elif end == start:
                if nums[end] == target:
                    idx = end
                else:
                    break
            middle = (end - start) / 2 + start
            if nums[middle] == target:
                idx = middle
                break
            if nums[start] == target:
                idx = start
                break
            if nums[end] == target:
                idx = end
                break
            if nums[middle] <= nums[end]:
                if nums[end] > target and nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle
            else:
                if nums[middle] > target and nums[start] < target:
                    end = middle
                else:
                    start = middle + 1
        return idx


# Solution
class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        hi, lo = len(nums) - 1, 0

        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] == target: return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid
        return -1

s = Solution2()
print s.search([4,5], 8)