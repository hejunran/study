# -*- coding: utf-8 -*-
# @Time : 2022/7/3 14:14
# @Author : hejunran

"""
题目描述：查询一个二维表格中是否存在一个字符串

解题思路是：利用深度优先便利和回溯法。
"""
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1: return True
            board[i][j] = ''
            if dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1):
                return True
            board[i][j] = word[k]

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    Solution().exist(board,word)

