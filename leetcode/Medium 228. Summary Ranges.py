# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/31
File:   Medium 228. Summary Ranges.py
"""
'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        tmp_result = [nums[0]]
        for num in nums[1:]:
            if not tmp_result or num - tmp_result[-1] == 1:
                tmp_result.append(num)
            else:
                if len(tmp_result) == 1:
                    result.append(str(tmp_result[0]))
                else:
                    result.append("->".join([str(tmp_result[0]), str(tmp_result[-1])]))
                tmp_result = [num]
        if len(tmp_result) == 1:
            result.append(str(tmp_result[0]))
        else:
            result.append("->".join([str(tmp_result[0]), str(tmp_result[-1])]))
        return result


if __name__ == '__main__':
    s = Solution()
    print s.summaryRanges([0, 1, 2, 4, 5, 7])
