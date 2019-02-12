# -*- coding: utf-8 -*-
# @File  : 322. Coin Change.py
# @Author: Huang_xk
# @Date  : 1/3/18


'''
    You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    Example 1:
        coins = [1, 2, 5], amount = 11
        return 3 (11 = 5 + 5 + 1)

    Example 2:
        coins = [2], amount = 3
        return -1.
'''


class Solution(object):
    # Self-wrtting, time limit exceed
    #     def search(self, idx, coins, amount):
    #         max_value = 100000
    #         if amount == 0:
    #             return 0
    #         if amount < 0:
    #             return max_value
    #         if idx >= len(coins):
    #             return max_value
    #         return min(self.search(idx, coins, amount - coins[idx]) + 1,
    #                   self.search(idx + 1, coins, amount))

    #     def coinChange(self, coins, amount):
    #         """
    #         :type coins: List[int]
    #         :type amount: int
    #         :rtype: int
    #         """
    #         res = self.search(0, coins, amount)
    #         if res < 100000:
    #             return res
    #         else:
    #             return -1


    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_value = amount + 1
        dp = [max_value] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        res = dp[amount]
        if res > amount:
            return -1
        else:
            return res


s = Solution()
print s.coinChange([1, 2, 5], 11)