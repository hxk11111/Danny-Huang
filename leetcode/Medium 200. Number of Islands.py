# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/12
File:   Medium 200. Number of Islands.py
"""
'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
'''


class Solution(object):
    def keep_going(self, grid, r, c, stack):
        if r - 1 >= 0 and grid[r - 1][c] == "1":
            stack.append((r - 1, c))
            grid[r - 1][c] = "0"
        if r + 1 < len(grid) and grid[r + 1][c] == "1":
            stack.append((r + 1, c))
            grid[r + 1][c] = "0"
        if c + 1 < len(grid[0]) and grid[r][c + 1] == "1":
            stack.append((r, c + 1))
            grid[r][c + 1] = "0"
        if c - 1 >= 0 and grid[r][c - 1] == "1":
            stack.append((r, c - 1))
            grid[r][c - 1] = "0"

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        islands = 0
        for r in range(row):
            for c in range(col):
                stack = []
                if grid[r][c] == "1":
                    stack.append((r, c))
                    grid[r][c] = "."
                while stack:
                    r_i, c_i = stack.pop()
                    self.keep_going(grid, r_i, c_i, stack)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == ".":
                    islands += 1
        return islands


if __name__ == '__main__':
    s = Solution()
    print s.numIslands(
        [["1", "0", "1", "1", "1"],
         ["1", "0", "1", "0", "1"],
         ["1", "1", "1", "0", "1"]])
