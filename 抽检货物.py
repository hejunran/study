import sys

class Solution:
    def count_min_sum(self,s):
        length=len(s)
        if length==0:
            return 0
        elif length==1:
            return s[0]
        elif length==2:
            return min(s[0],s[1])
        elif length==3:
            return min(s[0]+s[2],s[1])
        else:
            return min(min(s[0]+s[1]+self.count_min_sum(s[2:]),s[0]+s[2]+self.count_min_sum(s[3:])),
                       min(s[1]+s[2]+self.count_min_sum(s[3:]),s[1]+s[3]+self.count_min_sum(s[4:])))

class Solution1:
    def count_sum_min(self,s):
        good=0
        dp=[]
        if len(s)==1:
            return dp[0]
        elif len(s)==2:
            return min(s[0],s[1])
        else:
            length=len(s)
            dp.append(s[0])
            dp.append(s[1])
            for i in range(2,length):
                # 注意此处不能写dp[i]=s[i]+ min(dp[i-1],dp[i-2]),因为dp是一个列表不知道其长度，直接赋值i，越位
                dp.append(s[i]+ min(dp[i-1],dp[i-2]))
            return min(dp[len(s)-1],dp[len(s)-2])

    pass


if __name__ == '__main__':
    # 读取第一行的n,即有几个编码串
    consum= list(map(int,sys.stdin.readline().split()))
    print(Solution().count_min_sum(consum))
    print(Solution1().count_sum_min(consum))
    # print(consum)
