# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/1/10
File:   Medium 92. Reverse Linked List II.py
"""
'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse(self, node):
        last = None
        while node:
            nxt = node.next
            node.next = last
            last = node
            node = nxt
        return last

    def find_kth_node(self, head, k):
        for i in range(k):
            if not head:
                return None
            head = head.next
        return head

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        m_prev = self.find_kth_node(dummy, m - 1)
        mth = m_prev.next
        nth = self.find_kth_node(dummy, n)
        n_next = nth.next
        nth.next = None
        self.reverse(mth)
        m_prev.next = nth
        mth.next = n_next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    res = s.reverseBetween(node, 2, 4)
    print res
