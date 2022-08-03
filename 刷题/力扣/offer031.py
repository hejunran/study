# -*- coding: utf-8 -*-
# @Time : 2022/7/12 20:38
<<<<<<< HEAD
# @Author : hejunran


from typing import  List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        i=0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1]==popped[i]:
                stack.pop()
                i=i+1
        return not stack
=======
# @Author : hejunran
>>>>>>> origin/master
