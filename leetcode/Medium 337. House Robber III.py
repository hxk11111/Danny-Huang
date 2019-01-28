# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/28
File:   Medium 337. House Robber III.py
"""
'''
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self.rob_dfs(root)
        return result[1]

    def rob_dfs(self, node):
        if not node:
            return 0, 0
        left = self.rob_dfs(node.left)
        right = self.rob_dfs(node.right)
        # rob later, max(rob now, rob later)
        return left[1] + right[1], max(left[0] + right[0] + node.val, left[1] + right[1])

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)

    left = TreeNode(4)
    left.left = TreeNode(1)
    left.right = TreeNode(3)

    right = TreeNode(5)
    right.right = TreeNode(1)

    root.left = left
    root.right = right

    print s.rob(root)