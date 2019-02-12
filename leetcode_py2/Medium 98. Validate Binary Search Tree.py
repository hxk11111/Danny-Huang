# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/11
File:   Medium 98. Validate Binary Search Tree.py
"""
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input:
    2
   / \
  1   3
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_valid_root(self, root, lower_limit, upper_limit):
        if not root:
            return True
        if lower_limit is not None and root.val <= lower_limit:
            return False
        if upper_limit is not None and root.val >= upper_limit:
            return False
        left_flag = self.is_valid_root(root.left, lower_limit, root.val) if root.left else True
        if left_flag:
            return self.is_valid_root(root.right, root.val, upper_limit) if root.right else True
        else:
            return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid_root(root, None, None)


if __name__ == '__main__':
    t = TreeNode(0)
    t.right = TreeNode(-1)
    s = Solution()
    print s.isValidBST(t)
