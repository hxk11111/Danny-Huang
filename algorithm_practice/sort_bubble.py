# -*- coding: utf-8 -*-
# @Time    : 08/12/2017 10:27 PM
# @Author  : Huang_xk
# @FileName: sort_bubble.py

def bubble_sort(list_p):
    length = len(list_p)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if list_p[j] > list_p[j + 1]:
                list_p[j], list_p[j + 1] = list_p[j + 1], list_p[j]
    return list_p


l = [1, 2, 13, 8, 5, 6, 3, 4]
print bubble_sort(l)
