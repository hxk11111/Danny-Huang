# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/27
File:   Hard 32. Longest Valid Parentheses.py
"""
'''
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            elem = s[i]
            if elem == ")" and s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
            elif elem == ")" and s[i - 1] == ")":
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = 0
        return max(dp)

    def longestValidParentheses_stack(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_length = 0
        for ind, elem in enumerate(s):
            if elem == "(":
                stack.append(ind)
            elif elem == ")":
                stack.pop()
                if len(stack) == 0:
                    stack.append(ind)
                    continue
                length = ind - stack[-1]
                max_length = max(max_length, length)
        return max_length



if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses_stack("(()))()()()))(()()()))")
