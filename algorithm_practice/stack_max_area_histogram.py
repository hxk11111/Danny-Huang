# -*- coding: utf-8 -*-
# @File  : stack_max_area_histogram.py
# @Author: Huang_xk
# @Date  : 12/11/17

# 给定n个非负整数,表示直方图的方柱的高度,
# 同时,每个方柱的宽度假定都为1;试 找出直方图中最大的矩形面积。
# 如:给定高度为:2,1,5,6,2,3,最大面积为10。

def stack_max_area_histogram(list_p):
    list_p.append(0)  # 在栈的最后一位加入0
    length = len(list_p)
    stack = []
    max_area = 0
    stack.append(0)
    for i in range(1, length):
        if len(stack) == 0:
            stack.append(i)
            continue
        while len(stack) > 0:
            if list_p[i] >= list_p[stack[len(stack) - 1]]:
                stack.append(i)
                break
            else:
                top = stack.pop()
                if len(stack) == 0:
                    max_area = max(max_area, list_p[top] * i)
                    stack.append(i)
                    break
                else:
                    max_area = max(max_area, list_p[top] * (i - stack[len(stack) - 1] - 1))
    return max_area


print stack_max_area_histogram([2,1,5,6,2,3])
print stack_max_area_histogram([2,7,5,6,4])

