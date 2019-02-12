# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111(hxk11111@baidu.com)
Date:	2018/12/26
File:   Medium 31. Next Permutation.py
"""
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        flag = False
        for i in range(length - 2, -1, -1):
            tmp = nums[i]
            for j in range(length - 1, i, -1):
                if nums[j] > tmp:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i + 1:] = nums[i + 1:][::-1]
                    flag = True
                    break
            if flag:
                break
        if not flag:
            nums[:] = nums[::-1]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print nums
