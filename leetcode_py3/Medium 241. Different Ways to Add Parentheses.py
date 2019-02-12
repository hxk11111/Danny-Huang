# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/11
File:   Medium 241. Different Ways to Add Parentheses.py
"""
import operator
import re

'''
Given a string of numbers and operators, return all possible results from computing 
all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''


class Solution:
    def diffWaysToCompute(self, input: 'str') -> 'List[int]':
        tokens = re.split('(\D)', input)
        nums = list(map(int, tokens[::2]))
        ops = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2]))

        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b)
                    for i in range(lo, hi)
                    for a in build(lo, i)
                    for b in build(i + 1, hi)]

        return build(0, len(nums) - 1)

    def diffWaysToCompute2(self, input: 'str') -> 'List[int]':
        if not input:
            return []
        if not any(elem in input for elem in "+-*"):
            return [int(input)]
        result = []
        for ind, ch in enumerate(input):
            if ch in "+-*":
                left = self.diffWaysToCompute(input[:ind])
                right = self.diffWaysToCompute(input[ind + 1:])
                for l in left:
                    for r in right:
                        if ch == "-":
                            result.append(l - r)
                        elif ch == "+":
                            result.append(l + r)
                        else:
                            result.append(l * r)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.diffWaysToCompute2("11"))
