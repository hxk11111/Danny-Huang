# -*- coding: utf-8 -*-
# @File  : 125. Valid Palindrome.py
# @Author: Huang_xk
# @Date  : 1/2/18


'''
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    For example,
        "A man, a plan, a canal: Panama" is a palindrome.
        "race a car" is not a palindrome.

    Note:
    Have you consider that the string might be empty? This is a good question to ask during an interview.

    For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
