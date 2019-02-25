# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/24
File:   Hard 336. Palindrome Pairs.py
"""
from typing import List

'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, 
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        table = dict()
        for ind, word in enumerate(words):
            table[word] = ind

        result = []
        for idx, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):
                left_part = word[:i]
                right_part = word[i:]
                if (self.is_palindrome(left_part) and right_part[::-1] in table
                        and table[right_part[::-1]] != idx):
                    result.append([table[right_part[::-1]], idx])

                if (len(right_part) > 0 and self.is_palindrome(right_part)
                        and left_part[::-1] in table and table[left_part[::-1]] != idx):
                    result.append([idx, table[left_part[::-1]]])

        return result

    def is_palindrome(self, word):
        start = 0
        end = len(word) - 1
        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
