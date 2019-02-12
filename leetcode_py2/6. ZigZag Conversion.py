# -*- coding: utf-8 -*-
# @File  : 6. ZigZag Conversion.py
# @Author: Huang_xk
# @Date  : 12/30/17

'''
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
        (you may want to display this pattern in a fixed font for better legibility)
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

# Self-writting after solution
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows > len(s):
            return s

        index = 0
        step = 1
        res = [""] * numRows
        for ch in s:
            res[index] += ch
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step
        return "".join(res)


s = Solution()
print s.convert("ABC", 2)