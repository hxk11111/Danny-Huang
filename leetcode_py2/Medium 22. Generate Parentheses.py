# -*- coding: utf-8 -*-
# @Time    : 08/01/2018 11:18 PM
# @Author  : Huang_xk
# @FileName: Medium 22. Generate Parentheses.py

'''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
'''


class Solution(object):
    def getOneResult(self, left, right, res, res_list):
        if not left and not right:
            res_list.append(res)
            return
        if left:
            self.getOneResult(left - 1, right, res + "(", res_list)
        if right and left < right:
            self.getOneResult(left, right - 1, res + ")", res_list)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res_list = []
        self.getOneResult(n, n, "", res_list)
        return res_list

