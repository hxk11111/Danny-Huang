# -*- coding: utf-8 -*-
# @File  : Medium 17. Letter Combinations of a Phone Number.py
# @Author: Huang_xk
# @Date  : 1/5/18


'''
    Given a digit string, return all possible letter combinations that the number could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below.

    Input:Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
               "9": "wxyz", "0": " "}
        res = []
        for s in digits:
            if s == "1" or s == "0":
                return []
            if len(res) == 0:
                for elem in dic[s]:
                    res.append(elem)
            else:
                temp = []
                for elem in res:
                    for char in dic[s]:
                        temp.append(elem + char)
                res = temp
        return res


s = Solution()
print s.letterCombinations("875")