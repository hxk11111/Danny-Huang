# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/2
File:   Medium 49. Group Anagrams.py
"""
'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return d.values()


if __name__ == '__main__':
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
