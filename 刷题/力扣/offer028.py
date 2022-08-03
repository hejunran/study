# -*- coding: utf-8 -*-
# @Time : 2022/7/10 10:31
# @Author : hejunran
"""
对称二叉树
判断一颗二叉树是否对称
"""


# 方法一:一个比较直白的方法，该树翻转之后和以前相同，则镜像对称，先求其对称树，然后和原树比较
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import copy
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def reserve_tree(root:TreeNode)->bool:
            if root==None:return None
            temp=root.left
            root.left=reserve_tree(root.right)
            root.right=reserve_tree(temp)
            return root

        def match_tree(root:TreeNode,re_root:TreeNode)->bool:
            if root==None and re_root!=None:return False
            if root!=None and re_root==None:return False
            if root==None and re_root==None:return True
            if root.val!=re_root.val:return False
            else:
                left=match_tree(root.left,re_root.left)
                right=match_tree(root.right,re_root.right)
                return left and right
        """
        注意此处用到了深度copy，因为如果不用深度copy，root和re_root在内存的地址是一样的，
        也就是root变成翻转之后的树了，再怎么比较也是和re_root相同
        """
        copy_root = copy.deepcopy(root)
        re_root=reserve_tree(copy_root)
        return match_tree(root,re_root)


# 方法二：直接递归比较，只需要保证左子树的右节点值和右子树的左节点值相同，左子树的左节点值和右子树的右节点值相同
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        def match(l_root:TreeNode,r_root:TreeNode)->bool:
            if l_root==None and r_root==None:return True
            if l_root!=None and r_root==None:return False
            if l_root==None and r_root!=None:return False
            if l_root.val!=r_root.val:return False
            else:
                l = match(l_root.left,r_root.right)
                r = match(l_root.right, r_root.left)
                return l and r
        return match(root.left,root.right) if root else True





if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right = TreeNode(2)
    p =root.left
    q =root.right
    p.left=TreeNode(None)
    p.right=TreeNode(3)
    q.left=TreeNode(None)
    q.right=TreeNode(3)

    print(Solution().isSymmetric(root))