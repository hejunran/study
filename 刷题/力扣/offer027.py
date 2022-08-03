# -*- coding: utf-8 -*-
# @Time : 2022/7/10 0:20
# @Author : hejunran

"""
题目描述：二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法一：递归调用
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root==None:return None
        temp =root.left
        root.left=self.mirrorTree(root.right)
        root.right=self.mirrorTree(temp)
        return root


# 方法二：借用栈的思想
class Solution2:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        stackA=[]
        stackB=[]
        if root:
            stackA.append(root)
        else:
            return []

        while stackA or stackB:
            while stackA:
                stackB.append(stackA.pop())
            while stackB:
                temp =stackB.pop()
                if temp:
                    temp.left,temp.right=temp.right,temp.left
                    stackA.append(temp.left)
                    stackA.append(temp.right)
        return root

if __name__ == '__main__':
    root = TreeNode(4)
    root.left=TreeNode(2)
    root.right=TreeNode(7)
    p=root.left
    q=root.right
    p.left = TreeNode(1)
    p.right = TreeNode(3)
    q.left=TreeNode(6)
    q.right=TreeNode(9)
    print(Solution2().mirrorTree(root))
