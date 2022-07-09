"""
题目描述：正则表达式匹配

请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # m= '.' not in s and '*' not in s and '.' not in p and '*' not in p
        # if len(s)!=len(p) and m:
        #     return False
        # if len(s)==len(p) and m:
        #     for i in range(len(s)):
        #         if s[i]==p[i]:
        #             continue
        #         else:
        #             return False
        #     return True
        # if
        # 第一步删除多余的空格
        s = s.strip()

        pass