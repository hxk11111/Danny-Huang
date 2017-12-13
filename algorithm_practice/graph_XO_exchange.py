# -*- coding: utf-8 -*-
# @File  : graph_XO_exchange.py
# @Author: Huang_xk
# @Date  : 12/13/17

# 给定二维平面,格点处要么是‘X’,要么是 ‘O’。求出所有由‘X’围成的区域
# 找到这样的(多个)区域后,将所有的‘O’翻转 成‘X’即可
'''
    X X X X                 X X X X
    X O O X    =====>>>     X X X X
    X X O X                 X X X X
    X O X X                 X O X X
'''

# 解题思路： 从四周的节点开始，如果有节点为"O"，做一个标记，这个节点一定在最终结果中还是"O"，它不会被"X"包围
#           然后从四周的"O"开始，找它上下左右的"O"，如果找到做个标记，这个点在最终结果中一定还为"O"


# 检验某一个节点是不是O
def is_valid_O(matrix_p, j, i):
    rows = len(matrix_p)
    cols = len(matrix_p[0])
    if j < 0 or i < 0 or j >= rows or i >= cols or matrix_p[j][i] != "O":
        return False
    return True

# 检验从某个节点还能不能继续访问，即它的上下左右还有没有O节点
def could_continue(matrix_p, j, i):
    next_node = []
    next_move = [(j + 1, i), (j - 1, i), (j, i - 1), (j, i + 1)]
    for i in range(len(next_move)):
        if is_valid_O(matrix_p, next_move[i][0], next_move[i][1]):
            matrix_p[next_move[i][0]][next_move[i][1]] = "Y"
            next_node.append((next_move[i][0], next_move[i][1]))
    return next_node

# 从一个几点开始做广度优先遍历，看节点是否能从O变成X
def bfs(matrix_p, m, n):
    queue = []
    if is_valid_O(matrix_p, m, n):
        matrix_p[m][n] = "Y"
        queue.append((m, n))
    while len(queue) != 0:
        m_org, n_org = queue[0]
        queue.remove(queue[0])
        queue += could_continue(matrix_p, m_org, n_org)


def graph_XO_exchange(matrix_p):
    if len(matrix_p) == 0 or len(matrix_p[0]) == 0:
        return
    m = len(matrix_p)  # 矩阵的行数
    n = len(matrix_p[0])  # 矩阵的列数
    for i in range(n):
        bfs(matrix_p, 0, i)
        bfs(matrix_p, m - 1, i)
    for j in range(1, m - 1):
        bfs(matrix_p, j, 0)
        bfs(matrix_p, j, n - 1)
    for i in range(n):
        for j in range(m):
            if matrix_p[j][i] == "O":
                matrix_p[j][i] = "X"
            if matrix_p[j][i] == "Y":
                matrix_p[j][i] = "O"


matrix = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
graph_XO_exchange(matrix)
for row in matrix:
    print row
