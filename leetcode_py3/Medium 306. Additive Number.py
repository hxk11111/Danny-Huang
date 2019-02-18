# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/18
File:   Medium 306. Additive Number.py
"""
'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
             
Example 2:
Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?
'''


class Solution:
    def isAdditiveNumber(self, num: 'str') -> 'bool':
        length = len(num)
        half_length = length // 2 + 1
        for i in range(1, half_length):
            for j in range(i, length - 1):
                num1 = num[:i]
                num2 = num[i:j + 1]
                if (num1.startswith("0") and len(num1) != 1) or (num2.startswith("0") and len(num2) != 1):
                    continue
                num1 = int(num1)
                num2 = int(num2)
                ind = j
                while ind <= length - 1:
                    total = str(num1 + num2)
                    if num[ind + 1:ind + 1 + len(total)] == total:
                        ind = ind + len(total)
                        num1 = num2
                        num2 = int(total)
                    else:
                        break
                if ind == length - 1:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isAdditiveNumber("12122436"))
