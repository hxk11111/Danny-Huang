# -*- coding: utf-8 -*-
# @Time    : 13/01/2018 6:49 PM
# @Author  : Huang_xk
# @FileName: Easy 26. Remove Duplicates from Sorted Array.py

'''
    Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

    Do not allocate extra space for another array,
    you must do this by modifying the input array in-place with O(1) extra memory.

    Example:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the new length.
'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 1
        if len(nums) <= 1:
            return len(nums)
        while idx < len(nums):
            if nums[idx] == nums[idx - 1]:
                nums.remove(nums[idx])
            else:
                idx += 1
        return len(nums)


class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        idx = 0
        max_length = 1
        for i in range(1, length):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]
                max_length += 1
        return max_length


s = Solution2()
print s.removeDuplicates([1, 2, 2])