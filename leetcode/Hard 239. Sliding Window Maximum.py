# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/11
File:   Hard 239. Sliding Window Maximum.py
"""
'''
Given an array nums, there is a sliding window of size k which is moving from the very left 
of the array to the very right. You can only see the k numbers in the window. Each time the 
sliding window moves right by one position. Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if k <= 1:
            return nums

        deque = []
        result = []
        for i in range(k):
            while deque:
                if nums[i] > nums[deque[-1]]:
                    deque.pop()
                else:
                    break
            deque.append(i)

        for j in range(k, len(nums)):
            result.append(nums[deque[0]])
            if deque[0] < j - k + 1:
                del deque[0]
            while deque:
                if nums[j] > nums[deque[-1]]:
                    deque.pop()
                else:
                    break
            deque.append(j)

        result.append(nums[deque[0]])
        return result


if __name__ == '__main__':
    s = Solution()
    print s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
