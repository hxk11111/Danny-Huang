# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/26
File:   Medium 187. Repeated DNA Sequences.py
"""
'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to 
identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        table = {}
        for i in range(len(s) - 9):
            if s[i:i + 10] in table:
                table[s[i:i + 10]] += 1
            else:
                table[s[i:i + 10]] = 1
        res = dict(filter(lambda x: x[1] >= 2, table.items()))
        return res.keys()


if __name__ == '__main__':
    s = Solution()
    print s.findRepeatedDnaSequences("AAAAAAAAAAA")