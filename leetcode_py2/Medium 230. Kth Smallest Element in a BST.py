# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/1
File:   Medium 230. Kth Smallest Element in a BST.py
"""
'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def get_path(self, root, path):
        if not root:
            return
        self.get_path(root.left, path)
        path.append(root.val)
        self.k -= 1
        if self.k == 0:
            self.result = path[-1]
            return
        self.get_path(root.right, path)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.result = None
        path = []
        self.get_path(root, path)
        return self.result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root_left = TreeNode(1)
    root_right = TreeNode(4)
    root_left.right = TreeNode(2)
    root.left = root_left
    root.right = root_right
    print s.kthSmallest(root, 1)
