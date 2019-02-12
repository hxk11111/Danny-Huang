# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/15
File:   Medium 131. Palindrome Partitioning.py
"""
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution(object):
    def is_palindrome(self, string):
        start = 0
        end = len(string) - 1
        while start <= end:
            if string[start] == string[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def dfs(self, result, path, string, start):
        if start == len(string):
            result.append(path[:])
            return
        for i in range(start, len(string)):
            if self.is_palindrome(string[start: i + 1]):
                path.append(string[start: i + 1])
                self.dfs(result, path, string, i + 1)
                path.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.dfs(result, [], s, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.partition("aab")
