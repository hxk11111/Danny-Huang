# -*- coding: utf-8 -*-
# @File  : graph_word_ladder.py
# @Author: Huang_xk
# @Date  : 12/14/17

# 给定字典和一个起点单词、一个终点单词, 每次只能变换一个字母, 问从起点单词是否可以到达终点单词?最短多少步?
'''
    如：
         start = "hit"
         end = "cog"
         dict = ["hot","dot","dog","lot","log"]
         "hit" -> "hot" -> "dot" -> "dog" -> "cog"
'''


def transform_node(node_p):
    result_l = []
    for i in range(len(node_p)):
        for j in range(ord('a'), ord('z') + 1):
            if node_p[i] == chr(j):
                continue
            else:
                char = chr(j)
                new_string = node_p[:i] + char + node_p[i+1:]
                result_l.append(new_string)
    return result_l


def graph_word_ladder(start, end, string_l):
    curr_layer = []
    next_layer = []
    visited = []
    layer = 0
    flag = False
    if start == end:
        return 0
    curr_layer.append(start)
    while len(curr_layer) > 0 and not flag:
        layer += 1
        while len(curr_layer) > 0 and not flag:
            node = curr_layer.pop()
            result = transform_node(node)
            for elem in result:
                if elem == end:
                    return layer
                if elem in string_l and elem not in visited:
                    next_layer.append(elem)
                    visited.append(elem)
        curr_layer, next_layer = next_layer, curr_layer


string_l = ["hot", "dot", "dog", "lot", "log"]
start = "hit"
end = "cog"
print graph_word_ladder(start, end, string_l)