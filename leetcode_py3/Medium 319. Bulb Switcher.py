# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/19
File:   Medium 319. Bulb Switcher.py
"""
'''
There are n bulbs that are initially off. You first turn on all the bulbs. 
Then, you turn off every second bulb. On the third round, you toggle every third bulb 
(turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. 
For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:
Input: 3
Output: 1
 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
'''


class Solution:
    def bulbSwitch(self, n: 'int') -> 'int':
        bulbs = [1 for _ in range(n)]
        for i in range(2, n + 1):
            for ind, j in enumerate(bulbs[i - 1::i]):
                if j == 0:
                    bulbs[i * ind + i - 1] = 1
                else:
                    bulbs[i * ind + i - 1] = 0
        return sum(bulbs)


if __name__ == '__main__':
    s = Solution()
    print(s.bulbSwitch(999))
