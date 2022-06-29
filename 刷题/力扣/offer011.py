# -*- coding: utf-8 -*-
# @Time : 2022/7/2 2:09
# @Author : hejunran
"""
题目描述：旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在重复元素值的数组numbers，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。
请返回旋转数组的最小元素。例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。

注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

"""
from typing import List

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        return min(numbers)

class Solution2:
    def minArray(self, numbers: List[int]) -> int:
        length =len(numbers)
        low =0
        high = length-1
        while low<high:
            mid = low+(high-low)//2        # 整数除法 //     除法/
            if numbers[mid]>numbers[high]:
                low =mid+1
            elif numbers[mid]<numbers[high]:
                high=mid
            else:
                high=high-1

        return numbers[low]
        # return min(numbers)

if __name__ == '__main__':
    Solution2().minArray(numbers=[1,1])