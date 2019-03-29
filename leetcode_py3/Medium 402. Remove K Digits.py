# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/20
File:   Medium 402. Remove K Digits.py
"""
'''
Given a non-negative integer num represented as a string, 
remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. 
Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''


class Solution:
    def removeKdigits_time_limit_exceed(self, num: str, k: int) -> str:
        length = len(num)
        if length <= k:
            return "0"
        return self.remove_one_digit(0, num, k)

    def remove_one_digit(self, total, num, k):
        if k == 0:
            return total * 10 ** len(num) + int(num)
        length = len(num)
        num_list = [self.remove_one_digit(total, num[1:], k - 1)]
        for i in range(1, length - k):
            num_list.append(
                self.remove_one_digit(total * 10 ** i + int(num[:i]), num[i + 1:], k - 1))
        num_list.append(total * 10 ** (length - k) + int(num[:-k]))
        return min(num_list)

    def removeKdigits(self, num: str, k: int) -> str:
        length = len(num)
        if length <= k:
            return "0"
        stack = [0]
        start_ind = 1
        while start_ind < length and k > 0:
            if len(stack) > 0 and num[stack[-1]] > num[start_ind]:
                stack.pop()
                k -= 1
            else:
                stack.append(start_ind)
                start_ind += 1

        while k > 0 and len(stack) > 0:
            stack.pop()
            k -= 1

        result = num[start_ind:]
        for elem in stack[::-1]:
            result = num[elem] + result

        zero_ind = 0
        while zero_ind < len(result) and result[zero_ind] == "0":
            zero_ind += 1
        return result[zero_ind:] or "0"


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("10200", 1))
