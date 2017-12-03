# encoding=utf-8
# String permutation problem
# 给定字符串S[0...N-1]，设计算法，枚举S的全排列。

def str_permutation(start, end, str_p):
    if start == end:
        print str_p
    for i in range(start, end):
        str_p[i], str_p[start] = str_p[start], str_p[i]
        str_permutation(start + 1, end, str_p)
        str_p[i], str_p[start] = str_p[start], str_p[i]


str_p = [1, 2, 3, 4]
str_permutation(0, 4, str_p)
