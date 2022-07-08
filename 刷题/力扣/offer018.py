# -*- coding: utf-8 -*-
# @Time : 2022/7/5 17:19
# @Author : hejunran

"""
题目描述：删除链表节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head==None: return head

        if head.val==val:
            head=head.next
            return head
        p = head
        q = head.next
        while q.val!=val:
            q = q.next
            p=p.next
        if q.val==val:
            p.next=q.next
        return head



        pass