# -*- coding: utf-8 -*-
# @Time : 2022/7/9 12:54
# @Author : hejunran

"""
合并两个排序链表
合并之后仍然递增
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head=p=head_p=l1
        q=l2
        if l1==None:return l2
        if l2==None:return l1
        if p.val>q.val:
            head=head_p=q
            q=q.next
        else:
            head=head_p=p
            p=p.next
        while p!=None and q!=None:
            if p.val>q.val:
                head_p.next=q
                head_p=q
                q=q.next
            else:
                head_p.next=p
                head_p = p
                p=p.next
        if p==None:
            head_p.next=q
            return head
        if q==None:
            head_p.next=p
            return head