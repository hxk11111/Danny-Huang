# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/29
File:   Medium 417. Pacific Atlantic Water Flow.py
"""
from typing import List

'''
Given an m x n matrix of non-negative integers representing the height of each unit 
cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix 
and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another 
one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] 
(positions with parentheses in above matrix).
'''


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        dp_pacific = [[False for _ in range(cols)] for _ in range(rows)]
        dp_atlantic = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            self.dfs(dp_pacific, matrix, i, 0, rows, cols)
            self.dfs(dp_atlantic, matrix, i, cols - 1, rows, cols)

        for j in range(cols):
            self.dfs(dp_pacific, matrix, 0, j, rows, cols)
            self.dfs(dp_atlantic, matrix, rows - 1, j, rows, cols)

        result = []
        for i in range(rows):
            for j in range(cols):
                if dp_atlantic[i][j] and dp_pacific[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, visited, matrix, i, j, m, n):
        visited[i][j] = True
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for d in directions:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(visited, matrix, x, y, m, n)


if __name__ == '__main__':
    s = Solution()
    print(s.pacificAtlantic(
        [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
