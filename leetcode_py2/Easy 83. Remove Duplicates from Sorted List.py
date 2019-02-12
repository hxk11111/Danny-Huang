# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/7
File:   Easy 83. Remove Duplicates from Sorted List.py
"""
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(-1)
        cur.next = head
        while head:
            if head.next and head.val == head.next.val:
                head = head.next
                cur.next = head
            else:
                cur = cur.next
                head = head.next
        return dummy.next
