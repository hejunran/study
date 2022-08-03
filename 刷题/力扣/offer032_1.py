# -*- coding: utf-8 -*-
# @Time : 2022/7/12 20:41
# @Author : hejunran

"""
从上到下打印二叉树
层次遍历
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from  typing import List
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        stackA=[]
        stackB=[]

        L=[]
        if root==None:return []
        stackA.append(root)
        while stackA or stackB:
            if not stackB:
                while stackA:
                    temp=stackA.pop()
                    if temp:
                        L.append(temp.val)
                        stackB.append(temp.left)
                        stackB.append(temp.right)
            else:
                while stackB:
                    stackA.append(stackB.pop())
                # stackA.append(stackB.pop())
        return L

if __name__ == '__main__':
    root = TreeNode(3)
    root.left=TreeNode(9)
    root.right=TreeNode(20)
    p=root.left
    q=root.right
    q.left=TreeNode(15)
    q.right=TreeNode(7)
    Solution().levelOrder(root)