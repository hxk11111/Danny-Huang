# -*- coding: utf-8 -*-
# @Time    : 06/01/2018 2:30 PM
# @Author  : Huang_xk
# @FileName: Medium 81. Search in Rotated Sorted Array II.py


'''
    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Write a function to determine if a given target is in the array.

    The array may contain duplicates.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (end - start) / 2 + start
            while nums[middle] == nums[end] and middle < end:
                end -= 1
            while middle < end and nums[middle] == nums[middle + 1]:
                middle += 1
            if nums[middle] == target:
                return True
            if nums[middle] <= nums[end]:
                if nums[end] >= target and nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                if nums[middle] > target and nums[start] <= target:
                    end = middle - 1
                else:
                    start = middle + 1
        return False



# Solution
class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        i, j = 0, len(nums) - 1
        while i < j:
            m = (i + j) / 2
            if nums[m] == target:
                return True

            if nums[j] < nums[m]:
                if nums[i] <= target and target <= nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            elif nums[j] > nums[m]:
                if nums[j] >= target and target >= nums[m]:
                    i = m + 1
                else:
                    j = m - 1
            else:
                j -= 1

        return nums[j] == target


s = Solution()
print s.search([1, 1,2,3,4,1,1,1,1], 2)