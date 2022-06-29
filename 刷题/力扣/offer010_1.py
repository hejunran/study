# -*- coding: utf-8 -*-
# @Time : 2022/6/29 13:26
# @Author : hejunran
"""
题目描述：斐波拉且数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
"""

# 递归
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n ==1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)

# 因为原题目要求取模，且有时间限制，因此递归不行
class Solution2:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n ==1:
            return 1
        else:
            s=[]
            s.append(0)
            s.append(1)
            # s[0]=0   # 列表添加元素要用append才行
            # s[1]=1
            for i in range(2,n+1):
                s.append(s[i-1]+s[i-2])
        return s[-1]%1000000007


"""
yield 和 return有一定的区别
return：在函数中返回某个值，然后函数结束运行。一般没有返回值类型，就不用写return
yield：带yield的函数是一个迭代器，在函数内部碰到yield 的时候，函数会返回某个值，并停留在这个位置，
当下次执行函数后，会在上次停留的位置继续运行。
"""

class Solution3:
    def creater(self,n):
        current, a, b = 2, 1, 2
        while current < n + 1:
            yield a
            a, b = b, a + b
            current += 1

    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            for a in self.create(n):
                ret = a
            return ret % 1000000007
