# -*- coding: utf-8 -*-
# @Time : 2022/7/5 17:02
# @Author : hejunran

"""
题目描述：打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999
"""
from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:

        s = '9'*n
        L=[]
        for i in range(int(s)):
            L.append(i+1)
        return L


if __name__ == '__main__':
    s ='9'*3
    t = int(s)
    print('9'*3)
    Solution().printNumbers(10)