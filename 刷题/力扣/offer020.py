# -*- coding: utf-8 -*-
# @Time : 2022/7/5 17:26
# @Author : hejunran
"""
题目描述：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）

"""

class Solution:
    def isNumber(self, s: str) -> bool:
        if s==' ':return False
        # 第一步删除多余的空格
        s=s.strip()

        # 设置标志位符号
        is_number=is_e=is_sign=is_dot=False
        i =0
        while i<len(s):
            if '0'<=s[i]<='9':  # 判断当时是否是数字，如果是直接进行下一个判断
                is_number=True
                i= i+1
                continue
            if i==len(s):
                break
            if s[i]=='e' or s[i]=='E':
                if not is_number or is_e: # 判断e之前是否有数字和e，如果有数字才可以，没有为假的
                    return False
                is_e=True
                is_number=False
                is_dot=False
                is_sign=False
                i = i+1
                # continue
            elif s[i] in '+-':
                if is_sign or is_number or is_dot:   # 判断+-号之前有没有小数点，整数，+——号
                    return False
                is_sign=True
                i = i+1

            elif s[i] =='.':
                if is_dot or is_e:
                    return False
                is_dot=True
                i = i+1
            elif s[i]==' ':
                break
            else:
                return False

        return is_number and len(s)==i

if __name__ == '__main__':
    print(Solution().isNumber('3.'))