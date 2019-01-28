# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/28
File:   Hard 212. Word Search II.py
"""
'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example:
Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Output: ["eat","oath"]

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''


class Solution(object):
    def could_continue(self, i, j, word, board, visited):
        if not word:
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        if not visited[i][j] and board[i][j] == word[0]:
            visited[i][j] = True
            if (self.could_continue(i - 1, j, word[1:], board, visited) or
                    self.could_continue(i, j - 1, word[1:], board, visited) or
                    self.could_continue(i + 1, j, word[1:], board, visited) or
                    self.could_continue(i, j + 1, word[1:], board, visited)):
                return True
            visited[i][j] = False
            return False

    def is_valid_word(self, word, board, visited):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.could_continue(r, c, word, board, visited):
                    return True
        return False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        rows = len(board)
        cols = len(board[0])
        result = []
        for word in words:
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            if self.is_valid_word(word, board, visited):
                result.append(word)
        return list(set(result))


if __name__ == '__main__':
    s = Solution()
    print s.findWords(board=
    [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ], words=["oath", "pea", "eat", "rain"])
