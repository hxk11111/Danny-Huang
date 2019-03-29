# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/27
File:   Easy 412. Fizz Buzz.py
"""
from typing import List

'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples 
of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(n):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                result.append("FizzBuzz")
            elif (i + 1) % 3 == 0:
                result.append("Fizz")
            elif (i + 1) % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i + 1))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))
