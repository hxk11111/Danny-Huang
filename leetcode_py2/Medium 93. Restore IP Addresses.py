# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/10
File:   Medium 93. Restore IP Addresses.py
"""
'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''


class Solution(object):
    def dfs(self, result, path, s, start):
        if start > len(s) - 1:
            return
        if len(path) == 3:
            if s[start] == "0":
                if start == len(s) - 1:
                    result.append(".".join(path + [s[start:]]))
                else:
                    return
            else:
                if 0 <= int(s[start:]) <= 255:
                    result.append(".".join(path + [s[start:]]))
            return
        if s[start] == "0":
            path.append(s[start])
            self.dfs(result, path, s, start + 1)
            path.pop()
        else:
            for l in range(start + 1, start + 4):
                if 0 <= int(s[start:l]) <= 255:
                    path.append(s[start:l])
                    self.dfs(result, path, s, l)
                    path.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.dfs(result, [], s, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.restoreIpAddresses("10030023")
