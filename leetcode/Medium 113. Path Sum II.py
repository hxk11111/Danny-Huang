# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/12
File:   Medium 113. Path Sum II.py
"""
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, result, path, node, target):
        if node.val == target and node.left is None and node.right is None:
            result.append(path + [node.val])
            return
        if node.left:
            path.append(node.val)
            self.dfs(result, path, node.left, target - node.val)
            path.pop()
        if node.right:
            path.append(node.val)
            self.dfs(result, path, node.right, target - node.val)
            path.pop()


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        self.dfs(result, [], root, sum)
        return result