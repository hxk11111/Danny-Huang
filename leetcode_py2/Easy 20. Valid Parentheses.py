# -*- coding: utf-8 -*-
# @Time    : 07/01/2018 8:28 PM
# @Author  : Huang_xk
# @FileName: Easy 20. Valid Parentheses.py

'''
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) > 0 and stack.pop() == "(":
                    continue
                else:
                    return False
            elif s[i] == "]":
                if len(stack) > 0 and stack.pop() == "[":
                    continue
                else:
                    return False
            elif s[i] == "}":
                if len(stack) > 0 and stack.pop() == "{":
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

s = Solution()
print s.isValid("()[]{}")