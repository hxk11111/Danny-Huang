# -*- coding: utf-8 -*-
# @File  : 2. Add Two Numbers.py
# @Author: Huang_xk
# @Date  : 12/26/17



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        ten = 0
        while l1 or l2 or ten:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            result.append((l1_val + l2_val + ten) % 10)
            ten = (l1_val + l2_val + ten) / 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result
