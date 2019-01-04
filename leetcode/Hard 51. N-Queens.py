# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/2
File:   Hard 51. N-Queens.py
"""
'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution(object):
    def is_valid(self, row_ind, col_i, rows, diagonal, rev_diagonal):
        if col_i in rows:
            return False
        if diagonal[row_ind + col_i] > 0:
            return False
        if rev_diagonal[col_i - row_ind + len(rows) - 1] > 0:
            return False
        return True

    def dfs(self, queens_result, rows, row_ind, diagonal, rev_diagonal):
        if all(elem >= 0 for elem in rows):
            queens_result.append(["".join(["." if i != col else "Q" for i in range(len(rows))]) for col in rows])
            return
        for ind, elem in enumerate(rows[row_ind:]):
            if elem < 0:
                for i in range(len(rows)):
                    row_i = row_ind + ind
                    col_i = i
                    if self.is_valid(row_i, col_i, rows, diagonal, rev_diagonal):
                        rows[row_i] = col_i
                        diagonal[i + row_i] = 1
                        rev_diagonal[i - row_i + len(rows) - 1] = 1
                        self.dfs(queens_result, rows, row_i + 1, diagonal, rev_diagonal)
                        rows[row_i] = -1
                        diagonal[i + row_i] = -1
                        rev_diagonal[i - row_i + len(rows) - 1] = -1

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        rows = [-1 for _ in range(n)]
        diagonal = [-1 for _ in range(2 * n)]
        rev_diagonal = [-1 for _ in range(2 * n)]
        final_result = []
        self.dfs(final_result, rows, 0, diagonal, rev_diagonal)
        return final_result


if __name__ == '__main__':
    s = Solution()
    print s.solveNQueens(5)
