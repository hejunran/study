# -*- coding: utf-8 -*-
# @Time : 2022/7/3 14:57
# @Author : hejunran


"""
题目描述：判断机器人能够到达的位置

深度优先遍历加回溯标记能到达的位置，注意，这个起始位置是从（0，0）开始的，因此外部不需要多调用dfs
剪枝： 在搜索中，遇到数位和超出目标值、此元素已访问，则应立即返回，称之为 可行性剪枝

"""
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        ss=[]
        for i in range(m):
            s = []
            for j in range(n):
                s.append(0)
            ss.append(s)

        def dfs(i,j,k):
            if  i<0 or i>=m or j<0 or j>=n: return False
            if ss[i][j]==1:
                return False
            if i//100 + i//10%10 + i%10 + j//100 + j//10%10 + j%10>k:
                return False
            else:
                ss[i][j]=1
                while dfs(i-1,j,k) or dfs(i+1,j,k) or dfs(i,j-1,k) or dfs(i,j+1,k):
                    continue
                return False


        dfs(0,0,k)
        count=0
        for i in range(m):
            for j in range(n):
                if ss[i][j]==1:
                    count =count +1
        return count




# 利用集合记录访问过的位置。
class Solution2:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            if i >= m or j >= n or k < si + sj or (i, j) in visited: return 0
            visited.add((i,j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
        visited = set()
        return dfs(0, 0, 0, 0)


if __name__ == '__main__':
    m=1
    n=2
    k=1
    Solution().movingCount(m,n,k)