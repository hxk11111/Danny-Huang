# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/4
File:   Hard 57. Insert Interval.py
"""
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge_intervals(self, interval1, interval2):
        start = min(interval1.start, interval2.start)
        end = max(interval1.end, interval2.end)
        return Interval(start, end)

    def merge_behinds(self, intervals, ind, new_interval):
        for i, interval in enumerate(intervals[ind + 1:]):
            if new_interval.end < interval.start:
                return new_interval, i + ind + 1
            else:
                new_interval = self.merge_intervals(interval, new_interval)
        return new_interval, len(intervals)

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x.start)
        new_start = newInterval.start
        intervals_result = []
        ind = 0
        flag = True
        if len(intervals) == 0:
            return [newInterval]
        while ind < len(intervals):
            interval = intervals[ind]
            if interval.start > newInterval.end and ind == 0:
                intervals_result.append(newInterval)
                intervals_result.append(interval)
                flag = False
            elif interval.end < new_start and ind == len(intervals) - 1:
                intervals_result.append(interval)
                intervals_result.append(newInterval)
                flag = False
            elif interval.end < new_start and intervals[ind + 1].start > newInterval.end:
                intervals_result.append(interval)
                intervals_result.append(newInterval)
                flag = False
            elif not interval.end < new_start and flag:
                newInterval = self.merge_intervals(interval, newInterval)
                newInterval, ind = self.merge_behinds(intervals, ind, newInterval)
                intervals_result.append(newInterval)
                flag = False
                continue
            else:
                intervals_result.append(interval)
            ind += 1
        return intervals_result



if __name__ == '__main__':
    #[[1,3],[6,9]]
    intervals = [Interval(1, 3), Interval(6, 9)]
    new_interval = Interval(2, 5)
    s = Solution()
    result = s.insert(intervals, new_interval)
    print result
