# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/14
File:   Medium 127. Word Ladder.py
"""
'''
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        matrix = dict()
        for w in wordList:
            for i in range(len(w)):
                s = w[:i] + "_" + w[i + 1:]
                if s not in matrix:
                    matrix[s] = [w]
                else:
                    matrix[s].append(w)
        stack = [beginWord]
        visited_words = {beginWord}
        level = 1
        while stack:
            level += 1
            word_set = set()
            while stack:
                word = stack.pop()
                for i in range(len(word)):
                    tmp = word[:i] + "_" + word[i + 1:]
                    if tmp in matrix:
                        for next_word in matrix[tmp]:
                            if next_word not in visited_words:
                                word_set.add(next_word)
                                visited_words.add(next_word)
                                if next_word == endWord:
                                    return level
            stack = word_set
        return 0


if __name__ == '__main__':
    s = Solution()
    print s.ladderLength(beginWord="nanny",
                         endWord="cog",
                         wordList=["hot", "cig", "cit", "dog", "lot", "log", "cog"])
