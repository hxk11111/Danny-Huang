# -*- coding: utf-8 -*-
# @File  : 14. Longest Common Prefix.py
# @Author: Huang_xk
# @Date  : 1/2/18

'''
    Write a function to find the longest common prefix string amongst an array of strings.
'''


# Self-writting
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        count = 0
        first = strs[0]
        for elem in strs[1:]:
            if len(elem) < len(first):
                first = elem
        for i in range(len(first)):
            flag = True
            for elem in strs[1:]:
                if first[i] != elem[i]:
                    flag = False
                    break
            if flag:
                count += 1
            else:
                break
        return first[:count]


# Solution
class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        strs.sort()
        retVal = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                retVal += strs[0][i]
            else:
                break
        return retVal


# Self-writting after solution
class Solution3(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first = strs[0]
        for elem in strs[1:]:
            first = first[:len(elem)]
            while first != elem[:len(first)]:
                first = first[:-1]
        return first


s = Solution3()
print s.longestCommonPrefix(["abc", "abekl", "abb"])
