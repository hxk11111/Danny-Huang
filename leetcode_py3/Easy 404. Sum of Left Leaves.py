# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/3/22
File:   Easy 404. Sum of Left Leaves.py
"""
'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0
        return self.get_left_leave(root)

    def get_left_leave(self, node):
        total = 0
        if node.left:
            left_node = node.left
            if left_node.left is None and left_node.right is None:
                total += left_node.val
            total += self.get_left_leave(left_node)
        if node.right:
            total += self.get_left_leave(node.right)
        return total


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.sumOfLeftLeaves(root))
