# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/12
File:   Easy 257. Binary Tree Paths.py
"""
'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def search_path(self, result, path, node):
        if not node.left and not node.right:
            result.append("->".join(path + [node.val]))
            return
        if node.left:
            path.append(node.val)
            self.search_path(result, path, node.left)
            path.pop()
        if node.right:
            path.append(node.val)
            self.search_path(result, path, node.right)
            path.pop()

    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        result = []
        self.search_path(result, [], root)
        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode("1")
    root.left = TreeNode("2")
    root.right = TreeNode("3")
    root.left.right = TreeNode("4")
    print(s.binaryTreePaths(root))
