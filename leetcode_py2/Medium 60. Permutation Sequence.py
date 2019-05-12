# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/5
File:   Medium 60. Permutation Sequence.py
"""
'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
'''


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(elem + 1) for elem in range(n)]
        factorial = [1] * n
        k -= 1
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i
        result = []
        for j in range(n):
            index = k / factorial[n - 1 - j]
            result.append(nums[index])
            nums.remove(nums[index])
            k = k % factorial[n - 1 - j]
        return "".join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(4, 9))
