# -*- coding: utf-8 -*-
# @Time    : 24/12/2017 7:58 PM
# @Author  : Huang_xk
# @FileName: dp_minimal_path.py

'''
    In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right,
    by only moving to the right and down, is indicated in bold red and is equal to 2427.
               (131 673	234	103	18
                201 96  342 965	150
                630	803 746 422 111
                537	699	497 121 956
                805	732	524 37  331)
    Find the minimal path sum
'''


def dp_minimal_path(matrix_p):
    rows = len(matrix_p)
    cols = len(matrix_p[0])
    dp_matrix = [[0] * cols for _ in range(rows)]
    dp_matrix[rows - 1][cols - 1] = matrix_p[rows - 1][cols - 1]
    for i in range(rows - 2, -1, -1):
        dp_matrix[i][cols - 1] = matrix_p[i][cols - 1] + dp_matrix[i + 1][cols - 1]
    for j in range(cols - 2, -1, -1):
        dp_matrix[rows - 1][j] = matrix_p[rows - 1][j] + dp_matrix[rows - 1][j + 1]

    for i in range(rows - 2, -1, -1):
        for j in range(cols - 2, -1, -1):
            dp_matrix[i][j] = min(dp_matrix[i + 1][j], dp_matrix[i][j + 1]) + matrix_p[i][j]
    return dp_matrix[0][0]


matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111],
          [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]
print dp_minimal_path(matrix)
