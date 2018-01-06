# -*- coding: utf-8 -*-
# @File  : Medium 19. Remove Nth Node From End of List.py
# @Author: Huang_xk
# @Date  : 1/6/18

'''
    Given a linked list, remove the nth node from the end of list and return its head.

    For example,

       Given linked list: 1->2->3->4->5, and n = 2.

       After removing the second node from the end, the linked list becomes 1->2->3->5.
    Note:
    Given n will always be valid.
    Try to do this in one pass.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Self-writting
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        node_dict = {}
        temp = head
        while temp is not None:
            node_dict[count] = temp
            temp = temp.next
            count += 1
        removed_idx = count - n
        if removed_idx == count - 1 and count - 1 > 0:
            node_dict[removed_idx - 1].next = None
        elif removed_idx == count - 1 and count - 1 == 0:
            head = head.next
        elif 0 < removed_idx < count - 1:
            node_dict[removed_idx - 1].next = node_dict[removed_idx + 1]
        else:
            head = head.next
        return head


# Self-writting after solution
class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        res = head
        while n:
            temp = temp.next
            n -= 1

        if not temp:
            return head.next

        while temp.next:
            res = res.next
            temp = temp.next

        res.next = res.next.next
        return head