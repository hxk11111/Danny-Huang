# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/14
File:   Medium 518. Coin Change 2.py
"""
'''
You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that amount. 
You may assume that you have infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10] 
Output: 1

Note:
You can assume that
0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
'''


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        num_coins = len(coins)
        dp = [[0 for _ in range(num_coins + 1)] for _ in range(amount + 1)]
        for i in range(num_coins + 1):
            dp[0][i] = 1
        for j in range(1, amount + 1):
            for i in range(1, num_coins + 1):
                if coins[i - 1] > j:
                    dp[j][i] = dp[j][i - 1]
                else:
                    dp[j][i] = dp[j][i - 1] + dp[j - coins[i - 1]][i]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.change(amount=5, coins=[1, 2, 5]))
