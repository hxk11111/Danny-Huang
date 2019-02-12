# -*- coding: utf-8 -*-
# @File  : 9. Palindrome Number.py
# @Author: Huang_xk
# @Date  : 1/1/18

'''
    Determine whether an integer is a palindrome. Do this without extra space.
'''


# Self-writting
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed_int = 0
        temp = x
        while temp > 0:
            residual = temp % 10
            temp /= 10
            reversed_int = reversed_int * 10 + residual
        if reversed_int == x:
            return True
        else:
            return False




# Solution:
class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]