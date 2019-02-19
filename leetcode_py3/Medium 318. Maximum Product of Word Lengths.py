# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/19
File:   Medium 318. Maximum Product of Word Lengths.py
"""
'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) 
where the two words do not share common letters. You may assume that each word will contain only 
lower case letters. If no such two words exist, return 0.

Example 1:
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".

Example 3:
Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
'''


class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        length = len(words)
        max_length = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                words_set1 = set(words[i])
                words_set2 = set(words[j])
                if not words_set1 & words_set2:
                    max_length = max(max_length, len(words[i]) * len(words[j]))
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
