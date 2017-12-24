# -*- coding: utf-8 -*-
# @Time    : 23/12/2017 10:32 PM
# @Author  : Huang_xk
# @FileName: dp_max_triangle.py

'''
    在下面的数字三角形中寻找一条从顶部到底边的路径，使得路径上所经过的数字之和最大。
    路径上的每一步都只能往左下或 右下走。只需要求出这个最大和即可，不必给出具体路径。
    三角形的行数大于1小于等于100，数字为 0 - 99
    输入格式：
    5      //表示三角形的行数
    接下来输入三角形
    7
    3   8
    8   1   0
    2   7   4   4
    4   5   2   6   5
    要求输出最大和
'''


def dp_max_triangle(list_triangle):
    depth = len(list_triangle)
    res_list = [0] * depth
    path = []
    # 先将res_list赋值为三角形的最后一行
    for i in range(depth):
        res_list[i] = list_triangle[depth - 1][i]
    for i in range(depth - 2, -1, -1):
        layer_path = []
        for j in range(len(list_triangle[i])):
            if res_list[j] > res_list[j + 1]:
                layer_path.append(j)
            else:
                layer_path.append(j + 1)
            res_list[j] = max(res_list[j], res_list[j + 1]) + list_triangle[i][j]
        path.append(layer_path)
    res_path = [list_triangle[0][0]]
    next_layer = path.pop()[0]
    res_path.append(list_triangle[i + 1][next_layer])
    for i in range(1, len(path) + 1):
        next_layer = path.pop()[next_layer]
        res_path.append(list_triangle[i + 1][next_layer])
    return res_list[0], res_path


list_triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print dp_max_triangle(list_triangle)
