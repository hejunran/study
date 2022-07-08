# -*- coding: utf-8 -*-
# @Time : 2022/7/4 13:54
# @Author : hejunran

"""
题目描述：二进制中1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），
返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        s=[]
        if n == 0: return 0
        # 辗转相除法把二进制存储到列表中。
        while n//2!=0:
            s.append(n%2)
            n = n//2
        if n//2==0:s.append(1)
        count =0
        for i in range(len(s)):
            if s[i]==1:
                count =count+1
        return count

# 利用bin把数字转换为二进制数，然后再转换成字符串
class Solution2:
    def hammingWeight(self, n: int) -> int:
        n_str = str(bin(n))

# 利用按位与运算来实现，按位与运算，当
# n&1=0，当n的末尾是0时，n&1等于0
# n&1=1，当n的末尾是1时，n&1等于1
# n>>=1是无符号数的右移1位操作。
class Solution3:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            if n&1==1: res =res+1
            n>>=1
        return res

if __name__ == '__main__':
    Solution2().hammingWeight(11)