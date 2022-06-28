# -*- coding: utf-8 -*-
# @Time : 2022/6/28 18:13
# @Author : hejunran

from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        col = len(matrix[0])
        row = len(matrix)

        flag = False
        i=0
        j=0
        while(i<row and j < col):
            if matrix[i][j]==target:
                flag = True
                break

        pass



if __name__ == '__main__':
    pass