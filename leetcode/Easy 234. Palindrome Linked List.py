# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This module is provided by
	Authors: hxk11111
Date:	2019/2/2
File:   Easy 234. Palindrome Linked List.py
"""
'''
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


if __name__ == '__main__':
    s= Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    # head.next.next.next = ListNode(1)
    print s.isPalindrome(head)
