# -*- coding: utf-8 -*-
# @Time : 2022/7/5 20:39
# @Author : hejunran
"""
题目描述：调整数组顺序使奇数位于偶数前面

"""
from typing import List
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        L1=[0]*50000
        L2=[0]*50000
        i=0
        j=0
        k=0
        while i<len(nums):
            if nums[i]%2!=0:
                L1[j]=nums[i]
                i =i+1
                j=j+1
            else:
                L2[k]=nums[i]
                k=k+1
                i =i+1

        return L1[:j]+L2[:k]


# 双指针,一个指向数组头部，一个指向数组尾部，头部的指针
class Solution2:
    def exchange(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1

        while i <j:
            if nums[i]%2!=0:
                i=i+1
                continue
            elif nums[j]%2==0:
                j=j-1
                continue
            else:
                nums[j],nums[i]=nums[i],nums[j]
                i = i+1
                j = j-1

        return nums




