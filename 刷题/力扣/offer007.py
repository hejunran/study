# -*- coding: utf-8 -*-
# @Time : 2022/6/29 8:55
# @Author : hejunran
"""
题目描述：重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

经验总结：二叉树的问题一般都是分治思想，递归去做。因为二叉树本身就是递归定义的
"""
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None

        # 构建根节点
        root = TreeNode(preorder[0])
        # 因为在inorder和preorder中二叉树还是以列表的形式存储的，只是存储了值，故可以用index取的左右子树分割的位置
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx+1],inorder[0:idx])
        root.right =self.buildTree(preorder[idx+1:],inorder[idx+1:])

        return root

# 方法二：利用hash哈希表存储inorder中序表中各个节点的位置，然后再去前序表中根据长度分割左右子树
# 这样做是为了减少查询左右子树节点位置造成的时间复杂度变高
class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildtree(preorder:List[int],inorder:List[int],pre_left:int,pre_right:int,in_left:int,in_right:int) ->TreeNode:
            root =TreeNode(preorder[pre_left])
            mid = hash[preorder[pre_left]]    # 根据先序遍历找到根节点，然后利用hash表找到其在inorder中的位置索引，这样以便计算左子树的长度

            left_nums = mid - in_left  # 左子树的长度
            root.left  = buildtree(preorder,inorder,pre_left+1,pre_left+left_nums-1,in_left,mid-1)
            root.right = buildtree(preorder,inorder,pre_left+left_nums+1,pre_right,mid+1,in_right)

        hash=dict()
        n = len(preorder)
        # 根据节点的长度，hash表中存储的是各个节点的位置索引。
        for i in range(n):
            hash[inorder[i]]=i
        return buildtree(preorder,inorder,0,n-1,0,n-1)
