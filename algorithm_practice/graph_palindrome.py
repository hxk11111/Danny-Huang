# -*- coding: utf-8 -*-
# @File  : graph_palindrome.py
# @Author: Huang_xk
# @Date  : 12/16/17

# graph palindrome problem
# 给定一个字符串s, 将s划分成若干子串, 使得每一个子串都是回文串。计算s的所有可能的划分
'''
    如: s=“aab”, 返回
     “aa”,“b”;
     “a”,“a”,“b”。
'''


def graph_palindrome_problem(string_p):
    result = []
    path = []
    start = 0
    dfs(result, path, string_p, start)
    return result


def dfs(result, path, string_p, start):
    length = len(string_p)
    if start == length:
        res = []
        for item in path:
            res.append(item)
        result.append(res)
        return
    for i in range(start + 1, length + 1):
        if is_palindrome(string_p[start:i]):
            path.append(string_p[start:i])
            dfs(result, path, string_p, i)
            path.pop()


def is_palindrome(string_p):
    if len(string_p) <= 0:
        return False
    start = 0
    end = len(string_p) - 1
    while start < end:
        if string_p[start] == string_p[end]:
            start += 1
            end -= 1
        else:
            return False
    return True


print graph_palindrome_problem("ababa")
