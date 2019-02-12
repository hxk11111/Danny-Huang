# -*- coding: utf-8 -*-
# @File  : Easy 69. Sqrt(x).py
# @Author: Huang_xk
# @Date  : 1/22/18

'''
    Implement int sqrt(int x).

    Compute and return the square root of x.

    x is guaranteed to be a non-negative integer.


    Example 1:

    Input: 4
    Output: 2
    Example 2:

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
'''

# Self-writting after solution
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        left, right = 1, x
        ans = 0
        while left <= right:
            mid = left + (right - left) / 2
            if mid <= x / mid:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans