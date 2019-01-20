# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/17
File:   Medium 139. Word Break.py
"""
'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        dp = [False for _ in range(len(s))]
        length_set = set([len(word) for word in wordDict])
        min_length = min(length_set)
        for i in range(len(s)):
            if s[:i + 1] in wordDict:
                dp[i] = True
            elif i + 1 >= min_length:
                for length in length_set:
                    if i + 1 >= length and s[i + 1 - length:i + 1] in wordDict:
                        if dp[i - length]:
                            dp[i] = dp[i - length]
                            break
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print s.wordBreak(s="applepenapple", wordDict=["apple", "pen"])
