# -*- coding: utf-8 -*-
# @Time : 2022/6/28 18:13
# @Author : hejunran

"""
题目的描述：
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ','%20')



