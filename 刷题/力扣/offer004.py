# -*- coding: utf-8 -*-
# @Time : 2022/6/28 18:13
# @Author : hejunran

"""
题目描述：
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

"""
from typing import List

# 方法一：全局遍历，加上提前结束标志符
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 0:
            return False
        col = len(matrix[0])
        row = len(matrix)
        flag =False
        i=0
        while i <row:
            j=0
            while j < col:
                if matrix[i][j]==target:
                    flag=True
                    j = col
                    i = row
                j = j+1
            i= i+1

        if flag==True:
            return True
        else:
            return False


# 方法二：观察数组的特点，旋转45度，类似于二叉树
class Solution2:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        if len(matrix) == 0:
            return False

        i = len(matrix) - 1
        col = len(matrix[0])
        j = 0

        while i >= 0 and j < col:
            if matrix[i][j] < target:
                j = j + 1
            elif matrix[i][j] > target:
                i = i - 1
            else:
                return True
        return False


        pass


if __name__ == '__main__':
    matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target=5

    pass