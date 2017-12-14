# -*- coding: utf-8 -*-
# @Time    : 10/12/2017 5:44 PM
# @Author  : Huang_xk
# @FileName: stack_match_brackets.py

# Match the brackets which have the longest length
# 给定字符串，仅包含左括号'('和右括号')'，它可能不是括号匹配的，设计算法，找出最长匹配的括号子串，返回该子串的长度。
# 如:"(()":2;"(()())":6

def stack_match_brackets(string_p):
    length = len(string_p)
    stack = []
    max_len = 0
    last = -1               # this last index records the last time when ")" appears
    for i in range(length):
        if string_p[i] == "(":
            stack.append(i)
            continue
        if len(stack) == 0:
            last = i
        else:
            k = stack.pop()
            if len(stack) == 0:
                max_len = max(max_len, i - last)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len

print stack_match_brackets(")))(())())())")
