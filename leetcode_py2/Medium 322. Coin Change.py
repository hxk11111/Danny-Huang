# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/14
File:   Medium 322. Coin Change.py
"""
'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins_num = len(coins)
        dp = [[amount + 1 for _ in range(coins_num + 1)] for _ in range(amount + 1)]
        for i in range(coins_num + 1):
            dp[0][i] = 0
        for i in range(1, amount + 1):
            for j in range(1, coins_num + 1):
                if coins[j - 1] > i:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - coins[j - 1]][j] + 1)
        if dp[-1][-1] == amount + 1:
            return -1
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print s.coinChange(coins=[2], amount=3)
