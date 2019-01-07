# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/7
File:   Medium 82. Remove Duplicates from Sorted List II.py
"""
'''
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
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
        while head:
            num = head.val
            if head.next and head.next.val == num:
                while head.next and head.next.val == num:
                    head = head.next
                head = head.next
            else:
                cur.next = ListNode(head.val)
                head = head.next
                cur = cur.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    result = s.deleteDuplicates(head)
    print result


