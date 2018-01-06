# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 9:23 AM
# @Author  : Huang_xk
# @FileName: Medium 153. Find Minimum in Rotated Sorted Array.py

'''
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Find the minimum element.

    You may assume no duplicate exists in the array.
'''


# Self-writting
class Solution(object):
    def search(self, nums, start, end):
        if start == end:
            return nums[start]
        elif end - start == 1:
            if nums[end] > nums[start]:
                return nums[start]
            else:
                return nums[end]
        middle = (end - start) / 2 + start
        if nums[start] > nums[middle]:
            # In this circumstance, the minimum element lies in the front half
            res = self.search(nums, start, middle)
        elif nums[start] < nums[end]:
            return nums[start]
        else:
            res = self.search(nums, middle + 1, end)
        return res

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums
        else:
            return self.search(nums, 0, len(nums) - 1)


# Self-writting after solution
class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            middle = (end - start) / 2 + start
            if nums[start] <= nums[middle] <= nums[end]:
                return nums[start]
            elif nums[start] <= nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle


s = Solution2()
print s.findMin([4, 5, 6, 7, 0, 1, 2])
