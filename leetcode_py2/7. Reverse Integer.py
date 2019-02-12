# -*- coding: utf-8 -*-
# @File  : 7. Reverse Integer.py
# @Author: Huang_xk
# @Date  : 12/31/17

'''
    Given a 32-bit signed integer, reverse digits of an integer.

        Example 1:
            Input: 123
            Output:  321

    Note:
    Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
            x *= -1
        res = 0
        while x > 0:
            res = res * 10 + (x % 10)
            x /= 10
        res *= flag

        if abs(res) > 0x7FFFFFFF:
            return 0
        else:
            return res

