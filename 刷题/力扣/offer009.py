# -*- coding: utf-8 -*-
# @Time : 2022/6/29 8:55
# @Author : hejunran
"""
 题目描述：用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]


"""

class CQueue:

    def __init__(self):
        self.A=[]
        self.B=[]


    def appendTail(self, value: int) -> None:
        # 入栈
        self.A.append(value)

    # 队列的特点是先进先出，栈的特点是先进后出
    # 我们可以使用两个栈解决这个问题，一个输入栈stdin, 一个输出栈stdout
    # 队列进行添加操作时，添加到输入栈中
    # 队列进行删除操作时，先判断输出栈是否为空？不为空则出栈
    # 为空的话，判断输入栈是否为空，为空返回-1，不为空就把输入栈中的元素压入到输出栈中，
    # 然后输出栈在进行pop操作，就将元素实现了倒序，从而将先进后出变成先进先出

    def deleteHead(self) -> int:
        # 先出栈
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()