# -*- coding: utf-8 -*-
# @File  : Medium 29. Divide Two Integers.py
# @Author: Huang_xk
# @Date  : 1/22/18

'''
    Divide two integers without using multiplication, division and mod operator.

    If it is overflow, return MAX_INT.
'''

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


s = Solution()
print s.divide(12,5)