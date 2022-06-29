# -*- coding: utf-8 -*-
# @Time : 2022/6/30 10:43
# @Author : hejunran
"""
题目描述：青蛙跳台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

。
"""
"""
思路：如果求跳N阶台阶的可能次数，那么小青蛙跳到第N阶台阶时，其前一次必然是跳到第N-1阶台阶或者第N-2阶台阶上，
那么求跳N阶台阶的可能次数，只需要求跳第第N-1阶台阶或者第N-2阶台阶的可能次数，
即 dp（N）=dp（N-1）+ dp（N-2）
这个动态规划类似于斐波那契数列
这和爬楼梯类似

"""
# 递归虽然可以求但是时间复杂度大
class Solution:
    def numWays(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            return self.numWays(n-1) + self.numWays(n-2)



# 看清题目要求
class Solution2:
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return n
        else:
            s = []
            s.append(0)
            s.append(1)
            s.append(2)
            for i in range(3, n + 1):
                s.append(s[i - 1] + s[i - 2])
            return s[-1]
