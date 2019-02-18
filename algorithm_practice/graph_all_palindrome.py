# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2018/12/23
File:   graph_all_palindrome.py
"""
'''
给定一个字符串s，将s划分成若干子串，使 得每一个子串都是回文串。计算s的所有可 能的划分。

如:s=“aab”，
返回:“aa”，“b”; “a”，“a”，“b”。
'''
final_result = []


def is_palindrome(s):
    start = 0
    end = len(s) - 1
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def dfs(s, start, path):
    if start == len(s):
        global final_result
        result = [elem for elem in path]
        final_result.append(result)
        return
    for i in range(start, len(s)):
        substr = s[start: i + 1]
        if is_palindrome(substr):
            path.append(substr)
            dfs(s, i + 1, path)
            path.pop()


def all_palindrome(s):
    if len(s) <= 1:
        return s
    dfs(s, 0, [])
    print final_result

if __name__ == '__main__':
    all_palindrome("ababa")