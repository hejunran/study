#_*_cording.utf-8_*_
# 开发团队:开心科研
# 开发人员:Administrator
# 开发时间:2021/6/26 002616:32
# 文件名称:function_demo1
# 开发工具:PyCharm

"""
函数 : 复用
格式：
def 函数名（【参数1，参数2，……】）：
    代码
函数名：get_name()
        search()
代码：
    封装重复内容

无参数：
    def  函数名（）：
        代码
有参数：
    def 函数名（【参数1，参数2，……】）：
        代码
"""
import random

def generate_code():
    # 生成验证码
    s='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789'
    code=''
    while True:
        t=random.randint(0,len(s))       # random.randint(start,end)的功能是在start到end之间产生一个随机数
        code+=s[t]
        if 4==len(code):
            break
    print(code)
    return code


def login():
    username=input('请输入用户名：')
    passward=input('请输入密码：')
    if username=='hejunran' and passward=='123456':
        print('登录成功')
    else:
        print('登录失败')

if __name__ == '__main__':
    print(generate_code)     # 函数名为加载到内存中的地址
    generate_code()