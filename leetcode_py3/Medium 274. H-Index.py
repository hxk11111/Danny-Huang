# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/13
File:   Medium 274. H-Index.py
"""
'''
Given an array of citations (each citation is a non-negative integer) of a researcher, 
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: 
"A scientist has index h if h of his/her N papers have at least h citations each, 
and the other N − h papers have no more than h citations each."

Example:
Input: citations = [3,0,6,1,5]
Output: 3 

Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''


class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        citations = sorted(citations)
        length = len(citations)
        for ind, num in enumerate(citations):
            if num >= length - ind:
                return length - ind
        return 0

    def hIndex2(self, citations):
        n = len(citations)
        citeCount = [0] * (n + 1)
        for c in citations:
            if c >= n:
                citeCount[n] += 1
            else:
                citeCount[c] += 1

        i = n - 1
        while i >= 0:
            citeCount[i] += citeCount[i + 1]
            if citeCount[i + 1] >= i + 1:
                return i + 1
            i -= 1
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.hIndex([3, 0, 6, 1, 5]))
