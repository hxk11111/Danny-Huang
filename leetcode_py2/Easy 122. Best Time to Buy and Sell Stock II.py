# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/13
File:   Easy 122. Best Time to Buy and Sell Stock II.py
"""
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time 
(i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
             
Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
             
Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        last_price = prices[0]
        for price in prices:
            if price < last_price:
                max_profit += last_price - min_price
                last_price = price
                min_price = price
            else:
                last_price = price
        max_profit += last_price - min_price
        return max_profit

    def maxProfit2(self, prices):
        if not prices:
            return 0
        total_profit = 0
        single_max_profit = 0
        last_price = prices[0]
        for price in prices:
            if price >= last_price:
                single_max_profit += price - last_price
            else:
                total_profit += single_max_profit
                single_max_profit = 0
            last_price = price
        if single_max_profit > 0:
            total_profit += single_max_profit
        return total_profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit2([7, 1, 5, 3, 6, 4]))
