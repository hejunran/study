# -*- coding: utf-8 -*-
# @Time : 2022/7/9 9:54
# @Author : hejunran

"""
反转链表
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None:
            return None

        p = head
        q = head
        p = p.next
        q.next=None
        while p!=None:
            s=p
            p=p.next
            s.next=q
            q=s
        return q
