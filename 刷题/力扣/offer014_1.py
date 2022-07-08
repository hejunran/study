# -*- coding: utf-8 -*-
# @Time : 2022/7/4 13:53
# @Author : hejunran


# 绳子每段分为长度为3的长度，成绩最大，利用数学推导得出来的。
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n<=3: return n-1
        a ,b = n//3 ,n%3
        if b==0:
            return 3**a
        elif b==1:
            return (3**(a-1))*4
        elif b==2:
            return (3**a)*2



# 利用动态规划做
class Solution2:
    def cuttingRope(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(3,n+1):
            for j in range(2,i):
                dp[i]=max(dp[i],max(j*(i-j),j*dp[i-j]))
        return dp[n]



if __name__ == '__main__':
    Solution().cuttingRope(10)