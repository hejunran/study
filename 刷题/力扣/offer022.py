# -*- coding: utf-8 -*-
# @Time : 2022/7/9 9:26
# @Author : hejunran

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return None

        p =head
        length=0
        while p!=None:
            p=p.next
            length=length+1
        if length<k:
            return head
        else:
            s =length-k

        if s ==0:
            return head
        elif s==1:
            return head.next
        p = head
        k=0
        while k<s:
            p=p.next
            k=k+1

        return p