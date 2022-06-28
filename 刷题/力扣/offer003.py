# -*- coding: utf-8 -*-
# @Time : 2022/6/28 15:13
# @Author : hejunran

from typing import List
import sys

"""
题目描述：
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
"""

# 方法一：利用set集合的特点，集合中没有重复的元素(hash表）,
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        length = len(nums)
        # out=[]
        s = set()
        for i in range(length):
            if nums[i] in s:  # 如果表中已经有了该元素，则返回该值，否则加入表中
                return nums[i]
            else:
                s.add(nums[i])
        return -1

# 方法二：原地交换,因为是0到n-1之间的数，那么这之间数字和序号就是可以对应的
# eg: n=[2, 3, 1, 0, 2, 5, 3]
class Solution2:
    def findRepeatNumber(self, nums: List[int]) -> int:
        length = len(nums)

        i = 0
        while i<length:
            if nums[i]==i:
                i = i +1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]],nums[i] = nums[i], nums[nums[i]]

        return -1



if __name__ == '__main__':
    lines = sys.stdin.readline().strip()
    n = lines.split(',')
    # n =
    s = Solution().findRepeatNumber(n)
    pass