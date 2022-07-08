# -*- coding: utf-8 -*-
# @Time : 2022/7/4 16:36
# @Author : hejunran
"""
题目描述：数值的整数次方
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题
"""


# 方法一：一遍一遍乘，超出时间复杂度
class Solution:
    def myPow(self, x: float, n: int) -> float:
        s=1.0
        if n<0:
            n=-n
            for i in range(n):
                s=s*x
            s = 1/s
        elif n>0:
            for i in range(n):
                s=s*x
        else:
            return  1
        return s

# 利用二分法乘积
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        if x==0: return 0
        res=1.0
        if n <0:
            res=1/res
            n=-n
        while n:
            if n&1: res *=x
            x *= x
            n >>= 1
        return res






if __name__ == '__main__':
    print(Solution().myPow(0.00001,2147483647))