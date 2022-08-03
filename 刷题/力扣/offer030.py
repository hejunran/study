# -*- coding: utf-8 -*-
# @Time : 2022/7/10 15:28
# @Author : hejunran

"""
包含min函数的栈
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l1 = []

    def push(self, x: int) -> None:
        self.l1.append(x)

    def pop(self) -> None:
        if len(self.l1) == 0: return None
        self.l1.pop()

    def top(self) -> int:
        if len(self.l1) == 0: return None
        return self.l1[-1]

    def min(self) -> int:
        if len(self.l1) == 0: return None
        min = self.l1[0]
        for i in range(len(self.l1)):
            if min > self.l1[i]:
                min = self.l1[i]
        return min

