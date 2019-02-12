# -*- coding: utf-8 -*-
# @File  : 647. Palindromic Substrings.py
# @Author: Huang_xk
# @Date  : 12/29/17

'''
    Given a string, your task is to count how many palindromic substrings in this string.

    The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

    Example 1:
        Input: "abc"
        Output: 3
        Explanation: Three palindromic strings: "a", "b", "c".

'''

# After reading solution
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        count = 0
        dp = [[False]*length for _ in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        return count


s = Solution()
print s.countSubstrings("aaa")