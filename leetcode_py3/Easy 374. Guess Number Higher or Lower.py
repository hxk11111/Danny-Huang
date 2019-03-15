# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/13
File:   Easy 374. Guess Number Higher or Lower.py
"""
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
 
Example :
Input: n = 10, pick = 6
Output: 6
'''


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
def guess(num):
    if num == 6:
        return 0
    elif num < 6:
        return -1
    else:
        return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start <= end:
            mid = (start + end) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                end = mid - 1
            else:
                start = mid + 1


if __name__ == '__main__':
    s = Solution()
    print(s.guessNumber(10))
