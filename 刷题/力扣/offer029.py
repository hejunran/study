# -*- coding: utf-8 -*-
# @Time : 2022/7/10 11:44
# @Author : hejunran
"""
题目描述：顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []    # 如果matrix不存在，返回空列表
        l,r,t,b,res=0,len(matrix[0])-1,0,len(matrix)-1,[]

        while True:
            for i in range(l,r+1):
                res.append(matrix[t][i])    # 从左向右遍历
            t=t+1  # 遍历上方一行，t加1
            if t>b:break  # 如果是最后一行跳出
            for i in range(t,b+1):
                res.append(matrix[i][r])     # 从上向下遍历
            r =r-1
            if r<l:break     # 如果遍历最后一列跳出

            for i in range(r,l-1,-1):      # 从右向左遍历
                res.append(matrix[b][i])
            b=b-1
            if b<t: break
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l=l+1
            if l>r:break


        return res