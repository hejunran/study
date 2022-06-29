# -*- coding: utf-8 -*-
# @Time : 2022/6/29 8:54
# @Author : hejunran

"""
题目描述：遍历二叉树
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

"""
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        out=[]
        if head !=None:
            p=head.next
            out.append(head.val)
        else:
            return out

        while p!=None:
            out.append(p.val)
            p=p.next

        i=len(out)-1
        j=0
        while i>j:
            out[i],out[j]=out[j],out[i]
            i =i-1
            j =j+1
        return out