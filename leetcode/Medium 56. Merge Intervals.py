# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/3
File:   Medium 56. Merge Intervals.py
"""
'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                last = result[-1]
                if last.end < interval.start:
                    result.append(interval)
                else:
                    start = min(last.start, interval.start)
                    end = max(last.end, interval.end)
                    result[-1] = Interval(start, end)
        return result


if __name__ == '__main__':
    # [[1,3],[8,10],[2,6],[15,18]]
    intervals = [Interval(1, 3), Interval(8, 10), Interval(2, 6), Interval(15, 18)]
    s = Solution()
    result = s.merge(intervals)
    print result
