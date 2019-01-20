# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/20
File:   Medium 150. Evaluate Reverse Polish Notation.py
"""
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate 
to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''


class Solution(object):
    def calc(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num2 - num1
        elif operator == "*":
            return num1 * num2
        else:
            if num1 * num2 < 0 and num2 % num1 != 0:
                return num2 / num1 + 1
            else:
                return num2 / num1

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                result = self.calc(num1, num2, token)
                stack.append(result)
        return stack[-1]


if __name__ == '__main__':
    s = Solution()
    print s.evalRPN(
        ["-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16", "/",
         "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*", "-60",
         "+", "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*", "180", "70", "-40", "-", "*", "86",
         "132", "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-", "+", "28",
         "/", "95", "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/", "-62", "/", "93", "*", "196", "-",
         "-59", "+", "187", "-", "143", "/", "-79", "-89", "+", "-"])
