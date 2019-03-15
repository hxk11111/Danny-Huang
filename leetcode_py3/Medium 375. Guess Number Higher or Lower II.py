# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/13
File:   Medium 375. Guess Number Higher or Lower II.py
"""
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. 
You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
'''


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for low in range(n, 0, -1):
            for high in range(low + 1, n + 1):
                dp[low][high] = min(
                    [i + max(dp[low][i - 1], dp[i + 1][high]) for i in range(low, high)])
        return dp[1][n]


if __name__ == '__main__':
    s = Solution()
    print(s.getMoneyAmount(10))