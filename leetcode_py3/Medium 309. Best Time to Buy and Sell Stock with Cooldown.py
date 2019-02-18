# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/18
File:   Medium 309. Best Time to Buy and Sell Stock with Cooldown.py
"""
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''


class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        have = cool = float('-inf')
        free = 0
        for price in prices:
            free, cool, have = max(free, cool), have + price, max(have, free - price)
        return max(free, cool)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))
